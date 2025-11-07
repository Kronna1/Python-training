#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 4.1

#Training 4 - Bucles

#Exercici 1: Realitza un programa que mostri tots els nombres parells que hi ha entre 1 i 200. 

print("Aquests són els nombres parells presents entre 1 i 200.")

i = 0 #Creem una variable numèrica per a després poder incrementar-li el valor amb cada iteració.

#BUCLE:

while i < 200: #Mentre i sigui inferior a 200, s'executarà això:

    i+=1 #Incrementarem el valor d'i a cada interació (repetició del loop).

    residu = i % 2 #Això és una operació matemàtica amb output 1,2,3,4... 
    
    # ^Declarem variable residu per després realitzar una comprovació sobre el valor^

    if residu == 0: #Aquí es requereix una condició lògica (comparació), no puc ubicar directament % aquí.
        print (f"{i} és parell.") # Si el residu té valor 0, imprimirà "nº i és parell".

#FINALITZAR EL PROGRAMA

quit() #Finalitzem el programa