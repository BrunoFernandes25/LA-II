''' 100%

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''
 
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


def constroi_cidade (ruas):
    adj = {}

    for rua in ruas:
        r1 = rua[0]
        r2 = rua[-1]
        if r1 not in adj:
            adj[r1] = {}
        if r2 not in adj:
            adj[r2] = {}
        #caso que testa se já existir uma letra em adj e guarda aquela que tem um caminho menor
        if r2 in adj[r1] and adj[r1][r2] < len(rua):
            continue
        adj[r1][r2] = len(rua)
        adj[r2][r1] = len(rua)

    return adj

def tamanho(ruas):
    cidade = constroi_cidade(ruas)
    print(cidade)

    dist_max = 0
    for rua in cidade:
        distances = dijkstra(cidade, rua)
        # Iterate over the distances, ignoring any that are infinity
        for d in distances.values():
            if d != float("inf"):
                # Update the maximum distance if the current distance is larger
                dist_max = max(dist_max, d)
    print(dist_max)
    
    return dist_max
    




def main():
    print("<h3>tamanho</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:", ruas)
    print("out:", tamanho(ruas))

if __name__ == '__main__':
    main()
