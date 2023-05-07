""" 90% 

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""


def crescente(lista):
    n = len(lista)
    arr = []
    tam = 1
    if len(lista) == 0:
        tam = 0
        return tam
    elif len(lista) == 1:
        tam = 1
        return tam
    else:
        for i in range(n):
            tam = 1
            atual = lista[i]
            for j in range(i+1,n):
                prox = lista[j]
                #print(atual)
                #print(prox)
                #print()
                if(prox>=atual): # com >= dá 80%
                    tam +=1
                    atual = prox
            arr.append(tam)
        #print(arr)
    return max(arr)


def main():
    print("<h3>crescente</h3>")
    lista = [3] 
    print("in:",lista)
    print("out:",crescente(lista))
    
    
if __name__ == '__main__':
    main()