#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 3.2

#Training 3 - Condicionals

#Exercici 2: Escriu un programa que llegeixi tres nombres diferents i ens digui quin és el major

print ("Escriu un primer nombre:")

n1 = float(input())
#Es podria fer amb un integer, però emprem un float per poder acceptar inputs decimals.

print ("Escriu un segon nombre:")

n2 = float(input())

print ("Escriu un tercer nombre:")

n3 = float(input())

#CONDICIÓ QUIN N ÉS +GRAN
if n1 > n2 and n1 > n3:
    print (f"{int(n1)} és el nombre més gran del conjunt introduït.")

elif n2 > n1 and n2 > n3:
    print (f"{int(n2)} és el nombre més gran del conjunt introduït.")

elif n3 > n1 and n3 > n2:
    print (f"{int(n3)} és el nombre més gran del conjunt introduït.")

else:
    print ("Dos dels nombres introduïts tenen el mateix valor.")

#FINALITZAR EL PROGRAMA
quit()

