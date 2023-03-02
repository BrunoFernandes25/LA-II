'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

"""def factoriza(n):
    soma = 0
    for i in range(2,n+1//2):
        if n == 1:
            break
        if n % i == 0:
            soma += i
            while(n%i == 0):
                n /= i
    return soma
"""

def factoriza(n):
    soma = 0
    divisores = list(range(2, n+1))     #exemplo divisores possiveis de 84 a serem testados sao [2:84]
    divisores.append(1)                 #e caso nenhum divida, sabemos que 1 divide 
    divs_de_n = []
    while n != 1 :
        for div in divisores:
            if n % div == 0:    
                divs_de_n.append(div)
                n = n // div
                break
    print(divs_de_n)
    #retira elems repetidos dos divisores de n
    divs_de_n = list(set(divs_de_n))            
    print(divs_de_n)
    #falta apenas somar e retornar esse valor
    return sum(divs_de_n)




def main():
    print(factoriza(35))
if __name__ == '__main__':
    main()