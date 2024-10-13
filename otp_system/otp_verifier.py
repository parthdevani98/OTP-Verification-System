# otp_verifier.py

from tkinter import messagebox


class OTPVerifier:
    def __init__(self, attempts=3):
        self.generated_otp = None
        self.attempts = attempts

    def set_generated_otp(self, otp):
        self.generated_otp = otp

    def verify_otp(self, user_otp):
        if user_otp.isdigit() and int(user_otp) == self.generated_otp:
            messagebox.showinfo("Success", "Access granted!")
            return True
        else:
            self.attempts -= 1
            messagebox.showerror("Error", "Invalid OTP. Please try again.")
            if self.attempts == 0:
                messagebox.showerror("Error", "You have exhausted all attempts.")
                return False
            return None
