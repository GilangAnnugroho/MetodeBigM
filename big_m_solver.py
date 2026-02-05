import numpy as np
import pandas as pd

# Konstanta Big M (Penalti Besar)
M_VAL = 1e6  # 1.000.000 dianggap cukup besar untuk kasus ini
EPS = 1e-9
DISPLAY_DECIMALS = 2

# =========================
# Helpers
# =========================
def fmt(x: float) -> float:
    if x is None:
        return x
    if abs(x) < EPS:
        return 0.0
    return float(np.round(x, DISPLAY_DECIMALS))

def sign_flip(s: str) -> str:
    return {"<=": ">=", ">=": "<=", "=": "="}[s]

def build_big_m_model(c, A, signs, b, sense):
    """
    Membangun model Big M.
    Menambahkan Slack (<=), Surplus (>=), dan Artificial Variables (>=, =).
    Memberikan penalti M pada koefisien fungsi tujuan untuk variabel Artificial.

    Catatan implementasi:
    - Tableau dibangun untuk skema internal "maximize".
    - Jika sense=="min", koefisien tujuan internal dibuat -c agar menjadi maximize(-Z).
    - Penalti untuk artificial selalu -M pada objective internal (maximize).
    """
    m, n = A.shape

    # 1) Standarisasi Min/Max
    if sense == "min":
        c_eff = -np.array(c, dtype=float)
    else:
        c_eff = np.array(c, dtype=float)

    var_names = [f"X{i+1}" for i in range(n)]
    A_work = np.array(A, dtype=float).copy()
    b_work = np.array(b, dtype=float).copy()
    signs_work = list(signs)

    # Normalisasi RHS agar positif
    for i in range(m):
        if b_work[i] < -EPS:
            A_work[i, :] *= -1
            b_work[i] *= -1
            signs_work[i] = sign_flip(signs_work[i])

    cols = [A_work]
    basis = [None] * m

    # Koefisien objective (termasuk tambahan variabel)
    c_tableau = list(c_eff)

    slack_count = 0
    surplus_count = 0
    art_count = 0

    eq_text = []

    # 2) Tambah variabel tambahan sesuai tanda constraint
    for i in range(m):
        s = signs_work[i]

        # Buat teks persamaan untuk display
        row_text_parts = []
        for j in range(n):
            if abs(A_work[i, j]) > EPS:
                row_text_parts.append(f"{A_work[i, j]:g}{var_names[j]}")
        lhs_base = " + ".join(row_text_parts) if row_text_parts else "0"

        if s == "<=":
            # + Slack
            slack_count += 1
            name = f"S{slack_count}"
            var_names.append(name)
            col = np.zeros((m, 1))
            col[i, 0] = 1.0
            cols.append(col)
            basis[i] = name
            c_tableau.append(0.0)

            eq_text.append(f"{lhs_base} + {name} = {b_work[i]:g}")

        elif s == ">=":
            # - Surplus + Artificial
            surplus_count += 1
            u_name = f"E{surplus_count}"
            var_names.append(u_name)
            ucol = np.zeros((m, 1))
            ucol[i, 0] = -1.0
            cols.append(ucol)
            c_tableau.append(0.0)

            art_count += 1
            a_name = f"A{art_count}"
            var_names.append(a_name)
            acol = np.zeros((m, 1))
            acol[i, 0] = 1.0
            cols.append(acol)
            basis[i] = a_name
            c_tableau.append(-M_VAL)

            eq_text.append(f"{lhs_base} - {u_name} + {a_name} = {b_work[i]:g}")

        elif s == "=":
            # + Artificial
            art_count += 1
            a_name = f"A{art_count}"
            var_names.append(a_name)
            acol = np.zeros((m, 1))
            acol[i, 0] = 1.0
            cols.append(acol)
            basis[i] = a_name
            c_tableau.append(-M_VAL)

            eq_text.append(f"{lhs_base} + {a_name} = {b_work[i]:g}")

        else:
            raise ValueError(f"Unknown sign: {s}")

    Aeq = np.concatenate(cols, axis=1)
    return var_names, Aeq, b_work, basis, np.array(c_tableau, dtype=float), eq_text


