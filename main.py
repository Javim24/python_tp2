"""
    Cosas para hacer:
        *crear funcion para simular la noche de apuestas  --> HECHO
        *implementar un loop para simular cada apuesta de la noche --> HECHO
        *simular cada apuesta con un valor aleatorio
        *terminar el loop si se cumplen 300 juegos o se queda sin fichas   --> HECHO
        *devolver cantidad de fichas  y número de juegos        --> HECHO
        *hacer un loop para correr la función 20 veces
        *promediar los resultados
        *medir el tiempo que tarda en simularse cada noche e imprimirlo por pantalla
"""

def noche_de_apuestas(fichas, probabilidad, max_juegos):
    """
        Función que simula todas las apuestas de una noche.

        Entradas:
            fichas -> cantidad de fichas inicial que tiene el apostador
            probabilidad -> probabilidad de ganar
            max_juegos -> número máximo de juegos en una noche
        
        Salidas:
            Diccionario con claves:
                Num fichas -> almacena la cantidad de fichas que tiene al final de la noche
                Num juegos -> almacena la cantidad de juegos que se hicieron en la noche
    """

    contador_juegos = 0
    while fichas > 0 and contador_juegos < max_juegos:
        resultado = 1   #acá iría la parte de random
        if resultado:
            fichas += 1
        else:
            fichas -= 1
        #print(f"Apuesta N°: {contador_juegos}, tengo {fichas} fichas")
        contador_juegos += 1
    return {"Num fichas" : fichas, "Num juegos" : contador_juegos}


resultado =  noche_de_apuestas(50, 0.4, 300)
print(resultado)