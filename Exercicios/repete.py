'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

"""def repete(palavra,n):
    repetidos = 0
    sufixo = list(palavra)
    for i in range(1, len(palavra)):
        if palavra[:-i] == palavra[i:]:
            del sufixo[: len(palavra)-i]
            break
    sufixo = "".join(sufixo)
    result = palavra*(n>0)  + sufixo*(n-1)
    return result
"""

"""def repete(frase,n):
    pal = []
    pal2 = []
    for letra in frase:
        pal.append(letra)
        pal2.append(letra)
    print(pal)
    print()
    tam = len(pal)
    i = 0
    for reps in range(1,n):
        print()
        print(reps)
        for i in range(0,tam):
            if pal[i] != pal[len(pal)-1]:
                pal.append(pal[i])
                print(pal)
            else:
                print("'{}' na posicao {} == '{}' na posicao {}".format(pal[i], i, pal[len(pal)-1], len(pal)-1))
                pal.append(pal[i])
    nova_lista = []

    for letra in pal:
        if len(nova_lista) == 0 or letra != nova_lista[-1]:
            nova_lista.append(letra)

    print("nova lista",nova_lista)
    return pal
"""

def repete(palavra,n):
    seq_maxima = 0
    for i in range(1,len(palavra)):
        #verifica as primeiras i palavras com as i ultimas palavras a contar do fim para o inicio
        if palavra[:i] == palavra[-i:]:
            seq_maxima = i
    final = palavra
    final += (n-1) * palavra[seq_maxima:]
    
    if n != 0:
        return final
    else:
        return ''


def main():

    print(repete("aba",3))
if __name__ == '__main__':
    main()