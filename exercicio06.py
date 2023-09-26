numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 == numero2:
    print('Os numeros são iguais: ', end='')

else:
    if numero1 < numero2:
        print(numero1, numero2)

    else:
        print(numero2, numero1)
