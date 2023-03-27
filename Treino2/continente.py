'''  80%

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''
#                   [Fronteira]
# vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]

def dfs(adj,o): 
    return dfs_aux(adj,o,set(),{})  

def dfs_aux(adj,o,vis,pai): 
    vis.add(o)                  
    for d in adj[o]:                      
        if d not in vis:            
            pai[d] = o              
            dfs_aux(adj,d,vis,pai)  
    return pai

def adj(paises_vizinhos):
    vertices_adj = {}
    for paises in paises_vizinhos:
        i = 0
        while i < len(paises) - 1:
            origem = paises[i]
            destino = paises[i+1]
            if origem not in vertices_adj:
                vertices_adj[origem] = set()
            if destino not in vertices_adj:
                vertices_adj[destino] = set()
            vertices_adj[origem].add(destino)
            vertices_adj[destino].add(origem)
            i += 1
    return vertices_adj


def maior(vizinhos):
    maior = 0
    # criar o grafo a partir dos vizinhos
    continentes = adj(vizinhos)
    # obter o tamanho do maior continente
    #print("\n\nContinente: ",continentes)
    for pais in continentes:
        d = dfs(continentes,pais)
        if(len(d) + 1 > maior):
            maior = len(d) + 1
    return maior

def main2():
    print("<h3>maior</h3>")
    vizinhos = [["Portugal","Espanha"],["Espanha","Franca"],["Franca","Belgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
    print("in:", vizinhos)
    print("out:", maior(vizinhos))
    #print(adj(vizinhos))

if __name__ == '__main__':
    main2()