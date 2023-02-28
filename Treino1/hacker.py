"""  60%

Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""
def junta(num1,num2):
    resultado= ""
    for i in range(len(num2)):
        if(num2[i] != '*'):
            resultado += num2[i]
        else:
            resultado += num1[i]
    return resultado

    
def hacker(log):
    """Reconstrói os cartões de crédito a partir do log de transações."""
    # Cria um dicionário em que as chaves são os emails e os valores são listas de números de cartão de crédito.
    numeros = {}
    for num, mail in log:
        if mail not in numeros:
            numeros[mail] = [num]
        else:
            numeros[mail].append(num)

    # Reconstrói os cartões de crédito para cada email.
    resultado = []
    for email in numeros:
        # Ordena a lista de números de cartão de crédito com base na quantidade de dígitos visíveis em cada número e no email.
        numeros[email].sort(key=lambda num: (num.count('*')))

        # Comparamos o primeiro numero de cartão com os seguintes até obter o resultado final.
        num_cartao = numeros[email][0]
        for i in range(1, len(numeros[email])):
            num_cartao = junta(num_cartao, numeros[email][i])

        # Adiciona o número de cartão de crédito reconstruído à lista de cartões.
        resultado.append((num_cartao, email))

    # Ordena a lista de cartões com base na quantidade de dígitos visíveis em cada número e no email.
    resultado.sort(key=lambda x: (x[0].count('*'), x[1]))

    return resultado


def main():
    print("<h3>hacker</h3>")
    log = [("****1234********","maria@mail.pt"),
           ("0000************","ze@gmail.com"),
           ("****1111****3333","ze@gmail.com")]
    print("in:",log)
    print("out:",hacker(log))

if __name__ == '__main__':
    main()


"""
Deverá retornar ("00001111****3333,"ze@gmail.com"),(****1234********","maria@mail.pt")
"""