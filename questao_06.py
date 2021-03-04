# Questao 06

n = int(input("Tabuada de: "))
inicio = int(input("Informe o inicio da tabuada: "))
fim = int(input("Informe o fim da tabuada: "))


while inicio <= fim:
    print("%.d x %.d = %.d" % (n, inicio, n*inicio))
    inicio+=1