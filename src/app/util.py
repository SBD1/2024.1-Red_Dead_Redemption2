import os
import platform
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from dotenv import load_dotenv

load_dotenv()

def clear_screen():
    if platform.system() == "Windows": os.system('cls')
    else: os.system('clear')

def go_back(msg = "\nPressione Enter para continuar"):
    input(msg)

def print_prompt(file):
    with open(f"app/prompts/{file}.txt", "r") as f:
       print(f.read())
    
def generate_token(length=6):
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def send_email(receiver_email, token, name):
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("PASSWORD")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    subject = "RDR2: Seu token de confirmação"
    
    with open("assets/email_template.html", "r") as file:
        html_body = file.read()

    html_body = html_body.replace("{token}", token).replace("{nome}", name)
    
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        print(f"Failed to send email: {e}")
        exit()
    finally:
        server.quit()