""" 100%

Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.

"""

# "#" -> muro
# "." -> espaço vazio
# numeros -> valores bens abandonados


def saque(mapa):
    #atribui tudo a 0 na primeira linha da matriz/caminho pois inicialmente tá tudo a 0, ainda nao eoncontramos nada
    pesos = [[0] * len(mapa[0]) for i in range(len(mapa))] 
    #linha
    for i in range(len(mapa)):
        #coluna
        for j in range(len(mapa[0])):
            if mapa[i][j] != '#':
                maior = [0, 0]
                if i > 0:
                    maior[0] = pesos[i-1][j]
                if j > 0:
                    maior[1] = pesos[i][j-1] 
                if mapa[i][j] == '.':
                    pesos[i][j] = max(maior)
                else:
                    pesos[i][j] = int(mapa[i][j]) + max(maior)

    return pesos[len(mapa)-1][len(mapa[0]) - 1]



def main():
    print("<h3>saque</h3>")
    mapa = [".3......",
            "........",
            "...5#...",
            "...##...",
            ".....9..",
            "..2.....",
            "..2.....",
            "..2....."]
    print("in:")
    print('\n'.join(mapa))
    print("out:",saque(mapa))

    
if __name__ == '__main__':
    main()
