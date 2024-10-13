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
        """
        Create and arrange the GUI widgets for the OTP verification system.

        This method initializes the email input frame and OTP input frame,
        including labels, entry fields, and buttons. It sets up the layout
        using grid and pack geometry managers, allowing users to enter their
        email and OTP, and to submit the OTP for verification.

        The following widgets are created:
            - Email input frame with a label, entry field, and "Send OTP" button.
            - OTP input frame with a label and entry field.
            - "Submit OTP" button that is initially disabled until the OTP is sent.
            - Attempts label to display the number of remaining OTP attempts.
        """
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
        """
        Generate and send a One-Time Password (OTP) to the user's email.

        This method retrieves the email address entered by the user,
        generates a 6-digit OTP, and sends it to the specified email
        address using the OTP sender. It also handles input validation
        and updates the user interface based on the success or failure
        of the OTP sending process.

        If the email is empty, an error message is displayed. If the
        OTP is successfully sent, the generated OTP is stored for
        verification, the OTP input frame is displayed, and the "Submit
        OTP" button is enabled. If the OTP sending fails, an error
        message is shown.

        Attributes:
            recipient_email (str): The email address to which the OTP will be sent.
            generated_otp (int): The OTP that is generated and sent to the user.
        """
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
        """
        Handle the submission of the OTP entered by the user.

        This method retrieves the OTP from the entry field and verifies
        it using the OTP verifier. If the OTP is valid, the application
        is closed. If the user has exhausted their attempts, the
        application is also closed. If the OTP is invalid but attempts
        remain, the label displaying the number of remaining attempts
        is updated to reflect the new count.

        Attributes:
            user_otp (str): The OTP entered by the user for verification.
        """
        user_otp = self.otp_entry.get()
        if self.otp_verifier.verify_otp(user_otp):
            self.root.quit()
        elif self.otp_verifier.attempts == 0:
            self.root.quit()
        else:
            self.attempts_label.config(
                text=f"Attempts left: {self.otp_verifier.attempts}"
            )
