# main.py

import tkinter as tk
from otp_system.otp_sender import OTPSender
from otp_system.gui import OTPVerificationApp


def main():
    """
    Main function to run the OTP Verification Application.

    This function initializes the OTP sender with the sender's email
    and password, sets up the Tkinter root window, and starts the
    OTP Verification application. It also manages the main event
    loop for the Tkinter GUI, allowing for user interaction.

    Note:
        It is recommended to store sensitive credentials such as
        the sender's email and password securely, using environment
        variables or a configuration file, instead of hardcoding
        them in the source code.

    Example:
        If executed as a script, this function will launch the
        OTP Verification GUI application.
    """
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
