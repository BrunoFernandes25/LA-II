"""
Implemente uma função que, dada uma lista com registos de instantes de tempo e nome de piloto, 
descrevendo os tempos de passagem pela meta dos varios pilotos numa corrida de F1, 
devolva a lista com os nomes dos pilotos com a volta mais rápida ordenada por ordem alfabética. 
Assuma que todos os pilotos iniciaram a prova no instante 0.
"""


def formula1(lista):
    pilotos = {}
    volta_rapida = []
    pilotos_mais_rapidos = []
    if len(lista) == 0:
        return pilotos_mais_rapidos
    
    for volta in lista:
        if volta[1] not in pilotos:
            pilotos[volta[1]] = [volta[0]]
        else:
           pilotos[volta[1]].append(volta[0]) 
    
    #suponho que os tempos já vem ordenados visto ser uma corrida 
    for piloto,tempos in pilotos.items():
        voltamin = float('inf')
        for x,y in zip(tempos,tempos[1:]):
            tempo = abs(x-y)
            #print(tempo)
            if(tempo < voltamin):
                voltamin = tempo
        volta_rapida.append((piloto,voltamin))

    # Ordenar os pilotos de acordo com o nome
    volta_rapida = sorted(volta_rapida, key= lambda x: (x[1],x[0]))
    #print(volta_rapida)
    # Encontrar os pilotos com a volta mais rápida
    tempo_minimo = min(volta_rapida, key=lambda x: x[1]) # devolve (piloto,volta) e nós queremos apenas a volta logo tempo_minimo[1]
    # pilotos_minimos = [piloto for piloto, tempo in volta_rapida if tempo == tempo_minimo]
    for voltas in volta_rapida:
        #print(voltas[0])
        if voltas[1] == tempo_minimo[1]:
            pilotos_mais_rapidos.append(voltas[0])
    #print("Pilotos com a volta mais rapida:", pilotos_minimos)
    return pilotos_mais_rapidos


def main():
    #lista = [(0, "Russel"),(0, "Hamilton"),(0, "Tsunoda"),(0, "Gasly"),(0, "Verstappen"),(30, "Russel"), (80,"Hamilton"), (120, "Tsunoda"), (100, "Gasly"), (50, "Verstappen"),(130,"Hamilton"),(120,"Verstappen"),(170,"Gasly"),(240,"Gasly"),(170,"Hamilton")]
    lista = [(0, "Russel"),(0, "Hamilton"),(0, "Tsunoda"),(0, "Gasly"),(0, "Verstappen"), (80,"Hamilton"),(50,"Russel"), (120, "Tsunoda"), (100, "Gasly"), (50, "Verstappen"),(130,"Hamilton"),(120,"Verstappen"),(170,"Gasly")]
    #lista = []
    print(formula1(lista))
if __name__ == '__main__':
    main()