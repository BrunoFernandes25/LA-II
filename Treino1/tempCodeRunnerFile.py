def formata(codigo):
    cod = []
    identacao = 0
    for atual,seguinte in zip(codigo,codigo[1:]):
        if atual == "{":
            identacao += 2
            cod.append(atual + "\n" + identacao*" ")
        elif atual == ";" and seguinte not in {" ","}"}: 
            cod.append(atual + "\n" + identacao*" ")
        elif atual == ";" and  seguinte == " ":
            cod.append(atual + "\n" + identacao*" ")
        elif atual == " " and seguinte == " ":
            pass
        elif atual == ";" and seguinte == "}":
            identacao -= 2
            cod.append(atual + "\n" + seguinte)
        else:
            cod.append(atual)
    cod = ''.join(cod[0:])
    #print(cod)
    return cod