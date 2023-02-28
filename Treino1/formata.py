"""  0%  

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.
"""

def formata(codigo):
    cod = []
    identacao = 0
    #codigo = codigo.replace("  ", "")
    codigo = " ".join(codigo.split())
    codigo= codigo.replace("; ",";")
    for atual, seguinte in zip(codigo, codigo[1:]):
        if atual == "{":
            identacao += 2
            cod.append(atual + "\n" + identacao*" ")
        elif atual == ";" and seguinte != "}":
            cod.append(atual + "\n" + identacao*" ")
        elif atual == ";" and seguinte == "}":
            identacao -= 2
            cod.append(atual + "\n" + identacao*" " + seguinte)
        elif atual == "}":
            identacao -= 2
            cod.append("\n" + identacao*" " + atual)
        else:
            cod.append(atual)
    cod.append("}")
    cod = ''.join(cod[0:-1])
    return cod
    

def main():
    print("<h4>formata</h4>")
    codigo = "int main() {int x;x=0;     x=x+1;}"
    print(formata(codigo))

if __name__ == '__main__':
    main()


"""
Deveria retornar isto penso eu, contudo falha o 1º teste com o assert na ultima linha do ficheiro 
int main() {
    int x;
    x=0;
    x = x+1;
}

"""

'int x;\nx=0;\nx=x+1}' != 'int x;\nx=0;\nx=x+1;'

'int main() {\n  int x;\n  x=0;\n  x=x+1;\n' != 'int main() {\n  int x;\n  x=0;\n  x=x+1;\n}'
