'''  100%

Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    freq = {}
    texto = texto.split()
    #print(texto)
    for pal in texto:
        if pal not in freq:
            freq[pal] = 1
        else:
            freq[pal] += 1            
    
    freq_sorted = sorted(freq.items(), key = lambda x: (-x[1],x[0])) 
    freq_words = [word[0] for word in freq_sorted]
    return freq_words


def main():
    print("<h3>frequencia</h3>")
    texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    print("in:",texto)
    print("out:",frequencia(texto))

if __name__ == '__main__':
    main()