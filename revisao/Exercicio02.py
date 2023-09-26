num = int(input('Digite um número diferente de zero: '))

while num == 0:
    print('Valor invalido, tente novamente')

    num = int(input('Digite um número diferente de zero: '))

if num > 0:
    print(f'{num} é POSITIVO')
else:
    print(f'{num} é NEGATIVO')

