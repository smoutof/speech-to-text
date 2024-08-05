import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD   
TO_EMAIL = config.TO_EMAIL

def send_email(subject, body, to_email=TO_EMAIL, from_email=EMAIL_ADDRESS):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, EMAIL_PASSWORD)

        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()
