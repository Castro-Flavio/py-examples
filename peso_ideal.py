#calculo peso ideal para m/f
altura=float(input("informe sua altura: "))
sexo= input("informe o sexo m/f: ")
if sexo.lower() == 'm':
    peso_perfeito = (72.7*altura)-58
elif sexo.lower() == 'f':
    peso_perfeito = (62.1*altura)-44.7
else:
    peso_perfeito = 0
    print("Sexo nao reconhecido.")
print("Seu peso ideal e {0:.2f}".format(peso_perfeito))
