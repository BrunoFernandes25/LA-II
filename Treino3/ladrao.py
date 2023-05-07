""" 80% Recursivo 
    100% Memoization

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""
#Recursivamente
def ladrao(capacidade,objectos):
    #caso nao existam objetos ou o ladrao nao tenha mochila
    if len(objectos) == 0 or capacidade == 0:
        return 0
    
    #caso primeiro objeto ultrapasse a capacidade da mochila do ladrao
    if objectos[0][2] > capacidade :
        return ladrao(capacidade,objectos[1:])
    
    #caso primeiro objeto nao ultrapasse a capacidade da mochila
    dinheiro_ladrao_com_objeto_x = objectos[0][1] + ladrao(capacidade - objectos[0][2],objectos[1:])
    dinheiro_ladrao_sem_objeto_x = ladrao(capacidade,objectos[1:])
    return max(dinheiro_ladrao_com_objeto_x,dinheiro_ladrao_sem_objeto_x)

#Memoization
def ladrao(capacidade, objetos):
    return max_lucro(capacidade, objetos, {})

def max_lucro(capacidade, objetos, memo):
    if capacidade == 0 or not objetos:
        return 0
    nome, valor, peso = objetos[0]      #exemplo -> ("microondas",30,6)
    if (capacidade, len(objetos)) in memo:
        return memo[(capacidade, len(objetos))]
    if peso > capacidade:
        memo[(capacidade, len(objetos))] = max_lucro(capacidade, objetos[1:], memo)
    else:
        memo[(capacidade, len(objetos))] = max(max_lucro(capacidade, objetos[1:], memo),  valor + max_lucro(capacidade - peso, objetos[1:], memo))

    return memo[(capacidade, len(objetos))]
    

def main():
    print("<h3>ladrao</h3>")
    objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
    print("in:",10,objectos)
    print("out:",ladrao(10,objectos))
    
if __name__ == '__main__':
    main()