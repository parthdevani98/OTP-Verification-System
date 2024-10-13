# otp_verifier.py

from tkinter import messagebox


class OTPVerifier:
    def __init__(self, attempts=3):
        self.generated_otp = None
        self.attempts = attempts

    def set_generated_otp(self, otp):
        """
        Set the generated One-Time Password (OTP).

        This method stores the provided OTP in the instance variable
        `generated_otp`, allowing it to be accessed later for
        verification purposes.

        Args:
            otp (int): The OTP to be stored, expected to be a 6-digit integer.
        """
        self.generated_otp = otp

    def verify_otp(self, user_otp):
        """
        Verify the One-Time Password (OTP) entered by the user.

        This method checks if the entered OTP is valid by comparing it
        against the generated OTP. It also manages the number of
        attempts allowed for entering the correct OTP.

        Args:
            user_otp (str): The OTP entered by the user, expected to be
                             a string that can represent a 6-digit integer.

        Returns:
            bool: True if the OTP is valid and access is granted.
                   False if the OTP is invalid and no attempts are left.
                   None if the OTP is invalid but attempts are remaining.
        """
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
