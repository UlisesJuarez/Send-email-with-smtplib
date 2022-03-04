import pandas
import datetime as dt
import smtplib
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

fecha=dt.datetime.now()
email = os.getenv("CORREO")
password = os.getenv("PASSWORD")

fecha_actual=(fecha.month,fecha.day)
archivo=pandas.read_csv("day 32 send email/birthdays.csv")
fechas_cumples={(fecha["month"],fecha["day"]): fecha for (index,fecha) in archivo.iterrows()}

if fecha_actual in fechas_cumples:
    cumpleañero=fechas_cumples[fecha_actual]
    cartas_path=f"day 32 send email/letter_templates/felicitacion_{randint(1,3)}.txt"
    with open(cartas_path) as carta:
        contenido=carta.read()
        contenido=contenido.replace("[nombre]",cumpleañero["name"])
    with smtplib.SMTP("smtp.office365.com:587") as conexion:
        conexion.starttls()
        conexion.login(email,password)
        conexion.sendmail(from_addr=email,to_addrs=cumpleañero["email"],msg=f"Subject:birthday\n\n{contenido}")
    print("correo enviado")
