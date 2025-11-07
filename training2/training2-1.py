#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 2.1

#Training 2 - Variables i Casting

#Utilitzant el PyCharm realitzeu els següents programes:

#Exercici 1: Escriu un programa que calculi l'àrea d'un quadrat on la mida del lateral s'ha d'introduir per teclat.

print ("Introdueix la mida de un costat del quadrat:")

costat = float(input())

if costat <=0:
    print("El costat ha de tenir un valor positiu, torni a introduir el valor del costat:")

    print ("Introdueix la mida de un costat del quadrat:")

    costat = float(input())

area = costat ** 2

#area podria ser float o integer (int), escollim float perquè permet més marge d'operació.

#print ("L'àrea del quadrat proposat és:", area)
# ^És una forma vàlida de donar l'output, però no permet concatenar text després de "area"^

print (f"L'àrea del quadrat proposat és {area} unitats quadrades.")

# ^f string, en Python permeten concatenar text i variables de forma més flexible^

#FINALITZAR EL PROGRAMA
quit ()