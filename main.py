"""
    Cosas para hacer:
        *crear funcion para simular la noche de apuestas  --> HECHO
        *implementar un loop para simular cada apuesta de la noche --> HECHO
        *simular cada apuesta con un valor aleatorio        --> HECHO
        *terminar el loop si se cumplen 300 juegos o se queda sin fichas   --> HECHO
        *devolver cantidad de fichas  y número de juegos        --> HECHO
        *hacer un loop para correr la función 20 veces          --> HECHO   
        *promediar los resultados           --> HECHO
        *medir el tiempo que tarda en simularse cada noche e imprimirlo por pantalla
"""
import random

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

    contador_juegos = 0
    while fichas > 0 and contador_juegos < max_juegos:
        resultado = random.choices([0,1], weights=[1-prob_ganar, prob_ganar])
        if resultado[0]:
            fichas += 1
        else:
            fichas -= 1
        #print(f"Apuesta N°: {contador_juegos + 1}, tengo {fichas} fichas")
        contador_juegos += 1
    return {"Num fichas" : fichas, "Num juegos" : contador_juegos}

media_apuestas = 0
for i in range(20):
    resultado =  noche_de_apuestas(50, 0.4, 300)
    media_apuestas += resultado["Num juegos"]
    print(resultado)
media_apuestas /= 20
print(f"La media de la cantidad de apuestas es: {media_apuestas}")