def make_tableau(Aeq, beq, c_tableau):
    """
    Membuat tableau simplex dengan format:
      baris 0: -Z + Σ(cj * xj) = 0
      baris i: constraint i
    """
    m, n_total = Aeq.shape

    T = np.zeros((m + 1, 1 + n_total + 1), dtype=float)

    # Isi constraints
    T[1:, 1:1 + n_total] = Aeq
    T[1:, -1] = beq

    # Objective row awal
    T[0, 0] = -1.0
    T[0, 1:1 + n_total] = c_tableau
    T[0, -1] = 0.0

    return T


def canonicalize_objective(T, var_names, basis):
    """
    PENTING UNTUK BIG M:
    Jika basis awal mengandung artificial, maka baris tujuan (Z-row) mengandung -M.
    Kita harus membuat semua variabel basis memiliki koefisien 0 di baris Z dengan OBE:
      Z_row = Z_row - (coef_basis_di_Z * row_basis)
    """
    col_index = {name: idx for idx, name in enumerate(var_names)}
    for i, bname in enumerate(basis, start=1):
        if bname is None:
            continue
        j = 1 + col_index[bname]
        coef = T[0, j]
        if abs(coef) > EPS:
            T[0, :] = T[0, :] - coef * T[i, :]

    T[np.abs(T) < EPS] = 0.0
    return T


def select_entering(T):
    """
    Aturan entering variable untuk format row 0: -Z + Σ(cj * xj) = RHS.
    Untuk maximization pada format ini, variabel masuk = koefisien POSITIF terbesar di baris 0.
    Jika tidak ada koefisien positif -> optimal.
    """
    row = T[0, 1:-1]
    max_val = np.max(row)
    if max_val <= EPS:
        return None
    j_rel = int(np.argmax(row))
    return 1 + j_rel


def ratio_test(T, enter_col):
    """
    Ratio test: min RHS_i / a_i_enter untuk a_i_enter > 0
    """
    m = T.shape[0] - 1
    best_ratio = None
    best_row = None

    for i in range(1, m + 1):
        val = T[i, enter_col]
        if val > EPS:
            r = T[i, -1] / val
            if best_ratio is None or r < best_ratio:
                best_ratio = r
                best_row = i

    return best_row, best_ratio


def pivot_operation(T, basis, var_names, leave_row, enter_col):
    """
    Operasi pivot simplex (Gauss-Jordan):
    - normalisasi baris pivot
    - eliminasi kolom entering di baris lain
    - update basis
    """
    pivot_val = T[leave_row, enter_col]
    T[leave_row, :] /= pivot_val

    for i in range(T.shape[0]):
        if i != leave_row:
            factor = T[i, enter_col]
            T[i, :] -= factor * T[leave_row, :]

    basis[leave_row - 1] = var_names[enter_col - 1]
    T[np.abs(T) < EPS] = 0.0
    return T, basis


def tableau_to_display(T, var_names, basis, enter_col=None, leave_row=None, ratio=None):
    """
    Membuat DataFrame tableau untuk ditampilkan di UI.
    """
    cols = ["Basis", "Z"] + var_names + ["RHS", "Ratio"]
    data = []

    # Row Z
    z_row = ["Z", fmt(T[0, 0])] + [fmt(x) for x in T[0, 1:-1]] + [fmt(T[0, -1]), ""]
    data.append(z_row)

    # Rows constraints
    for i in range(1, T.shape[0]):
        r_val = ""
        if i == leave_row and ratio is not None:
            r_val = fmt(ratio)
        elif enter_col is not None and T[i, enter_col] > EPS:
            r_val = fmt(T[i, -1] / T[i, enter_col])

        row = [basis[i - 1], fmt(T[i, 0])] + [fmt(x) for x in T[i, 1:-1]] + [fmt(T[i, -1]), r_val]
        data.append(row)

    df = pd.DataFrame(data, columns=cols)
    return df


