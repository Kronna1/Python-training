#Alexandra Aixendri, SMX2B, Ins Montsià, PYTHON TRAINING 4.3

#Training 5 - Funcions

#1. Refactorització d'Exercicis a Funcions

#Per a cadascun dels exercicis que heu completat (p. ex., càlcul àrea):

#Tota la lògica d'aquest exercici s'ha d'encapsular dins d'una funció amb un nom descriptiu (p. ex., def calcul_area():).

#Aquestes funcions han de contenir tot el codi necessari per a l'exercici (inclosos els input i print).

#Si és necessari feu ús de paràmetres a les funcions.

#DEFINICIÓ DE FUNCIONS

from time import sleep# la llibreria "time", que conté la funció / mètode de Python sleep().

def HelloWorld ():
    print("Hola món! / Hello world!")
    #quit () - Comentem el quit() perque aquest tanca Python i no permet que s'executi el loop.

def CalculArea ():
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
    #quit ()

def Calculadora ():
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
    #quit ()

def ConcatenarParaules ():
    print("Introdueix la primera paraula:")

    a = input()

    print("Introdueix la segona paraula:")

    b = input()

    print("Introdueix la tercera paraula:")

    c = input()

    #CONCATENAR PARAULES
    d = a + " " + b + " " + c

    print(d)

    #FINALITZAR EL PROGRAMA
    #quit ()

def OperacioDecimal ():
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
    #quit ()

def MajoriaEdat ():
    print ("Introdueix la teva edat")

    edat = int(input())

    #CONDICIÓ MAJORIA D'EDAT
    if edat >=18:
        print("Ets major d'edat.")

    else:
        print("Ets menor d'edat")

    #FINALITZAR EL PROGRAMA
    #quit ()

def NombreMesGran ():

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
    #quit()

def PositiuNegatiu (): 

    print ("Escriu un nombre:")

    n = float(input())

    #CONDICIÓ N POSITIU
    if n >= 0:
        print (f"El nombre {int(n)} és positiu.")

    #Si aquí afegeixo un elif, podem establir que si n=18 doni un missatge "felicitats, ja ets major d'edat."

    else:
        print (f"El nombre {int(n)} és negatiu.")

    #FINALITZAR EL PROGRAMA
    #quit() 

def NombresParells (): 

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

    #quit() #Finalitzem el programa

def NotesAlumnes (): 

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
    #quit() # Finalitzem el programa

def NegatiusConjunt (): 

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

    #quit() #Finalitzem el programa.

#2. Creació del Menú Principal (Main)

#Heu de crear un programa principal que actuï com a llançadora.

#Aquest programa ha d'implementar un bucle principal (p. ex., while (True):) que es mantingui en execució.

#Dins del bucle, el programa ha de:

#Mostrar a l'usuari un menú amb les opcions disponibles (p. ex., "1. Calcul Area", "2. Calcul edad", ..., "S. Sortir").

#Demanar a l'usuari que triï una opció.

#Gestionar la selecció de l'usuari.

while True: #Aquest bucle s'executarà sempre.
        
    print(f"""Tria quina de les següents funcions vols que s'executi:\n

    S-Finalitzar el programa \n\n
           
    1-Python dient Hello World\n\n
           
    2-Calcular l'àrea d'un quadrat\n\n
           
    3-Calculadora bàsica\n\n
           
    4-Concatenar 3 paraules\n\n
           
    5-Calculadora d'operacions decimals\n\n
           
    6-Comprovació majoria d'edat\n\n
           
    7-Entre un conjunt de 3 nº, quin és el més gran?\n\n
           
    8-El nombre introduit és positiu o negatiu?\n\n
           
    9-Nombres parells entre 0 i 200\n\n
           
    10-Hi ha algun 10 entre les notes dels alumnes?\n\n
           
    11-Hi ha algun número negatiu en el conjunt?""")
    tria = input().upper().strip() #Demanem input a l'usuari.
    
    #upper força que l'input de l'usuari sempre sigui amb majúscula. Això evita els problemes per input case sensitive. 
    
    #strip elimina els possibles espais en blanc de l'input, per exemple " 1 " en comptes de "1".

    match tria:

        case "1":

            HelloWorld()

        case "2":

            CalculArea()

        case "3":

            Calculadora()

        case "4":

            ConcatenarParaules()
        
        case "5":

            OperacioDecimal()

        case "6":

            MajoriaEdat()

        case "7":

            NombreMesGran()

        case "8":

            PositiuNegatiu()

        case "9":

            NombresParells()

        case "10":

            NotesAlumnes()

        case "11":

            NegatiusConjunt()

        case "S":

            print ("Has escollit l'opció de sortida del programa. A continuació es tancarà.")
            break #Trenquem el bucle, ara executarà el que hi hagi després de while.
            
        case _: #Si l'input no correspon amb cap de les altres opcions definides en el matchcase...
            print("L'opció introduïda no és vàlida.")
    
    sleep(3)  #Temps d'espera per reiniciar el loop.

quit() # Si es produeix un break, s'executara quit per tancar el programa.

#3. Control de Flux del Menú

#Si l'usuari tria una opció d'exercici (p. ex., '1'), el programa ha de cridar la funció corresponent (p. ex., executar_calculadora()). Un cop acabi la funció, el programa ha de tornar al menú.

#Si l'usuari tria l'opció de 'S' (Sortir), el bucle principal s'ha de trencar (p. ex., amb break) i el programa ha de finalitzar amb un missatge de comiat.

#Si l'usuari tria una opció no vàlida, el programa li ha de notificar l'error i tornar a mostrar el menú (p. ex., amb continue o simplement deixant que el bucle es repeteixi).