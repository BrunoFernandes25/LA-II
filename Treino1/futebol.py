'''  100%

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''

def tabela(jogos):
    tabela = {} # {nome: (pontos,dg), ...}
    #pontos = 0
    #golos = 0
    for jogo in jogos:
        if jogo[0] not in tabela:
            tabela[jogo[0]] = [0,0]
        if jogo[2] not in tabela:
            tabela[jogo[2]] = [0,0]
        if jogo[1]>jogo[3]:
            #soma pontos e dif.golos para a primeira equipa
            tabela[jogo[0]][0] += 3
            tabela[jogo[0]][1] += jogo[1] - jogo[3]
            #soma pontos e dif.golos para a segunda equipa
            tabela[jogo[2]][0] += 0
            tabela[jogo[2]][1] += jogo[3] - jogo[1]
        elif jogo[1]<jogo[3]:
            #soma pontos e dif.golos para a segunda equipa
            tabela[jogo[2]][0] += 3
            tabela[jogo[2]][1] += jogo[3] - jogo[1]
            #soma pontos e dif.golos para a primeira equipa
            tabela[jogo[0]][0] += 0
            tabela[jogo[0]][1] += jogo[1] - jogo[3]
        else:
            #soma pontos e dif.golos para a segunda equipa
            tabela[jogo[2]][0] += 1
            tabela[jogo[2]][1] += jogo[3] - jogo[1]
            #soma pontos e dif.golos para a primeira equipa
            tabela[jogo[0]][0] += 1
            tabela[jogo[0]][1] += jogo[1] - jogo[3]

    #lista com pontos ordem decrescente
    # Em caso de empate neste critério, deve ser usada a diferença de golos, e, se persistir o empate, o nome da equipa.
    
    #print(tabela.items())                     (x[0], x[1][0],x[1][1])
    #[('Benfica', [4, -2]), ('Porto', [4, 2]), ('Sporting', [2, 0])]
    lista = sorted(tabela.items(), key = lambda x: (-x[1][0],-x[1][1],x[0]))
    #tornar lista como uma lista de tuplos com (nome_equipa,pontos)
    tab = list(map(lambda x: (x[0], x[1][0]), lista))
    return tab


def main():
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

if __name__ == '__main__':
    main()


"""def calcular_tabela(jogos):
    tabela = {}
    for jogo in jogos:
        equipa1, golo1, equipa2, golo2 = jogo
        if equipa1 not in tabela:
            tabela[equipa1] = [0, 0, 0, 0] # [pontos, golos marcados, golos sofridos, diferença de golos]
        if equipa2 not in tabela:
            tabela[equipa2] = [0, 0, 0, 0]
        if golo1 > golo2:
            tabela[equipa1][0] += 3 # equipa1 ganhou, recebe 3 pontos
        elif golo2 > golo1:
            tabela[equipa2][0] += 3 # equipa2 ganhou, recebe 3 pontos
        else:
            tabela[equipa1][0] += 1 # empate, cada equipa recebe 1 ponto
            tabela[equipa2][0] += 1
        tabela[equipa1][1] += golo1 # golos marcados por equipa1
        tabela[equipa1][2] += golo2 # golos sofridos por equipa1
        tabela[equipa2][1] += golo2 # golos marcados por equipa2
        tabela[equipa2][2] += golo1 # golos sofridos por equipa2
    # calcular a diferença de golos e adicionar à tabela
    for equipa in tabela:
        tabela[equipa][3] = tabela[equipa][1] - tabela[equipa][2]
    # ordenar a tabela classificativa por pontos, diferença de golos e nome da equipa
    tabela_classificativa = sorted(tabela.items(), key=lambda x: (-x[1][0], -x[1][3], x[0]))
    # converter a lista de tuples em lista de lists para torná-la mutável
    tabela_classificativa = [list(tup) for tup in tabela_classificativa]
    # remover a diferença de golos da tabela (não é necessária para a apresentação final)
    for equipa in tabela_classificativa:
        equipa.pop(1)
    return tabela_classificativa"""