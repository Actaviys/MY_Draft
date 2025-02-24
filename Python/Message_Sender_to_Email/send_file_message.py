import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Налаштування
SMTP_SERVER = "smtp.gmail.com"  
SMTP_PORT = 587

EMAIL_SENDER = "youremail@gmail.com" 
EMAIL_PASSWORD = "*** ***** ***"  # Використовуйте пароль додатка, якщо увімкнено 2FA

EMAIL_RECEIVER = "useremail@gmail.com"



# Створення листа
msg = MIMEMultipart()
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg["Subject"] = "Привіт це лист з вкладенням та повідомленням"

# Текст листа
body = "Файл про успіх."
msg.attach(MIMEText(body, "plain"))

# 📌 Додаємо вкладення (файл)
file_path = "filename.txt"  # Шлях до файлу (може бути .png, .jpg, .pdf і т. д.)
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Кодуємо файл у Base64
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={file_path}")

# Додаємо вкладення до листа
msg.attach(part)

# Відправка листа
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.quit()
    print("Лист успішно відправлено!")
except Exception as e:
    print("Помилка:", e)