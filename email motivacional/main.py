import datetime as dt
import smtplib
from random import choice
import os
from dotenv import load_dotenv

load_dotenv()

email =os.getenv("CORREO")
password = str(os.getenv("PASSWORD"))
now=dt.datetime.now()
weekday=now.weekday()

if weekday==3:
    with open("day 32 send email/email motivacional/quotes.txt") as file:
        all_quotes=file.readlines()
        quote=choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.office365.com:587") as conexion:
        conexion.starttls()
        conexion.login(email,password)
        conexion.sendmail(from_addr=email,to_addrs="velascoespinosad@gmail.com",msg=f"Subject:Monday Motivation\n\n{quote}")
    print("correo enviado")