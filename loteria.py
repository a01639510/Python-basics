import random

cartas_jugador = []
cartas_mesa = []
cartas_repetidas =[]
cartas_correctas= []
cartas =('El gallo', 'El diablo', 'La dama', 'El catrín', 'El paraguas', 'La sirena', 'La escalera', 'La botella', 'El barril', ' El árbol', 'El melón', ' El valiente', ' El gorrito', 'La muerte', 'La pera', 'La bandera', 'El bandolón', 'El violoncello', 'La garza', 'El pájaro', 'La mano', 'La bota', 'La luna', 'El cotorro', 'El borracho', 'El negrito', 'El corazón', 'La sandía', 'El tambor', 'El camarón')
win = False

#esta funcion define las 9 cartas aleatorias que tendra el jugador para acertar
def cartas_del_juego():
    #Le da 9 cartas aleatorias al jugador
    x = 0
    while x < 9:
        num_carta = random.randint(1,30)
        cartas_jugador.append(cartas[num_carta -1 ])
        x = x+1
    print(cartas_jugador)
#valida si el jugador gano o no
def validacion():
    global win
    if len(cartas_correctas) > 8:
        print("\n \n \n \n \n      LOTERÍA! \n\n")
        win = True
    else:
        print("no habian pasado algunas cartas")    
        win = False
#esta funcion realiza el ciclo del juego
def juego():
    #hace la variable win, una variable global y no local
    global win
    while win == False:

        num_carta = random.randint(1,30)
        #validar si la carta ya salio
        if num_carta in cartas_repetidas:
            print("salio repetida")
            
        else:
            #Agrega la carta a la validacion de cartas repetidas, las cartas que han salido y la carta del turno
            cartas_mesa.append(cartas[num_carta -1 ])
            print (cartas[num_carta -1 ])
            cartas_repetidas.append(num_carta)
            carta_turno = (cartas[num_carta -1 ])
            #Valida si la carta esta en el juego del jugador
            if  carta_turno in cartas_jugador:
                cartas_correctas.append(num_carta)

            
        #Input para saber si el jugador piensa que ya gano
        loteria = input("escribe loteria cuando hayas ganado >>>>")
        if loteria == "loteria" or loteria == "Loteria":
        
            validacion()
            loteria = ""      

#ejecuta el codigo
cartas_del_juego()
juego()
    