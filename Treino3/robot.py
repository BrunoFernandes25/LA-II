"""  100% -> COPIADA

Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partida num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.

"""


# Memoization

def prob_aux(passos, x, y, probs, cache):
    if passos == 0:
        if (x,y) == (0,0):
            return 1
        else:
            return 0
    if (passos,x,y) in cache:
        return cache[(passos,x,y)]
    u = probs['U'] * prob_aux(passos-1, x, y+1, probs, cache)
    d = probs['D'] * prob_aux(passos-1, x, y-1, probs, cache)
    l = probs['L'] * prob_aux(passos-1, x-1, y, probs, cache)
    r = probs['R'] * prob_aux(passos-1, x+1, y, probs, cache)
    cache[(passos,x,y)] = u+d+l+r
    return cache[(passos,x,y)]

def probabilidade(passos,probs):
    if passos % 2 == 0:
        return round(prob_aux(passos, 0, 0, probs, {}),2)
    else:
        return 0.0


def main():
    print("<h3>probabilidade</h3>")
    probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
    print("in:",6,probs)
    print("out:",probabilidade(2,probs))

    
if __name__ == '__main__':
    main()