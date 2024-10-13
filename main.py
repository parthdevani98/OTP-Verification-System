# main.py

import tkinter as tk
from otp_system.otp_sender import OTPSender
from otp_system.gui import OTPVerificationApp


def main():
    # Setup sender credentials (can be securely stored as environment variables or .env)
    sender_email = "parthdevani98@gmail.com"
    sender_password = "qodjdzyegnksgnlx"

    # Initialize OTP sender object
    otp_sender = OTPSender(sender_email, sender_password)

    # Initialize Tkinter root window
    root = tk.Tk()

    # Start the OTP Verification app
    app = OTPVerificationApp(root, otp_sender)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
