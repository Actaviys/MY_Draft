import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Налаштування
SMTP_SERVER = "youremail@gmail.com"  # Для Gmail
SMTP_PORT = 587

EMAIL_SENDER = "pc.sending.notification@gmail.com" # youremail@gmail.com
EMAIL_PASSWORD = "*** ***** ***"  # Використовуйте пароль додатка, якщо увімкнено 2FA

EMAIL_RECEIVER = "useremail@gmail.com"


 

# Відправка листа
def send_message_to_email(text_message, text_header="Привіт! Це тестове повідомлення з Python."):
    # Створення листа
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = text_header

    body = text_message
    msg.attach(MIMEText(body, "plain"))
    # print(msg.as_string()) #
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Шифрування з'єднання
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("Лист успішно відправлено!")
    except Exception as e:
        print("Помилка:", e)


send_message_to_email("Привіт Дмитро \nПовідомлення про успіх")




# def main():
#     pass


# if __name__ == "__main__":
#     main()