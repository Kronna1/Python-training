#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 2.3

#Training 2 - Variables i Casting

#Utilitzant el PyCharm realitzeu els següents programes:

#Exercici 4: (casting) Escriu un programa que donat dos nombres en coma flotant ens retorni un enter.

#OBTENCIÓ I CASTING DE L'INPUT 1
print("Introdueix el primer nombre decimal a operar (empra un punt com a coma)")

decimal1 = float(input())

#OBTENCIÓ I CASTING DE L'INPUT 2
print("Introdueix el segon nombre decimal a operar (empra un punt com a coma)")

decimal2 = float(input())

#OPERAR AMB ELS FLOATS

#Suma
suma = decimal1 + decimal2 

#Resta
resta = decimal1 - decimal2

#Producte
producte = decimal1 * decimal2

#Divisió
divisio = decimal1 // decimal2
# L'operand / executa una divisió float (amb decimal sempre), // correspon a una divisió amb integers (sense decimals).

#CASTEJAR I MOSTRAR ELS RESULTATS

suma = int(suma)
resta = int(resta)
producte = int(producte)
divisio = int(divisio)

print ("Aquests són els resultats enters de les operacions decimals:")
print (f"Suma: {suma}")
print (f"Resta: {resta}")
print (f"Producte: {producte}")
print (f"Divisió: {divisio}")

#FINALITZAR EL PROGRAMA
quit ()