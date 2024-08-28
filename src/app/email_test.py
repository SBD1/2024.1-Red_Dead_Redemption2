import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Generate a random numeric token
def generate_token(length=6):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

# Email configuration
sender_email = "bruno.martval@gmail.com"
receiver_email = "bruno.martval@outlook.com"
password = "zahg zlrq amju voxg"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create the numeric token
token = generate_token()

# Email content
subject = "Your Confirmation Token"
body = f"Your confirmation token is: {token}"

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
