from flask import Flask, render_template, request
import numpy as np
import big_m_solver

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/input")
def input_page():
    return render_template("input.html")


def parse_input(form):
    """
    Parse input dari form:
    - var_name[] : label menu
    - c[]        : biaya per porsi
    - w[]        : berat per porsi (gram)
    - A[i][j]    : koefisien gizi per porsi
    - sign[]     : tanda kendala
    - req[]      : standar gizi per siswa (baseline)
    - b[]        : RHS total (auto = req * students)
    - constraint_name[] : nama kendala (opsional untuk display)
    """
    var_labels = [x.strip() for x in form.getlist("var_name[]")]
    c_cost = list(map(float, form.getlist("c[]")))
    w_gram = list(map(float, form.getlist("w[]")))

    b = list(map(float, form.getlist("b[]")))
    signs = form.getlist("sign[]")

    req = form.getlist("req[]")
    req = list(map(float, req)) if req else []

    constraint_names = form.getlist("constraint_name[]")

    m = len(b)
    n = len(c_cost)

    A = []
    for i in range(m):
        row = []
        for j in range(n):
            val = float(form.get(f"A[{i}][{j}]", 0))
            row.append(val)
        A.append(row)

    final_labels = []
    for i, lbl in enumerate(var_labels):
        final_labels.append(lbl if lbl else f"X{i+1}")

    return (
        final_labels,
        np.array(c_cost, dtype=float),
        np.array(w_gram, dtype=float),
        np.array(A, dtype=float),
        list(signs),
        np.array(b, dtype=float),
        np.array(req, dtype=float) if len(req) else np.array([], dtype=float),
        constraint_names
    )


@app.route("/solve", methods=["POST"])
def solve():
    sense = request.form.get("sense", "max").strip().lower()
    budget = float(request.form.get("budget"))
    students = int(request.form.get("students"))

    (var_labels, c_cost, w_gram, A_nut, signs, b, req_per_student, constraint_names) = parse_input(request.form)
    n = len(c_cost)

    # Tambah constraint minimal porsi untuk siswa: sum x >= students
    A_porsi = np.ones((1, n), dtype=float)
    A = np.vstack([A_nut, A_porsi])
    signs2 = signs + [">="]
    b2 = np.append(b, float(students))

    # Tambah constraint budget: cost dot x <= budget
    A_budget = c_cost.reshape(1, -1)
    A = np.vstack([A, A_budget])
    signs2.append("<=")
    b2 = np.append(b2, float(budget))

    # Objective
    if sense == "max":
        c_objective = np.ones(n, dtype=float)   # max total portions
        solver_sense = "max"
        objective_label = "Jumlah Porsi Optimal (Maksimum)"
    else:
        c_objective = c_cost.copy()             # min total cost
        solver_sense = "min"
        objective_label = "Total Biaya Optimal (Minimum)"

    # Solve Big M
    result = big_m_solver.big_m_simplex(
        c_objective, A, signs2, b2, sense=solver_sense
    )

    status = result["status"]
    x = result["x"]
    z = float(result["z"])
    logs = result["logs"]
    eq_text = result["eq_text"]

    # Extract x values
    x_values = np.zeros(n, dtype=float)
    main_vars = []
    for i in range(n):
        val = float(x.get(f"X{i+1}", 0.0))
        x_values[i] = val
        main_vars.append({"label": var_labels[i], "value": round(val, 2)})

    total_portions = float(np.sum(x_values))
    total_cost = float(np.dot(c_cost, x_values))

    # Total nutrition from menu mix
    total_nutrition = np.dot(A_nut, x_values)   # shape (m,)
    nutrition_per_student = total_nutrition / max(students, 1)

    # Baseline nutrition per student (sebelum optimasi) = standar input per siswa
    # Jika user isi 3 kendala (kalori, protein, lemak), ambil 3 pertama.
    baseline = {
        "kalori": round(float(req_per_student[0]), 2) if len(req_per_student) > 0 else 0,
        "protein": round(float(req_per_student[1]), 2) if len(req_per_student) > 1 else 0,
        "lemak": round(float(req_per_student[2]), 2) if len(req_per_student) > 2 else 0,
    }

    actual = {
        "kalori": round(float(nutrition_per_student[0]), 2) if len(nutrition_per_student) > 0 else 0,
        "protein": round(float(nutrition_per_student[1]), 2) if len(nutrition_per_student) > 1 else 0,
        "lemak": round(float(nutrition_per_student[2]), 2) if len(nutrition_per_student) > 2 else 0,
    }

    # Weight calculation
    # total_weight (gram) = sum(w_j * x_j)
    total_weight_gram = float(np.dot(w_gram, x_values))
    weight_per_student_gram = total_weight_gram / max(students, 1)

    ratio_portion = (total_portions / max(students, 1)) if students > 0 else 0.0
    avg_weight_per_portion = (total_weight_gram / total_portions) if total_portions > 0 else 0.0

    weight_info = {
        "total_weight_gram": round(total_weight_gram, 2),
        "avg_weight_per_portion": round(avg_weight_per_portion, 2),
        "ratio_portion": round(ratio_portion, 4),
        "weight_per_student_gram": round(weight_per_student_gram, 2),
    }

    # Card berat awal per menu
    menu_weights = []
    for i in range(n):
        menu_weights.append({
            "label": var_labels[i],
            "weight": round(float(w_gram[i]), 2)
        })

    # Recommendation (menu dominan porsi terbanyak)
    best_menu = "-"
    if n > 0 and total_portions > 0:
        best_menu = var_labels[int(np.argmax(x_values))]

    recommendation_text = (
        f"Menu {best_menu} merupakan menu paling optimal karena memenuhi seluruh "
        f"standar gizi dan menghasilkan porsi terbanyak berdasarkan hasil optimasi."
    )

    # Format logs for HTML
    formatted_logs = []
    for log in logs:
        df = log["df"]
        rows = df.to_dict(orient="records")
        columns = df.columns.tolist()

        for row in rows:
            basis = row.get("Basis", "")
            if isinstance(basis, str) and basis.startswith("X"):
                try:
                    idx = int(basis[1:]) - 1
                    if 0 <= idx < len(var_labels):
                        row["Basis"] = var_labels[idx]
                except:
                    pass

        formatted_logs.append({
            "iter": log.get("iter"),
            "note": log.get("note", ""),
            "columns": columns,
            "rows": rows,
            "enter": log.get("enter"),
            "leave": log.get("leave")
        })

    return render_template(
        "result.html",
        status=status,
        z=round(z, 2),
        objective_label=objective_label,
        main_vars=main_vars,
        logs=formatted_logs,
        eq_text=eq_text,
        budget=budget,
        students=students,
        recommendation=recommendation_text,
        total_portions=round(total_portions, 2),
        total_cost=round(total_cost, 2),
        baseline_nutrition=baseline,
        nutrition=actual,
        menu_weights=menu_weights,
        weight_info=weight_info,
        mode=sense
    )


if __name__ == "__main__":
    app.run(debug=True)
