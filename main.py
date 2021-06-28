import random
import time

def noche_de_apuestas(fichas, prob_ganar, max_juegos):
    """
        Función que simula todas las apuestas de una noche.

        Entradas:
            fichas -> cantidad de fichas inicial que tiene el apostador
            prob_ganar -> probabilidad de ganar
            max_juegos -> número máximo de juegos en una noche
        
        Salidas:
            Diccionario con claves:
                Num fichas -> almacena la cantidad de fichas que tiene al final de la noche
                Num juegos -> almacena la cantidad de juegos que se hicieron en la noche
    """

    contador_juegos = 0                         #cuenta la cantidad de veces que se jugó
    while fichas > 0 and contador_juegos < max_juegos:
        resultado = random.choices([0,1], weights=[1-prob_ganar, prob_ganar])   #resultado de la apuesta
       
        if resultado[0]:
            fichas += 1
        else:
            fichas -= 1

        #print(f"Apuesta N°: {contador_juegos + 1}, tengo {fichas} fichas")
        contador_juegos += 1

    return {"Num fichas" : fichas, "Num juegos" : contador_juegos}  #devuelve diccionario con resultados



#comienzo de programa principal

media_apuestas = 0

for i in range(20):
    t_start = time.time()               #para medir el tiempo que tarda en ejecutarse
    resultado =  noche_de_apuestas(50, 0.4, 300)        #llamada a la función para simular la noche de apuestas
    t_end = time.time()
    print(f"La simulación tardó {t_end - t_start} segundos")
    media_apuestas += resultado["Num juegos"]
    print(resultado)

media_apuestas /= 20
print(f"La media de la cantidad de apuestas es: {media_apuestas}")