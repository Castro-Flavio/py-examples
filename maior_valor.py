#mostra o maior valor das entradas
maior=0
numero= int(input("informe um valor: "))
while numero!=0:
    if numero>maior:
        maior=numero
    numero= int(input("informe um valor: "))
print("o maior numero e : {0}".format(maior))

