"""  60%  

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.
"""

def formata(codigo):
    cod = []
    identacao = 0
    espacos = False
    for atual,seguinte in zip(codigo,codigo[1:]):
        if atual == "{":
            identacao += 2
            cod.append(atual + "\n" + identacao*" ")
        elif atual == ";" and seguinte not in {" ","}"}: 
            cod.append(atual + "\n" + identacao*" ")
        elif atual == ";" and  seguinte == " ":
            cod.append(atual + "\n" + identacao*" ")
            espacos = True
        elif atual == " " and seguinte == " ":
            pass
        elif atual == ";" and seguinte == "}":
            identacao -= 2
            cod.append(atual + "\n" + seguinte)
        elif atual == " " and seguinte != " " and espacos == True:
            espacos = False
            pass
        elif atual == " " and seguinte != " " and espacos == False:
            cod.append(atual)
        else:
            cod.append(atual)

    if codigo[-1] == ";":
        cod.append(";")

    cod = ''.join(cod[0:])
    #print(cod)
    return cod

def main():
    print("<h4>formata</h4>")
    codigo = "int main() {int x;x=0;     x=x+1;}"
    print(formata(codigo))
if __name__ == '__main__':
    main()

