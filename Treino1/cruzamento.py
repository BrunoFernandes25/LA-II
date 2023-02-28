'''  80%
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    cruz ={}
    for rua in ruas:
        #verificar se a primeira letra da rua está no dicionario cruz
        if rua[0] not in cruz:
            cruz[rua[0]] = 1
        else:
            cruz[rua[0]] += 1
        #caso a primeira e ultima letra sejam diferentes        
        if rua[0] != rua[-1]:
            #entao vamos verificar se a ultima letra já se encontra no dicionario cruz
            if rua[-1] not in cruz:
                cruz[rua[-1]] = 1
            else:
                cruz[rua[-1]] += 1
    #tornar cruz numa lista de tuplos
    l_cruz = list(cruz.items())
    l_cruz =sorted(l_cruz, key= lambda x: (x[1],x[0]))
    #print(l_cruz)
    # Ordenar a lista de cruzamentos por ordem crescente de criticidade
    # e, para cruzamentos com o mesmo número de ruas, por ordem alfabética.
    # cruzamentos = sorted(cruzamentos, key=lambda x: (x[1], x[0]))
    #l_cruz = sorted() 
    return l_cruz
# [('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)]


def main():
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))

if __name__ == '__main__':
    main()
