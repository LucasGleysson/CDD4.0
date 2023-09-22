count_negativo = 0
soma = 0
for i in range(10):
    num = int(input('Digite um número: '))
    if num < 0:
        count_negativo += 1
        soma += num
        print(f'{num} é um numero NEGATIVO')

count_positivo = 10 - count_negativo
print(f'Quantidade de números POSITIVOS: {count_positivo}')
print(f'Quantidade de números NEGATIVOS: {count_negativo}')
print(f'A soma de todos os números NEGATIVOS digitados é: {soma}')
