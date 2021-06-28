



def noche_de_apuestas(fichas, probabilidad, max_juegos):
    """
        Función que simula todas las apuestas de una noche.

        Entradas:
            fichas -> cantidad de fichas inicial que tiene el apostador
            probabilidad -> probabilidad de ganar
            max_juegos -> número máximo de juegos en una noche
        
        Salidas:
            ....
    """
    contador_juegos = 0
    while fichas > 0 and contador_juegos < max_juegos:
        
        print(f"Apostando {contador_juegos} {fichas}")
        fichas -= 1
        contador_juegos += 1


noche_de_apuestas(50, 0.4, 300)