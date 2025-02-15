import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import time

# Config faylını oxumaq
def read_config():
    with open("config.json", "r") as file:
        config = json.load(file)
    return config

# Token və vaxtı yeniləmək
def update_token(config):
    config["token"] = "yeni_token_here"  # Yeni tokenı əlavə edin
    config["e"] = int(time.time())  # Cari vaxtı yeniləyin
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

# E-poçt göndərmək
def send_email(config):
    sender_email = "your_email@gmail.com"  # Göndərən e-poçt
    receiver_email = "receiver_email@gmail.com"  # Qəbul edən e-poçt
    password = "your_password"  # Göndərən e-poçtun şifrəsi

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Yeni Token və Link"

    body = f"""
    Yeni Token: {config["token"]}
    Yeni Link: {generate_stream_url(config)}
    """
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server
