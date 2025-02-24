import smtplib

def send_to_email(sd_mesage):
    sender = "pc.sending.notification@gmail.com"
    senderPassw = "********"
    print("1")
    
    # server = smtplib.SMTP("login.live.com", 5000)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    print("2")
    server.login(sender, senderPassw)
    # server.starttls()
    print("3")
    try:
        # server.login(sender, senderPassw)
        # server.sendmail(sender, "actaviys88@gmail.com", sd_mesage)
        
        return "Успішно відправлено"
    
    except Exception:
        print(f"{Exception}: Невірний логін або пароль!!!")
    
    return print("4")

print(send_to_email("Повідомлення про успіх :)"))



# def main():
#     pass


# if __name__ == "__main__":
#     main()