# otp_sender.py

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class OTPSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = "parthdevani98@gmail.com"
        self.password = "qodjdzyegnksgnlx"

    def generate_otp(self):
        return random.randint(100000, 999999)

    def send_otp_via_email(self, otp, recipient_email):
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = recipient_email
        msg["Subject"] = "Your OTP Verification Code"

        body = f"Your OTP is: {otp}"
        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            return True
        except Exception as e:
            print(f"Failed to send OTP: {str(e)}")
            return False
