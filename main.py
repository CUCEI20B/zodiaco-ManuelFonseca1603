dia = int(input("Escribe el dia: "))
mes = int(input("Escribe el mes: "))

if dia >= 20 and mes == 1 or dia <= 18 and mes == 2:
    print("Eres Acuario")
elif  dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
    print("Eres Piscis")
elif dia >= 21 and mes == 3 or dia <= 19 and mes == 4:
    print("Eres Aries")
elif dia >= 20 and mes == 4 or dia <= 20 and mes == 5:
    print("Eres Tauro")
elif dia >= 21 and mes == 5 or dia <=20 and mes == 6:
    print("Eres Geminis")
elif dia >= 21 and mes == 6 or dia <= 22 and mes == 7:
    print("Eres Cancer")
elif dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
    print("Eres Leo")
elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
    print("Eres Virgo")
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
    print("Eres Libra")
elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
    print("Eres Escorpio")
elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
    print("Eres Sagitario")
else:
    print("Eres Capricornio")