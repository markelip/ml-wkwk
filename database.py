import csv
import os

CSV_FILE = "data.csv"

def save_user_data(user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["User ID", "Server ID", "Email", "Login Method", "Password", "WhatsApp", "Price Offer", "File Path"])
        writer.writerow([user_id, server_id, email, login_method, password, whatsapp, price_offer, file_path])
