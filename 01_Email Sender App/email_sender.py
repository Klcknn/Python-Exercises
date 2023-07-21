import ssl, smtplib

smtp_port = 587  # Standart SMTP port değeri
smtp_server =  "smtp.gmail.com"  # Google SMTP Server adresi

email_from = "kenanklc.76@gmail.com"
email_to = "kenanklc.76@gmail.com"
password = "bcyyrzxwffrjjzrm"  # Kendi Google Hesabımızın Güvenlik bölümünün altından Uygulama Şifreleri başlığı altında yeni bir uygulama şifresini oluşturuyoruz ve oluşturmuş olduğumuz uygulama şifresini kopyalayıp buraya yapıştırıyoruz. 

message = "Mesaj içeriğini bu kısma giriniz. "    # mesajın içeriği 
email_context = ssl.create_default_context()

try:
    print("Connecting to SMTP server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=email_context)
    TIE_server.login(email_from, password)
    print("Connected to SMTP server...")

    print("****************************")
    print( f"Sending email to - {email_to}" )
    TIE_server.sendmail(email_from, email_to, message)
    print( f"Email successfully sent to - {email_to}" )

except Exception as e:
    print(e)

finally:
    TIE_server.quit()










