# OTP Verification System

## Project Description

The OTP Verification System is a Python application that generates a One-Time Password (OTP) and sends it to the user's email address for verification. Users can enter the received OTP to gain access. This project utilizes the Tkinter library for the GUI and the SMTP protocol for sending emails.

## Features

- Generate a 6-digit OTP.
- Send OTP to the user's email address.
- User-friendly interface for OTP input and submission.
- Limited attempts for OTP entry to enhance security.
- Error handling for invalid email and OTP.

## Installation

To run this project, ensure you have Python 3.x installed on your machine. Follow these steps to set up the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/OTP-Verification-System.git
   cd OTP-Verification-System
   
2. Install the required packages:

   ```bash
   pip install -r requirements.txt

## Requirements

Create a requirements.txt file with the following content.

tkinter
smtplib
email

Note: tkinter is included in the standard Python library, but it may need to be installed separately on some systems.


## Usage
1. Open the terminal and navigate to the project directory.
2. Run the application:
   ```bash
   python main.py

3. Enter your email address and click "Send OTP."
4. Check your email for the OTP and enter it in the application.
5. Click "Submit OTP" to verify.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/parthdevani98/OTP-Verification-System/blob/main/LICENSE) file for details.




    
