#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 4.3

#Training 4 - Bucles

#Exercici 3: Escriu un programa que llegeixi 10 nombres, quan acabi ha d'indicar si "hi havia almenys un nombre negatiu" o "no hi ha cap nombre negatiu".

print ("Introdueix deu nombres. Quan acabis et diré quants d'ells eren negatius.")

#CREACIÓ VARIABLES NECESSARIES:

nombre = int(input()) #Declarem la variable nombre per guardar l'input de l'usuari.

negatiu = False #Declarem una variable negatiu False per defecte, servirà per comprovar si hi ha inputs negatius.

#BUCLE:

for i in range (9): #Per 9 cops (el 10è és el que hi ha fora del bucle), es repetirà el següent:
    
    nombre = int(input()) #Demana input a l'usuari i el casteja a un nombre per poder fer comparacions numèriques.

    if nombre < 0: #Si nombre és menor a zero (per tant negatiu)...
        negatiu = True #... canviem el valor de la variable booleana (de comprovació) a True.

#ESTABLIR L'OUTPUT:

if negatiu == True: #Si la variable negatiu canvia a True...
    print ("Hi havia almenys un nombre negatiu.") # ...imprimim que "hi havia almenys un nombre negatiu."

else: #Si no, (negatiu = false) ...
    print ("No hi ha cap nombre negatiu.") # ...imprimim que "no hi ha cap nombre negatiu."

#FINALITZAR EL PROGRAMA

quit() #Finalitzem el programa.