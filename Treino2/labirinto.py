''' 80%

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''
def desenha_caminho(mapa):
    ultima_linha = len(mapa)-1
    adj = {}
    for linha in range (0,len(mapa)):
        for coluna in range(0,len(mapa[0])):
            #comparar elems laterais/horizontais
            if coluna < len(mapa[0])-1:
                if mapa[linha][coluna] == " " and mapa[linha][coluna+1] == " ":
                    if (linha,coluna) not in adj:
                        adj[(linha,coluna)] = []
                    if (linha,coluna+1) not in adj:
                        adj[(linha,coluna+1)] = []
                    adj[(linha, coluna)].append((linha, coluna+1))
                    adj[(linha, coluna+1)].append((linha, coluna))
            # comparar elementos com outros elementos na mesma coluna
            if linha < ultima_linha:
                if mapa[linha][coluna] == " " and mapa[linha+1][coluna] == " ":
                    if (linha, coluna) not in adj:
                        adj[(linha,coluna)] = []
                    if (linha+1,coluna) not in adj:
                        adj[(linha+1,coluna)] = []
                    adj[(linha, coluna)].append((linha+1, coluna))
                    adj[(linha+1, coluna)].append((linha, coluna))
    #print(adj)
    return adj

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

def caminho_mais_curto(adj,o,d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    print("\nCAMINHO",caminho)
    return caminho
#caminho(build(exemplo),”MAD","NRT")


def caminho(mapa):
    cam = desenha_caminho(mapa)
    print(cam)

    #falta obter o caminho mais curto, irei usar o dijkstra
    cam_min = caminho_mais_curto(cam, (0, 0), (len(mapa)-1 , len(mapa)-1))
    print(cam_min)
    #falta agora associar a string de cordenadas a cada movimento que é feito
    res = ""
    for i in range(len(cam_min)-1):     
        if (cam_min[i][0] <= cam_min[i+1][0]) and (cam_min[i][1] < cam_min[i+1][1]):
            res = res + "E"
        elif (cam_min[i][0] < cam_min[i+1][0]) and (cam_min[i][1] <= cam_min[i+1][1]):
            res = res + "S"
        elif (cam_min[i][0] > cam_min[i+1][0]) and (cam_min[i][1] >= cam_min[i+1][1]):
            res = res + "N"
        else:
            res = res + "O"
    return res



def main():
    print("<h3>caminho</h3>")
    mapa = ["  ########",
            "# # #    #",
            "# # #### #",
            "# #      #",
            "# # # ####",
            "# # #    #",
            "#   # #  #",
            "##### ####",
            "#        #",
            "########  "]
    print("in:")
    print('\n'.join(mapa))
    print("out:",caminho(mapa))

if __name__ == '__main__':
    main()