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
        """
        Generate a random 6-digit One-Time Password (OTP).

        This method utilizes the random number generator to create an
        OTP within the range of 100000 to 999999, ensuring that the
        result is always a 6-digit integer.

        Returns:
            int: A randomly generated 6-digit OTP.
        """
        return random.randint(100000, 999999)

    def send_otp_via_email(self, otp, recipient_email):
        """
        Send a One-Time Password (OTP) to the specified email address.

        This method constructs an email message containing the OTP and
        sends it to the recipient's email address using SMTP. It utilizes
        the Gmail SMTP server and requires valid sender email credentials.

        Args:
            otp (int): The OTP to be sent to the recipient.
            recipient_email (str): The email address of the recipient.

        Returns:
            bool: True if the OTP was sent successfully, False otherwise.
        """
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