def _detect_infeasible_big_m(final_x, var_names, eps_infeasible=1e-6):
    """
    Deteksi infeasible untuk Big M:
    Jika setelah proses simplex selesai, masih ada artificial variable A_k > eps,
    maka masalah asli (tanpa artificial) tidak feasible.

    Return:
      - (is_infeasible: bool, offenders: list[str])
    """
    offenders = []
    for name in var_names:
        if name.startswith("A"):
            if final_x.get(name, 0.0) > eps_infeasible:
                offenders.append(name)
    return (len(offenders) > 0), offenders


def big_m_simplex(c, A, signs, b, sense="min", max_iter=100):
    """
    Menyelesaikan LP dengan metode Big M + Simplex.

    Input:
      c, A, signs, b, sense
    Output dict:
      status, x, z, logs, eq_text, var_names
    """
    # 1) Build model Big M
    var_names, Aeq, beq, basis, c_tableau, eq_text = build_big_m_model(c, A, signs, b, sense)

    # 2) Initial tableau
    T = make_tableau(Aeq, beq, c_tableau)

    # 3) Canonicalize objective (penting Big M)
    T = canonicalize_objective(T, var_names, basis)

    logs = []
    status = "running"

    for iteration in range(max_iter):
        z_current = T[0, -1]

        enter_col = select_entering(T)

        if enter_col is None:
            df = tableau_to_display(T, var_names, basis)
            logs.append({
                "iter": iteration,
                "df": df,
                "note": "Optimality Condition Met (No positive coeff in Z row)",
                "z": z_current
            })
            status = "optimal"
            break

        leave_row, best_ratio = ratio_test(T, enter_col)

        df = tableau_to_display(T, var_names, basis, enter_col, leave_row, best_ratio)
        enter_name = var_names[enter_col - 1]

        if leave_row is None:
            status = "unbounded"
            logs.append({
                "iter": iteration,
                "df": df,
                "note": "Unbounded Solution",
                "z": z_current
            })
            break

        leave_name = basis[leave_row - 1]

        logs.append({
            "iter": iteration,
            "df": df,
            "enter": enter_name,
            "leave": leave_name,
            "pivot_val": T[leave_row, enter_col],
            "note": f"Pivot: {enter_name} enters, {leave_name} leaves",
            "z": z_current
        })

        # Pivot
        T, basis = pivot_operation(T, basis, var_names, leave_row, enter_col)

    # Jika loop habis tanpa break
    if status == "running":
        status = "iter_limit"
        df = tableau_to_display(T, var_names, basis)
        logs.append({
            "iter": max_iter,
            "df": df,
            "note": "Iteration limit reached (no conclusion)",
            "z": T[0, -1]
        })

    # 4) Extract final solution
    final_x = {name: 0.0 for name in var_names}
    for i, bname in enumerate(basis):
        final_x[bname] = T[i + 1, -1]

    # 5) Hitung nilai objective asli dari c (hanya X1..Xn)
    z_final_calc = 0.0
    for i, coef in enumerate(c):
        var_n = f"X{i+1}"
        z_final_calc += float(coef) * float(final_x.get(var_n, 0.0))

    # 6) DETEKSI INFEASIBLE (PENTING UNTUK BIG M)
    # Hanya relevan bila status optimal (atau iter_limit tapi ingin deteksi), namun paling aman:
    infeasible, offenders = _detect_infeasible_big_m(final_x, var_names)

    if infeasible and status == "optimal":
        status = "infeasible"
        # Tambahkan log penjelasan di akhir untuk keperluan sidang/penilaian
        df = tableau_to_display(T, var_names, basis)
        logs.append({
            "iter": (logs[-1]["iter"] + 1) if logs else 0,
            "df": df,
            "note": f"Infeasible detected: Artificial variables still > 0 -> {', '.join(offenders)}",
            "z": T[0, -1]
        })

    return {
        "status": status,
        "x": final_x,
        "z": z_final_calc,
        "logs": logs,
        "eq_text": eq_text,
        "var_names": var_names
    }
