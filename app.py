from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="database-1.cyfmeu8sc41r.us-east-1.rds.amazonaws.com",
    user="admin", # your username that you provided to RDS
    password="passwd123", # your password that you provided to RDS
    database="information"  # your database that you created  in database server 
)

@app.route("/", methods=["GET", "POST"])
def index():
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        cursor.execute("INSERT INTO users (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, phone))
        db.commit()
    cursor.execute("SELECT * FROM users ORDER BY submitted_at DESC")
    users = cursor.fetchall()
    cursor.close()
    return render_template("index.html", users=users)

@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        cursor.execute("UPDATE users SET first_name=%s, last_name=%s, email=%s, phone=%s WHERE id=%s",
                       (first_name, last_name, email, phone, user_id))
        db.commit()
        cursor.close()
        return redirect(url_for("index"))
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template("edit.html", user=user)

@app.route("/delete/<int:user_id>")
def delete(user_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    db.commit()
    cursor.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
