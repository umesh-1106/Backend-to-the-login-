from flask import Flask, render_template, request, redirect, url_for, session, flash

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key to enable secure sessions and flashing messages
app.secret_key = "super_secret_admin_key_change_me"

@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Handle the form submission when the user clicks login
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Verify credentials
        if username == "UMESH1106" and password == "8919":
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
            
        # If verification fails, show error message
        flash("Invalid Admin Username or Password", "danger")
        
    # Handle the initial GET request to display the login page
    return render_template("admin_login.html")

# Optional: Placeholder route so url_for("admin_dashboard") doesn't crash your server
@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        flash("Please log in first", "danger")
        return redirect(url_for("admin"))
    return "Welcome to the Admin Dashboard!"

if __name__ == "__main__":
    app.run(debug=True)
