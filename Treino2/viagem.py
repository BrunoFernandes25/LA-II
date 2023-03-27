'''  100%

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''

rotas = [["Porto",20,"Lisboa"],
         ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
         ["Braga",3,"Famalicao",3,"Porto"],
         ["Viana",4,"Povoa",3,"Porto"],
         ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]]

#Ou seja, entre Porto e Viana temos os seguintes preços: 7€ ou 16€ ou 

def adj(rotas):
    vertices_adj = {}
    for rota in rotas:
        i = 0
        while i<len(rota)-1:
            origem = rota[i]
            preco = rota[i+1]
            destinos = rota[i+2]
            #casos em que nao existe cidade no dicionario
            if origem not in vertices_adj:
                vertices_adj[origem] = {}
            if destinos not in vertices_adj:
                vertices_adj[destinos] = {}
            #existindo adicionamos o valor da viagem
            vertices_adj[origem][destinos]= preco
            vertices_adj[destinos][origem]= preco
            i+=2
    return vertices_adj

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

def viagem(rotas,o,d):
    if(rotas == []):
        return 0

    #funçao que desenha o grafo
    rotas = adj(rotas)
    #print("ROTAS ->",rotas)
    
    #o = Caminha
    #d = Lisboa
    #algoritmo do caminho mais curto partindo de Caminha
    dj = dijkstra(rotas,o)
    #falta obter o preco do caminho mais curto passando lhe o destino pretendido
    return dj[d]
    



def main():
    print("<h3>viagem</h3>")
    rotas = [["Porto",20,"Lisboa"],
             ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
             ["Braga",3,"Famalicao",3,"Porto"],
             ["Viana",4,"Povoa",3,"Porto"],
             ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]
            ]
    print("in: Caminha Lisboa")
    print('\n'.join(map(str,rotas)))
    print("out:",viagem(rotas,"Caminha","Lisboa"))
    
    
if __name__ == '__main__':
    main()