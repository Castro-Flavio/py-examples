#teste valor par/impar e positivo/negativo
numero= int(input("informe um valor inteiro: "))
if numero%2==0:
    if numero>0:
        print("o valor {0} e par e positivo".format(numero))
    else:
        print("o valor {0} e par e negativo ".format(numero))
else:
    if numero>0:
        print("o valor {0} e impar e positivo".format(numero))
    else:
        print("o valor {0} e impar e negativo".format(numero))
