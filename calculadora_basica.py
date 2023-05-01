#usuario insere 2 valores e um operador '+-/*'
while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite um operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float=float(numero_1)
        num_2_float=float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos valores digitados sao invalidos')
        continue

    operadores_permitidos='+-/*'

    if operador not in operadores_permitidos:
            print('Operador invalido.')

    if len(operador)>1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta confira o resultador abaixo:')

    #logica da calculadora
    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=',num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=',num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=',num_1_float * num_2_float)
    else:
        print('este print nunca deveria acontecer!!')
    
    sair= input('Quer sair? [s]im ').lower().startswith('s')

    if sair is True:
        break



