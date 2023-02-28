"""  100%

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""
# prefs = {10000:[1,2],10885:[1,5],40000:[5]}


def aloca(prefs):
    alunos_com_projs = {} # {proj : Aluno,...}
    lista_Alunos_Sem_Projeto = []
    for aluno in sorted(prefs.keys()): #garantimos a ordenação pelo número de aluno
        # vamos atribui o primeiro projeto a cada aluno, 
        # caso esse projeto já se encontre atribuido entao atribui se a proxima preferencia, se nao existir entao vai para lista de alunos sem projeto
        for proj in prefs[aluno]:
            if proj not in alunos_com_projs:
                alunos_com_projs[proj] = aluno
                break
        else:
            lista_Alunos_Sem_Projeto.append(aluno)
    print(alunos_com_projs)
    return lista_Alunos_Sem_Projeto

def aloca2(prefs):
    alunos_com_projs = {}
    lista_Alunos_Sem_Projeto = []
    projs_atribuidos = []
    for aluno in sorted(prefs.keys()):
        alocado = False
        for proj in prefs[aluno]:
            if proj not in projs_atribuidos:
                alunos_com_projs[proj] = aluno
                projs_atribuidos.append(proj)
                alocado = True
                break # termina este ciclo for interno
        if not alocado:
            lista_Alunos_Sem_Projeto.append(aluno)
    return lista_Alunos_Sem_Projeto



def main():
    #       {Aluno:[projs],...}
    prefs = {10885:[1,5],40000:[5],10000:[1,2]}
    print("in:",prefs)
    print("out:",aloca2(prefs))

if __name__ == '__main__':
    main()