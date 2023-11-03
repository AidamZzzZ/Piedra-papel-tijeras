#se importa la libreria
import random

#se usa un bucle while inicializado con True
while True:
    #se le pide al usuario las acciones a realizar
    user_action = input("Ingrese piedra,papel o tijeras: ")
    
    #se guardan las posibles acciones
    possibles_action = ["piedra","papel","tijeras"]
    
    #se incorporan en una variable la cual sera la que seleccione cualquiera de forma aleatoria
    computer_action = random.choice(possibles_action)
    
    #comienza especificando que acciones escogieron el usuario y la computadora
    print(f"\nTu elegiste: {user_action} la computadora eligio: {computer_action}. \n")
    
    #se pone un condicional el cual indica si uno es igual al otro
    if user_action == computer_action:
        
        #entonces pasaria esto si son iguales
        print(f"Ambos jugadores seleccionaron: {user_action} es un empate.")
        
    #si usuario escribe piedra y la computadora tijeras
    elif user_action == "piedra":
        if computer_action == "tijeras":
            #se imprime este mensaje
            print("La piedra destroza a la tijera! ganaste.")
        #sino muestra
        else:
            #lo contrario,pero con papel
            print("El papel cubre a la piedra, perdiste.")
            
    #si usuario escribe papel y la computadora piedra pasa lo mismo que lo anterior pero mostrando que gano(en este caso a la inversa)
    elif user_action == "papel":
        if computer_action == "piedra":
            #se imprime este mensaje
            print("El papel cubre a la piedra!, tu ganas.")
        else:
            #si no dice que la tijera corta el papel (siguiendo con la otra linea de codigo)
            print("La tijera corta el papel, tu pierdes.")
    
    #si el usuario escribe tijera y la computadora papel
    elif user_action == "tijeras":
        if computer_action == "papel":
            #se muestra eset mensaje
            print("La tijera corta el papel!, tu ganas.")
        else:
            #sino muestra esto,del bloque de codigo anterior
            print("La piedra destroza a la tijera, tu pierdes")
            
    #se pide al usuario si quiere jugar otra vez dando dos opciones si escoge que si,se repite el bucle,sino,se cierra
    jugar_otras_vez = input("Quiere jugar otra ve? [si/no]: ")
    
    #si el usuario pone algun caracter en mayuscula con el lower lo transformara a minuscula para poder asimilarlo con el "si" y continuar el juego las veces q quiera
    if jugar_otras_vez.lower() != "si":
        
        #si el usuario escribe un no o cualquier otro caracter,este se finaliza por completo
        break
            

