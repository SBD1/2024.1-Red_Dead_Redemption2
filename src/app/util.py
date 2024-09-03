import os
import platform
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

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

def send_email(receiver_email, token):
    sender_email = "bruno.martval@gmail.com"
    password = "zahg zlrq amju voxg"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    subject = "Seu código de confirmação"

    try:
        with open("/assets/email_template.html", "r") as file:
            html_body = file.read()
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return

    html_body = html_body.replace("{token}", token)
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
        print(f"Houve uma falha no envio do email: {e}")
    finally:
        server.quit()