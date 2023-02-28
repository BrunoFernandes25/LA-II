"""  100%

Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.

"""

def apelidos(nomes):
    #ordenar por apelidos e verificar numero de apelidos pelo numero de espaços entre nomes
    lista = []
    nomes.sort()
    for nome in nomes:
        apelidos = nome.split()
        lista.append((nome,len(apelidos)))
    lista.sort(key = lambda x: x[1])
    #print(lista)  
    #devolver lista apenas com tuplos na posicao 0
    lista = [x[0] for x in lista]
    return lista


def apelidos2(nomes):
    l = [] #lista vazia iniciada 
    for i in nomes:
        l.append((i,i.count(" ")))          ##funcao que conta os espaços de cada palavra(tendo assim o nºde apelidos), juntando o nº de apelidos
    l.sort(key = lambda x: x[0])            ## precisamos agora de ordenar os apelidos
    l.sort(key = lambda x: x[1])            ## e ainda ordenar o nº de apelidos
    return list(map(lambda x: x[0],l))      ##agora temos de retornar a lista com os nomes devidamente ordenados de acordo com o nª de apelidos,
                                            ## logo fui a cada (Nome,nºapelido) e peguei apenas nos nomes (x[0]), na lista l atraves do map e listei esses nomes


def main():
    print("<h3>apelidos</h3>")
    nomes = ["Jose Carlos Bacelar Almeida",
             "Maria Joao Frade",
             "Jose Bernardo Barros",
             "Jorge Manuel Matos Sousa Pinto",
             "Manuel Alcino Pereira Cunha",
             "Xico Esperto"]
    print("in:",nomes)
    print("out:",apelidos(nomes))

if __name__ == '__main__':
    main()