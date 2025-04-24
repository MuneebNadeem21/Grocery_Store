import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "abc@gmail.com"
receiver_email = "newoca8550@kuandika.com"
subject = "Dummy Email"
body = "This is a dummy email from an anonymous sender."

# Gmail SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_password = "23456"  # Use app-specific password if 2FA is enabled

# Function to send email using SMTP
def send_email():
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        
        # Attach the body with the message
        message.attach(MIMEText(body, "plain"))

        # Connect to the Gmail SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)

        print("Email sent successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Send 10 dummy emails
for i in range(1):
    print(f"Sending email {i + 1}...")
    send_email()
