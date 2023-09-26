intervalo = 0

for i in range(10):
    num = int(input('Digite um número: '))
    if 20 >= num >= 10:
        intervalo += 1

contador = 10 - intervalo

print(f'Numeros no intervalo de 10 e 20: {intervalo}')
print(f'Números fora do intervalo: {contador}')
