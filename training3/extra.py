#Indica si l'any introduït per l'usuari és de traspàs o no

print ("Introdueix un any per saber si és de traspàs o no.")

any = int(input())

divisible4 = any%4
divisible100 = any%100

if divisible4 or divisible100 == 0:
    print (f"{any} és un any de traspàs.")
else:
    print (f"{any} NO és un any de traspàs.")

quit ()