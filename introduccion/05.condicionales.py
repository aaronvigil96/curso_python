print("1- Mañana")
print("2- Tarde")
print("3- Noche")
hora = int(input("¿Que turno es ahora?"))

#Si hora es 1 entonces..
if hora == 1:
    print("Buen día")
#Sino si hora es 2 entonces..
elif hora == 2:
    print("Buenas tardes")
#Sino si hora es 3 entonces..
elif hora == 3:
    print("Buenas noches")
#Sino..
else:
    print("No sé como saludarte, porque no indicaste ninguno")
    