@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "UMESH1106" and password == "8919":

            session["admin"] = True

            return redirect(url_for("admin_dashboard"))

        flash("Invalid Username or Password", "danger")

    return render_template("admin_login.html")


@app.route("/admin_dashboard")
def admin_dashboard():

    if "admin" not in session:
        return redirect(url_for("admin"))

    conn = get_db()

    users = conn.execute(
        "SELECT * FROM users ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "admin_dashboard.html",
        users=users
    )


@app.route("/admin_logout")
def admin_logout():

    session.pop("admin", None)

    return redirect(url_for("admin"))
