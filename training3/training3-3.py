#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 3.3

#Training 3 - Condicionals

#Exercici 3: Escriu un programa que llegeixi per teclat un nombre i ens digui si és positiu o negatiu (considerem el zero com a positiu).

print ("Escriu un nombre:")

n = float(input())

#CONDICIÓ N POSITIU
if n >= 0:
    print (f"El nombre {int(n)} és positiu.")

#Si aquí afegeixo un elif, podem establir que si n=18 doni un missatge "felicitats, ja ets major d'edat."

else:
    print (f"El nombre {int(n)} és negatiu.")

#FINALITZAR EL PROGRAMA
quit() 