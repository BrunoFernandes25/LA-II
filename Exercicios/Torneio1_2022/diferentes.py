"""
    Essa função recebe uma lista de strings "frases" e retorna uma lista ordenada dessas strings, em ordem decrescente 
    de quantidade de caracteres diferentes presentes em cada uma delas. Caso haja empate na quantidade de 
    caracteres diferentes, a ordenação é feita em ordem crescente de ordem alfabética.
"""

# em caso de termos frases iguais é suposto retornarmos essas mesmas frasaes,logo da maneira que implementei a minha função, 
# apenas irá aparecer uma vez a mesma frase caso seja repetida 
def diferentes(frases):
    #ordenar por ordem decrescente de tamanho -len(letras_difs)
    pals = []

    for frase in frases:
        letras_difs = []
        for letra in frase:
            if letra not in letras_difs:
                letras_difs.append(letra)
        pals.append((frase,len(letras_difs)))
        #pals[frase] = len(letras_difs)
    #tornar dicionario numa lista de tuplos
    #pals = list(pals.items())
    pals = sorted(pals, key = lambda x: (-x[1],x[0]))
    palss = [frase[0] for frase in pals]
    return palss



def main():
    frases = ["Olá, tudo bem?","Sim tá tudo bem obrigado!!","Olá, tudo bem?","Olá, tudo bme??"]
    print(diferentes(frases))
if __name__ == '__main__':
    main()