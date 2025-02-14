from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import csv
from werkzeug.utils import secure_filename
from database import save_user_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Pastikan folder upload ada
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

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

        return redirect(url_for("index"))

    return render_template("index.html")

# Route buat download user_data.csv
@app.route("/download")
def download_file():
    try:
        return send_file("user_data.csv", as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
