""" 60%
    80% com Memoization

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""

def verifica_palavra(palavra, frase):
    for i in range(len(palavra)):
        if i >= len(frase) or palavra[i] != frase[i]:
            return -1
    return 1

def espaca(frase, palavras):
    maior_frase = ""
    for palavra in palavras:
        if verifica_palavra(palavra, frase) == 1:
            nova_frase = frase[len(palavra):]  #remove se a palavra já analisada
            if nova_frase == "":
                frase_atual = palavra
            else:
                frase_atual = palavra + " " + espaca(nova_frase, palavras)
            
            if len(frase_atual) > len(maior_frase):
                maior_frase = frase_atual

    return maior_frase


def main():
    print("<h3>espaca</h3>")
    palavras = ["e", "o", "so", "maior", "este", "curso", "urso", "es", "maio"]
    print("in:", "estecursoeomaior", palavras)
    print("out:",espaca("estecursoeomaior", palavras))
    

if __name__ == '__main__':
    main()





#Memoization
"""
def espaca(frase, palavras_validas):
    n = len(frase)
    dp = [""] * (n+1)
    dp[0] = ""
    for i in range(n):
        for palavra in palavras_validas:
            if i + len(palavra) <= n and frase[i:i+len(palavra)] == palavra:
                nova_frase = dp[i] + " " + palavra if i > 0 else palavra
                if len(nova_frase) > len(dp[i+len(palavra)]):
                    dp[i+len(palavra)] = nova_frase
    return dp[n].strip()
"""