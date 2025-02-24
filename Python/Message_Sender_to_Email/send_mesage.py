import smtplib

def send_to_email(sd_mesage):
    sender = "pc.sending.notification@gmail.com"
    senderPassw = "vtys1612"
    print("1")
    
    server = smtplib.SMTP("smtp.google.com", 587)
    print("2")
    server.starttls()
    print("3")
    try:
        server.login(sender, senderPassw)
        server.sendmail(sender, "actaviys88@gmail.com", sd_mesage)
        
        return "Успішно відправлено"
    
    except Exception:
        print(f"{Exception}: Невірний логін або пароль...")
    
    return print("4")

print(send_to_email("Повідомлення про успіх :)"))



# def main():
#     pass


# if __name__ == "__main__":
#     main()