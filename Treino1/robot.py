'''  100%
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

# se dir = 0 robot está direcionado sobre o eixo do y no sentido positivo
# se dir = 1 robot está direcionado sobre o eixo do x no sentido negativo
# se dir = 2 robot está direcionado sobre o eixo do y no sentido negativo
# se dir = 3 robot está direcionado sobre o eixo do x no sentido positivo



# somar (0,0) + (0,1) = (0, 0, 0, 1) e eu queria obter (0,1)
def robot(comandos):
    posicoes = []
    dir = 0
    #posicao inicial
    pos = [0,0]
    #coordenadas minimas e maximas de x e y
    cords = (0,0,0,0)
    for comando in comandos:
        if comando == "A":
            if dir == 0:
                pos[1] += 1
            elif dir == 1:
                pos[0] += -1
            elif dir == 2:
                pos[1] += -1
            else:
                pos[0] += 1
            #verificamos o minimo ou maximo que temos comparativamente à posicao comparada
            cords = (min(cords[0], pos[0]), min(cords[1], pos[1]), max(cords[2], pos[0]), max(cords[3], pos[1]))
        elif comando == "E":
            dir = (dir + 1) % 4
        elif comando == "D":
            dir = (dir + 3) % 4
        elif comando == "H":
            posicoes.append(cords)
            # damos reset as coordenadas para um novo retangulo que possa aparecer, ou seja, guarda novas posicoes até encontrar um novo H
            dir = 0
            pos = [0,0]
            cords = (0,0,0,0)

    return posicoes
# dá erro mas reconhece que tem 2 retangulos, falta verificar o porque de nao somar
# resultado  [(-9, -2, 0, 2), (0, 0, 0, 3)]


def main():
    print("<h3>robot</h3>")
    cs = "EEAADAAAAAADAAAADDDAAAHAAAH"
    print("in:",cs)
    print("out:",robot(cs))

if __name__ == '__main__':
    main()