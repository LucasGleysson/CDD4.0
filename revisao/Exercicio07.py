b = float(input('Digite o valor da base: '))
while b <= 0:
    print('O valor não pode ser MENOR ou IGUAL a ZERO')
    b = float(input('Digite o valor da base: '))

h = float(input('Digite o valor da altura: '))
while h <= 0:
    print('O valor não pode ser MENOR ou IGUAL a ZERO')
    h = float(input('Digite o valor da altura: '))

A = (b * h) / 2
print(f'O valor da área é: {A}')
