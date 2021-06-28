



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
        print(f"Apuesta N°: {contador_juegos}, tengo {fichas} fichas")
        contador_juegos += 1
    return {"Num fichas" : fichas, "Num juegos" : contador_juegos}


resultado =  noche_de_apuestas(50, 0.4, 300)
print(resultado)