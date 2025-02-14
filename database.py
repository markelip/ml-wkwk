import csv
import os

DATABASE_FILE = "user_data.csv"

# Buat file CSV kalau belum ada
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "w", newline="") as db:
        writer = csv.writer(db)
        writer.writerow(["User ID", "Server ID", "Email", "Login Method", "Password", "WhatsApp", "Price Offer", "Screenshot File"])

def save_user_data(user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path):
    with open(DATABASE_FILE, "a", newline="") as db:
        writer = csv.writer(db)
        writer.writerow([user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path])
