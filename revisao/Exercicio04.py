maior = 0
for i in range(3):
    num = int(input('Digite um número: '))
    if i == 0:
        maior = num
    elif num > maior:
        maior = num

print(f'O maior número é {maior}')

