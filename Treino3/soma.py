"""   90% 

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""

def maxsoma(lista):
    resultado = []
    if len(lista) == 0:
        return 0
    
    for i_num in range(0,len(lista)):
        res_atual = lista[i_num]
        resultado.append(res_atual)
        for j_num in range(i_num+1,len(lista)):
            #print("Depois do for res_atual -> ",res_atual)
            #print("Prox elem da lista ->",lista[j_num])
            #print()
            res_atual = res_atual + lista[j_num]
            #print("Somando-> ",res_atual)
            resultado.append(res_atual)


    return max(resultado)



def main():
    print("<h3>maxsoma</h3>")
    lista = [-2,1,-3,4,-1,2,1,-5,4]
    print("in:",lista)
    print("out:",maxsoma(lista))

    
if __name__ == '__main__':
    main()



""" 100%

def maxsoma(lista):
    soma_atual = 0
    soma_maxima = float('-inf')
    
    for num in lista:
        #print(num)
        #print(soma_atual)
        soma_atual = max(num, soma_atual + num)
        #print(num)
        #print(soma_atual)
        #print("soma_atual: ",soma_atual)
        soma_maxima = max(soma_maxima, soma_atual)
        #print("soma_maxima: ",soma_maxima)
        #print()
    return soma_maxima
"""


""" 100%

def maxsoma(lista):
    resultado = [lista[0]]
    print(resultado)
    for i in range(1, len(lista)):
        resultado.append(max(resultado[i-1] + lista[i], lista[i]))
    
    print(resultado)
    return max(resultado)
"""