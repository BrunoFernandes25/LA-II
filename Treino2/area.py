''' 80%

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def constroi_mapa(mapa):
    adj = {}
    ultima_linha = len(mapa)-1
    for linha in range(0,len(mapa)):
        for coluna in range(0,len(mapa[0])):
            #o if abaixo permite nos comparar sempre o elem atual com o seguinte
            if coluna < len(mapa[0])-1:
                #comparação horizontal
                if mapa[linha][coluna] == "." and mapa[linha][coluna+1] == ".":
                    if (linha,coluna) not in adj:   
                        adj[(linha,coluna)] = []
                    if (linha,coluna+1) not in adj:   
                        adj[(linha,coluna+1)] = []
                    adj[(linha, coluna)].append((linha, coluna+1))
                    adj[(linha, coluna+1)].append((linha, coluna))
            # comparar com os elementos abaixo(verticalmente)
            if linha < ultima_linha:
                if mapa[linha][coluna] == "." and mapa[linha+1][coluna] == ".":
                    if (linha,coluna) not in adj:   
                        adj[(linha,coluna)] = []
                    if (linha+1,coluna) not in adj:   
                        adj[(linha+1,coluna)] = []
                    adj[(linha, coluna)].append((linha+1, coluna))
                    adj[(linha+1, coluna)].append((linha, coluna))
    return adj

#Travessia em largura
def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai
#bfs(build(exemplo),”MAD")

def area(p,mapa):
    mapaa = constroi_mapa(mapa)
    print(mapaa)

    p = (p[1],p[0]) # sem isto, tinha apenas 60%
    f = bfs(mapaa,p)
    print(f)
    return len(f)+1




def main():
    print("<h3>area</h3>")
    mapa = ["..*..",
            ".*.*.",
            "*...*",
            ".*.*.",
            "..*.."]
    print("in:",(3,2))
    print('\n'.join(mapa))
    print("out:",area((3,2),mapa))

if __name__ == '__main__':
    main()
