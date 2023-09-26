soma = 0

for x in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 1:
        soma += num

print(f'A soma dos números ímpares é {soma}')
