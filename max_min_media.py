#varredura 0 a 10 e determina max min e media
maior=-999
menor=999
soma=0
for n in range(1,11):
    valor=int(input("informe um valor:"))
    if valor>0:
        if valor>maior:
            maior=valor
            if valor<menor:
                menor=valor
            soma=soma+valor
        else:
            valor=int(input("informe um valor:"))
media=soma/10
print("o maior valor e {0}".format(maior))
print("o menor valor e {0}".format(menor))
print("o media valor e {0}".format(media))


