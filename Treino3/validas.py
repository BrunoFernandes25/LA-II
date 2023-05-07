"""  90 %

Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""

def verifica_somas(lista,soma):
    for i_num in range(0,len(lista)):
        if lista[i_num] == soma:
            return 1
        for j_num in range(i_num+1,len(lista)):   # verificar a soma com cada numero a frente da lista
            #if soma_nums == soma:       
            if lista[i_num] + lista[j_num] == soma:
                return 1
        res = lista[i_num]
        for k_num in range(i_num+1,len(lista)): #verificar a soma de cada subsequencia
            res = res + lista[k_num]
            if res == soma:
                return 1
    
    return -1
    


def validas(soma,listas):
    res = []
    for lista in listas:
        if verifica_somas(lista,soma) == 1:
            res.append(lista)
        
    return res


def main():
    print("<h3>validas</h3>")
    listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
    print("in:",10,listas)
    print("out:",validas(10,listas))

if __name__ == '__main__':
    main()