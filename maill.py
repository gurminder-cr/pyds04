import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_HOST = "smtpout.secureserver.net"
SMTP_PORT = 465  # use 587 if 465 is blocked
SENDER_EMAIL = ""
SENDER_PASSWORD = ""  # never hardcode this

def send_mail(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Port 465 uses SSL from the start
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

    print("Email sent successfully!")

if __name__ == "__main__":
    send_mail(
        to_email="coderroots001@gmail.com",
        subject="Test Email",
        body="Hello, this is a test email sent via GoDaddy SMTP."
    )