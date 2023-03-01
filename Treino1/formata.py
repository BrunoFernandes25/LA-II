"""  60%  

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.
"""

'''def formata(codigo):
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
    return cod'''

#  80%
def formata(codigo):
    cod = []
    identacao = 0
    espacos = False
    for atual,seguinte in zip(codigo,codigo[1:]):
        #casos como "{int x"
        if atual == "{" and seguinte != " ":
            identacao += 2
            cod.append(atual + "\n" + identacao*" ")
        #casos como "int main(){ if"
        elif atual == "{" and seguinte == " ":
            identacao += 2
            cod.append(atual + "\n" + identacao*" ")
            espacos = True
        #casos como ";x=0"
        elif atual == ";" and seguinte not in {" ","}"}: 
            cod.append(atual + "\n" + identacao*" ")
        #casos como ";     x=x+1;"    
        elif atual == ";" and  seguinte == " ":
            cod.append(atual + "\n" + identacao*" ")
            espacos = True
        #casos como "     x=x+1;"
        elif atual == " " and seguinte == " ":
            pass
        #casos como "x=x+1;}"
        elif atual == ";" and seguinte == "}":
            identacao -= 2
            cod.append(atual + "\n" + identacao*" ")
        #espaco  e encontramos uma letra ( como " x=x+1")
        elif atual == " " and seguinte != " " and espacos == True:
            espacos = False
            pass
        #espaco letra nos casos normais, i.e, um espaço como em "int main"
        elif atual == " " and seguinte != " " and espacos == False:
            cod.append(atual)
        #casos como "} else"
        elif atual == "}" and seguinte == " ":
            cod.append(atual + "\n" +identacao*" ")
            espacos = True
        #casos como "else{x+=2;}}"
        elif atual == "}" and seguinte == "}":
            identacao -=2
            cod.append(atual + "\n" + identacao*" ")
        # nos restantes casos como "int", apenas se adiciona a letra à lista cod
        else:
            cod.append(atual)

    #caso o ultimo caracter de codigo seja ";" então adicionamo-lo visto que nao abordamos isso nos if/elses
    if codigo[-1] == ";":
        #cod.append(";")
        cod.append(identacao*" " + ";")
    #no caso de ser "}" identamos e colocamos a respetiva identação seguida do "}"
    else:
        cod.append(identacao*" " + "}")
    cod = ''.join(cod)
    return cod


def main():
    print("<h4>formata</h4>")
    #codigo = "int x;x=0;x=x+1;"
    codigo = "int main() {int x;x=0;     x=x+1;}"
    #codigo= "int main(){ if (x==2){ x+=1;} else{x+=2;}}"
    print(formata(codigo))
if __name__ == '__main__':
    main()

