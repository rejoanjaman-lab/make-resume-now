from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/preview", methods=["POST"])
def preview():
    # Collect form fields (simple; expand as you need)
    data = {
        "full_name": request.form.get("full_name", ""),
        "title": request.form.get("title", ""),
        "email": request.form.get("email", ""),
        "phone": request.form.get("phone", ""),
        "summary": request.form.get("summary", ""),
        "education": [],
        "experience": [],
        "skills": [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()],
        "template": request.form.get("template", "clean")
    }

    # Education: allow multiple entries using indexed fields edu_school_1, edu_year_1, ...
    for i in range(1, 6):  # support up to 5 education rows
        school = request.form.get(f"edu_school_{i}")
        degree = request.form.get(f"edu_degree_{i}")
        year = request.form.get(f"edu_year_{i}")
        if school or degree or year:
            data["education"].append({"school": school, "degree": degree, "year": year})

    # Experience: up to 6 rows
    for i in range(1, 7):
        company = request.form.get(f"exp_company_{i}")
        role = request.form.get(f"exp_role_{i}")
        period = request.form.get(f"exp_period_{i}")
        desc = request.form.get(f"exp_desc_{i}")
        if company or role or period or desc:
            data["experience"].append({"company": company, "role": role, "period": period, "desc": desc})

    return render_template("preview.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
