import smtplib

# Тест #
def send_to_email(sd_mesage):
    sender = "youremail@gmail.com"
    senderPassw = "***********"
    print("1")
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 587)
    print("2")
    # server.starttls()
    print("3")
    try:
        server.login(sender, senderPassw)
        server.sendmail(sender, "useremail@gmail.com", sd_mesage)
        
        return "Успішно відправлено"
    
    except Exception as _ex:
        return f"{_ex}\nНевірний логін або пароль!!!"
    
    return print("4")

print(send_to_email("Повідомлення про успіх"))



# def main():
#     pass


# if __name__ == "__main__":
#     main()