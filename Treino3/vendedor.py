""" 70 %

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""


# produto -> (nome,valor,peso)

def vendedor(capacidade,produtos):
    res = aux_vendedor(capacidade, produtos)
    res[1].sort()
    return res
    
def aux_vendedor(capacidade, produtos):
    #caso nao existam produtos ou o vendedor nao capacidade na mochila
    if capacidade == 0 or produtos == []:
        return (0,[])
    #caso primeiro produto ultrapasse a capacidade da mochila do vendedor
    if produtos[0][2] > capacidade:
        return aux_vendedor(capacidade, produtos[1:])
    
    # Caso primeiro produto nao ultrapasse a capacidade da mochila, temos 3 caos:
    #
    # manter a mesma capacidade da lista de produtos e remover o primeiro produto da lista de produtos        -> a
    # diminuir a capacidade pelo peso do primeiro produto da lista de produtos  e manter o produto na lista   -> b
    # diminuir a capacidade pelo peso do primeiro produto da lista de produtos e remover o produto da lista   -> c

    a = aux_vendedor(capacidade, produtos[1:])                   
    b = aux_vendedor(capacidade - produtos[0][2], produtos)    
    c = aux_vendedor(capacidade - produtos[0][2], produtos[1:]) 

    # Vendendo o primeiro produto da lista, temos de atualizar b e c
    # b é do tipo (valor máximo que pode ser ganho,lista de produtos vendidos)
    # e c é do mesmo tipo mas de acordo com o caso de c
    b = b[0] + produtos[0][1], b[1] + [produtos[0][0]]
    c = c[0] + produtos[0][1], c[1] + [produtos[0][0]]
    
    # No final temos de averiguar qual o valor maximo desses 3 casos base aplicados a todas as possibilidades
    # Vamos comparar as tuplas a, b e c utilizando como chave de ordenação o valor máximo obtido em cada tupla.
    # O resultado final será a tupla que contém o maior valor máximo. 
    # Caso haja empate, a primeira tupla encontrada no conjunto de empates será retornada.
    return max(c, b, a, key=lambda x: x[0])



def main():
    print("<h3>vendedor</h3>")
    produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
    print("in:",14,produtos)
    print("out:",vendedor(14,produtos))


    
if __name__ == '__main__':
    main()