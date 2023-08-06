import random

# FUNCION PARA INICIALIZAR MATRICES QUE SERAN MODIFICADAS PARA MOSTRAR POR CONSOLA
def inicializar_matriz():
    matriz = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    return matriz

def inicializar_matriz_computadora():
    matriz = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]

    n = 4
    while n > 0:
        if n == 2 or n == 1:
            m = n + 1
        else:
            m = n
        posicion_barco = random.randint(0, 1)
        fila = random.randint(0, 8 - m)
        columna = random.randint(0, 9 - m)
        
        if posicion_barco == 0:
            for i in range(m):
                if matriz[fila + i][columna] != "X":
                    matriz[fila + i][columna] = "X"
                else:
                    n +=  1    
        else:
            for i in range(m):
                if matriz[fila][columna + i] != "X":  
                    matriz[fila][columna + i] = "X" 
                else:
                    n +=  1  
        n -= 1           
    return matriz  

# FUNCION PARA MOSTRAR LOS TABLEROS POR CONSOLA
def mostrar_tablero(matriz):
    cadena = ""
    cadena += "  A B C D E F G H I"
    contador = 0
    for fila in matriz:
        cadena += '\n' + str(contador) + " "
        int(contador)
        contador += 1 
        for valor in fila:
            cadena += valor + " "
    return cadena    

# FUNCION PARA HACER EL PROCESO DEL USUARIO PONIENDO SUS BARCOS
def solicitar_barcos():
    matriz_jugador = inicializar_matriz() # INICIALIZAMOS LA MATRIZ DEL USUARIO
    barco1 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 1 (4 celdas):")
    barco1 = separar_coordenadas(barco1)
    while colocar_barco(barco1, matriz_jugador, 4) is None:
        print("Las coordenadas ingresadas no son válidas!!") 
        barco1 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 1 (4 celdas):")
        barco1 = separar_coordenadas(barco1)
    print("Barcos colocados correctamente.")

    barco2 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 2 (3 celdas):")
    barco2 = separar_coordenadas(barco2)
    while colocar_barco(barco2, matriz_jugador, 3) is None:
        print("Las coordenadas ingresadas no son válidas!!") 
        barco2 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 2 (3 celdas):")
        barco2 = separar_coordenadas(barco2)
    

    barco3 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 3 (3 celdas):")
    barco3 = separar_coordenadas(barco3)
    while colocar_barco(barco3, matriz_jugador, 3) is None:
        print("Las coordenadas ingresadas no son válidas!!") 
        barco3 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 3 (3 celdas):")
        barco3 = separar_coordenadas(barco3)
    

    barco4 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 4 (2 celdas):")
    barco4 = separar_coordenadas(barco4)
    while colocar_barco(barco4, matriz_jugador, 2) is None:
        print("Las coordenadas ingresadas no son válidas!!") 
        barco4 = input("Ingrese las coordenadas iniciales y finales para colocar su barco (Ejemplo: A1 A4) '\n' Barco 4 (2 celdas):")
        barco4 = separar_coordenadas(barco4)
    

    return matriz_jugador

# FUNCION PARA SEPARAR COORDENADAS DE LOS BARCOS
def separar_coordenadas(cadena):
    espacio = 0
    coordenadas_separadas = [""]
    for i in range(len(cadena)):
        if cadena[i] == " ":
            espacio += 1
            coordenadas_separadas.append("")
        else:
            coordenadas_separadas[espacio] += cadena[i] 
    return coordenadas_separadas

def colocar_barco(barco, matriz, n_barco):
    caracteres_validos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "0", "1", "2", "3", "4", "5", "6", "7", "8"]
    for i in barco:
        for j in i:
            if j not in caracteres_validos:
                return None
    
    primer_coordenada = barco[0]
    ultima_coordenada = barco[1]
    columna_primer_coordenada = primer_coordenada[0]
    columna_ultima_coordenada = ultima_coordenada[0]
    columna_primer_coordenada = ord(columna_primer_coordenada) - 65
    columna_ultima_coordenada = ord(columna_ultima_coordenada) - 65
    fila_primer_coordenada = int(primer_coordenada[1])
    fila_ultima_coordenada = int(ultima_coordenada[1])
    barco_vertical = False

    if columna_primer_coordenada == columna_ultima_coordenada:
        barco_vertical = True
    if barco_vertical:
        for i in range(n_barco):
            if matriz[fila_primer_coordenada + i][columna_primer_coordenada] != "X" and fila_ultima_coordenada - fila_primer_coordenada == n_barco - 1:
                matriz[fila_primer_coordenada + i][columna_primer_coordenada] = "X"
            else:
                return None    
    else:
        for i in range(n_barco):
            if matriz[fila_primer_coordenada][columna_primer_coordenada + i] != "X" and columna_ultima_coordenada - columna_primer_coordenada == n_barco - 1:  
                matriz[fila_primer_coordenada][columna_primer_coordenada + i] = "X" 
            else:
                return None           
    return matriz  

def ataque_jugador(matriz_visible, matriz_computadora, contador):
    coordenadas_ataque = input("Ingrese las coordenadas para atacar (Ejemplo: A1): ")
    columna_coordenadas = ord(coordenadas_ataque[0]) - 65
    fila_coordenadas = int(coordenadas_ataque[1])
    while coordenadas_ataque[0] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I"] or coordenadas_ataque[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        coordenadas_ataque = input("Coordenadas no validas. Ingrese nuevamente las coordenadas para atacar (Ejemplo: A1): ")
        columna_coordenadas = ord(coordenadas_ataque[0]) - 65
        fila_coordenadas = int(coordenadas_ataque[1])
    if matriz_computadora[fila_coordenadas][columna_coordenadas] == "X":
        matriz_visible[fila_coordenadas][columna_coordenadas] = "X"
        contador += 1
        print("Acertaste! Has impactado en un barco enemigo.")
    else:
        matriz_visible[fila_coordenadas][columna_coordenadas] = "O"
        print("Fallaste! No has impactado en un barco enemigo.")
    print(mostrar_tablero(matriz_visible))
    return contador
