# gui.py

import tkinter as tk
from tkinter import messagebox
from .otp_sender import OTPSender
from .otp_verifier import OTPVerifier


class OTPVerificationApp:
    def __init__(self, root, otp_sender):
        self.root = root
        self.root.title("OTP Verification System")

        self.otp_sender = otp_sender
        self.otp_verifier = OTPVerifier()

        self.create_widgets()

    def create_widgets(self):
        self.email_frame = tk.Frame(self.root)
        self.email_frame.pack(pady=20)

        self.email_label = tk.Label(self.email_frame, text="Enter your email:")
        self.email_label.grid(row=0, column=0, padx=10)

        self.email_entry = tk.Entry(self.email_frame, width=30)
        self.email_entry.grid(row=0, column=1)

        self.send_button = tk.Button(
            self.email_frame, text="Send OTP", command=self.send_otp
        )
        self.send_button.grid(row=0, column=2, padx=10)

        self.otp_frame = tk.Frame(self.root)
        self.otp_label = tk.Label(self.otp_frame, text="Enter OTP:")
        self.otp_label.grid(row=0, column=0, padx=10)

        self.otp_entry = tk.Entry(self.otp_frame, width=15)
        self.otp_entry.grid(row=0, column=1)

        self.submit_button = tk.Button(
            self.root, text="Submit OTP", state=tk.DISABLED, command=self.submit_otp
        )
        self.submit_button.pack(pady=20)

        self.attempts_label = tk.Label(
            self.root, text=f"Attempts left: {self.otp_verifier.attempts}"
        )
        self.attempts_label.pack()

    def send_otp(self):
        recipient_email = self.email_entry.get()
        if not recipient_email:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        generated_otp = self.otp_sender.generate_otp()
        if self.otp_sender.send_otp_via_email(generated_otp, recipient_email):
            self.otp_verifier.set_generated_otp(generated_otp)
            messagebox.showinfo("Success", "OTP sent successfully.")
            self.otp_frame.pack(pady=10)
            self.submit_button.config(state=tk.NORMAL)
            self.send_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror(
                "Error", "Failed to send OTP. Please check your email settings."
            )

    def submit_otp(self):
        user_otp = self.otp_entry.get()
        if self.otp_verifier.verify_otp(user_otp):
            self.root.quit()
        elif self.otp_verifier.attempts == 0:
            self.root.quit()
        else:
            self.attempts_label.config(
                text=f"Attempts left: {self.otp_verifier.attempts}"
            )
