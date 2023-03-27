''' 80%

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

"""
mapa = ["4563",
        "9254",
        "7234",
        "3231",
        "3881"]

travessia(mapa),(2,10)

"""

def vertices_menores_2(mapa):
    ultima_linha = len(mapa)-1
    dict_grafo = {}
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):

            #comparar elems laterais/horizontais
            if coluna < len(mapa[0]) - 1:
                if abs(int(mapa[linha][coluna]) - int(mapa[linha][coluna+1])) <= 2:
                    if (linha, coluna) not in dict_grafo:
                        dict_grafo[(linha,coluna)] = {}
                    if (linha,coluna+1) not in dict_grafo:
                        dict_grafo[(linha,coluna+1)] = {}
                    dict_grafo[(linha, coluna)][(linha, coluna+1)] = abs(int(mapa[linha][coluna]) - int(mapa[linha][coluna+1])) + 1
                    dict_grafo[(linha, coluna+1)][(linha, coluna)] = abs(int(mapa[linha][coluna]) - int(mapa[linha][coluna+1])) + 1
            # comparar elementos com outros elementos na mesma coluna
            if linha < ultima_linha:
                if abs(int(mapa[linha][coluna]) - int(mapa[linha+1][coluna])) <= 2:
                    if (linha, coluna) not in dict_grafo:
                        dict_grafo[(linha,coluna)] = {}
                    if (linha+1,coluna) not in dict_grafo:
                        dict_grafo[(linha+1,coluna)] = {}
                    dict_grafo[(linha, coluna)][(linha+1, coluna)] = abs(int(mapa[linha][coluna]) - int(mapa[linha+1][coluna])) + 1
                    dict_grafo[(linha+1, coluna)][(linha, coluna)] = abs(int(mapa[linha][coluna]) - int(mapa[linha+1][coluna])) + 1
    #print(dict_grafo)
    return dict_grafo
   
def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
                
    return dist



def travessia(mapa):
    d_2 = vertices_menores_2(mapa)
    start_points = {}
    
    # Encontrar o custo total de percurso para cada ponto de partida na linha mais ao norte
    for col in range(0,len(mapa[0])):
        #se start tem vertices adjacentes, ou seja, se é key de dict_grafo
        start = (0, col)
        # temos de verificar se é possivel começar na linha 0 e no primeiro elemento, caso nao seja temos de ir vendo até ser possivel
        if start in d_2:
            distances = dijkstra(d_2, start)
            #print("Start: ",start)
            for end in distances:
                #print("End ",end)
                if end[0] == len(mapa) - 1:
                    total_cost = distances[end]
                    if start not in start_points or total_cost < start_points[start]:
                        start_points[start] = total_cost
    #ordenar o dicionario de start_points, para caso haja travessias com o mesmo custo ele retornar a mais a oeste(+ à esquerda)
    #print("Start_Points -> ",start_points)
    lista_chaves = []
    for key in start_points.keys():
        #print(key)
        #print(start_points[key])
        lista_chaves.append((key,start_points[key]))
    lista_chaves = sorted(lista_chaves,key=lambda x: (x[0], x[1]))
    #print(lista_chaves)
    # Encontrar o ponto de partida com o menor custo total de percurso
    best_start = min(lista_chaves, key=lambda x: x[1])
    #print(best_start)
    return (best_start[0][1], best_start[1])




def main():
    print("<h3>travessia</h3>")
    mapa = ["4563",
        "9254",
        "7234",
        "3231",
        "3881"]
    """mapa = ["90999",
            "00000",
            "92909",
            "94909"]"""
    print("in:")
    print('\n'.join(mapa))
    print("out:",travessia(mapa))
    
    
if __name__ == '__main__':
    main()