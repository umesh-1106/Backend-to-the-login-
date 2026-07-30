@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "UMESH1106" and password == "8919":
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))

        flash("Invalid Admin Username or Password", "danger")

    return render_template("admin_login.html")
