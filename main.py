from funciones import * 

matriz = inicializar_matriz() # Generamos la matriz qu se mostrara por consola
print("¡Bienvenidos a Batalla Naval!" + "\n" + "\n")
print(mostrar_tablero(matriz)) # La mostramos por pantalla

matriz_computadora = inicializar_matriz_computadora()
matriz_jugador = solicitar_barcos()

print('\n', "Tablero del Jugador: ", '\n')
print(mostrar_tablero(matriz_jugador), '\n')
print("Tablero de la Computadora: ", '\n')
print(mostrar_tablero(matriz))

contador_jugador = 0
contador_computadora = 0
while contador_jugador < 12 and contador_computadora < 12: # 12 = Numero de aciertos para ganar
    contador_jugador = ataque_jugador(matriz, matriz_computadora, contador_jugador)
    contador_computadora = ataque_computadora(matriz_jugador, contador_computadora)
print("Termino El Juego")
