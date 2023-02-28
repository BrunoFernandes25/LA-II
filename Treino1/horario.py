"""  80%

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. 
A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respectivo número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.
"""
def aluno_Horas(horario):
    result = []
    for aluno, aulas in horario.items():
        total = sum(aula[2] for aula in aulas)
        result.append((aluno,total))
    return result

def verificar_horario(lista):
    chaves_remover = set()  # cria um conjunto para armazenar as chaves a remover
    for chave, valores in lista.items():
        i = 0
        while i < len(valores):
            dia1, hora1, duracao1 = valores[i]
            j = i+1
            while j < len(valores):
                dia2, hora2, duracao2 = valores[j]
                if dia1 == dia2:
                    if hora1 + duracao1 > hora2:
                        # adiciona a chave a remover ao conjunto
                        chaves_remover.add(chave)
                        break  # sai do loop interno, pois a chave será removida
                    else:
                        j += 1
                else:
                    j += 1
            i += 1
    for chave in chaves_remover:
        del lista[chave]  # remove a chave e seus valores do dicionário
    return lista

def horario(ucs,alunos):
    #horario = [(num1,horas1),(num2,horas2),...]
    horario = {}
    alunos_para_remover = [] #alunos com cadeiras que nao existem no dicionario ucs
    for aluno in alunos:
        horario[aluno] = []
        for disciplina in alunos[aluno]:
            if disciplina in ucs.keys():
                horario[aluno].append(ucs[disciplina])
            else:
                alunos_para_remover.append(aluno) # adiciona o aluno a remover caso contenha cadeiras que nao pertencam a ucs
    
    # remove os alunos do dicionário horario
    for aluno in alunos_para_remover:
        horario.pop(aluno)
                
    #verificar se dias da semana(1 cenas do triplo) sao todos diferentes, caso sejam adicionar a lista final
    #caso existam dias iguais verificar se a hora do dia mais baixa com a soma total da aula nao ultrapassa
    # o inicio da outra aula, caso contrario nao serve e nao se adiciona
    
    #ordenar horario de cada aluno por dia e hora
    horario = {aluno: sorted(disciplinas, key=lambda x: (x[0], x[1])) for aluno, disciplinas in horario.items()}
    #print("aluno ->",horario)
    h = verificar_horario(horario)
    #print("horario ->",h)
    res = aluno_Horas(horario)
    resultado = sorted(res, key=lambda x: (-x[1], x[0]))
    return resultado


def main():
    print("<h4>horario</h4>")
    ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
    alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
    print(horario(ucs,alunos))

if __name__ == '__main__':
    main()