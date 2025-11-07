#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 4.2

#Training 4 - Bucles

#Exercici 2: Escriu un programa que llegeixi una seqüència de notes (valors de 0 a 10) i finalitzarà la seqüència amb el valor -1. Quan finalitzi ens ha d'indicar si "Hi ha hagut alguna nota que té un 10" o "No hi ha cap 10".

print (f"Introdueix les notes dels teus alumnes. \nQuan acabis, introdueix el nombre -1, per deixar d'introduir notes. \nLlavors veurem si hi ha algun 10 o no.")

#CREACIÓ DE VARIABLES NECESSARIES:

nota = float(input()) #Creem variable nota per guardar l'input de l'usuari.

nota10 = False #Creem una variable boolean que cambiarà a true si nota = 10.

#BUCLE:

while nota != -1: #Mentre nota sigui diferent a -1, s'executarà el bucle.
    
    if nota == 10: #Si nota és 10, el valor de nota10 canviarà a true.
        nota10 = True

    nota = int(input()) #Afegim aquesta línia per tornar a demanar l'input de l'usuari.

print ("Introducció de notes finalitzada.") #Això s'imprimeix quan s'acaba el bucle.

if nota10 == True: #Si hi ha algun 10...
    print ("Hi ha algun 10.") # Imprimirà que "hi ha algun 10."

else: # Si no hi ha cap 10...
    print ("No hi ha cap 10") # Imprimirà que "no hi ha cap 10."

#FINALITZAR EL PROGRAMA
quit() # Finalitzem el programa