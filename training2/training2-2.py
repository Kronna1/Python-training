#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 2.2

#Training 2 - Variables i Casting

#Utilitzant el PyCharm realitzeu els següents programes:

#Exercici 2: Escriu un programa que donat dos nombres enters que introduirem per teclat ens calculi la suma, la resta, la multiplicació i la divisió.

#OBTENCIÓ I CASTING DE L'INPUT 1
print("Introdueix el primer nombre a operar:")
numero1 = float(input())

#OBTENCIÓ I CASTING DE L'INPUT 2
print("Introdueix el segon nombre a operar:")
numero2 = float(input())

#REALITZACIÓ DE LES OPERACIONS
#Suma
suma = numero1 + numero2

#Resta
resta = numero1 - numero2

#Producte
producte = numero1 * numero2

#Divisió
divisio = numero1 / numero2

#MOSTRAR EL RESULTAT DE LES OPERACIONS
print(f"Resultat de la suma dels nombres introduïts: {suma}" )

print(f"Resultat de la resta dels nombres introduïts: {resta}")

print(f"Resultat del producte dels nombres introduïts: {producte}")

print(f"Resultat de la divisió dels nombres introduïts: {divisio}")

#FINALITZAR EL PROGRAMA
quit ()