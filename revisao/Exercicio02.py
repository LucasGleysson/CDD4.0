finalizar = 'n'
while finalizar != 's':
    num = int(input('Digite um número diferente de zero: '))

    if num == 0:
        print('Valor invalido, tente novamente')
        continue
    if num > 0:
        print(f'{num} é POSITIVO')
    else:
        print(f'{num} é NEGATIVO')

    finalizar = input('Finalizar? (s/n): ')

