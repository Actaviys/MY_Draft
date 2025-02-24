import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Налаштування
SMTP_SERVER = "smtp.gmail.com"  # Для Gmail
SMTP_PORT = 587
EMAIL_SENDER = "pc.sending.notification@gmail.com"
EMAIL_PASSWORD = "vtys1612"  # Використовуйте пароль додатка, якщо увімкнено 2FA
EMAIL_RECEIVER = "actaviys88@gmail.com"

# Створення листа
msg = MIMEMultipart()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg["Subject"] = "Тестове повідомлення"

body = "Привіт! Це тестове повідомлення з Python."
msg.attach(MIMEText(body, "plain"))

# Відправка листа
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Шифрування з'єднання
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.quit()
    print("Лист успішно відправлено!")
except Exception as e:
    print("Помилка:", e)