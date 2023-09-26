count = 0
soma = 0

while count < 10:
    num = int(input('Digite um número: '))
    soma += num
    count += 1

media = soma / 10
print(f'Soma dos numeros: {soma}')
print(f'Média: {media}')
