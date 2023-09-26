combustivel = input('Digite qual o combustível (G/E): ')

if combustivel == 'G' or combustivel == 'g':
    litros = float(input('Digite a quantidade de litros: '))
    valor_venda = 5.80 * litros

elif combustivel == 'E' or combustivel == 'e':
    litros = float(input('Digite a quantidade de litros: '))
    valor_venda = 5.80 * litros

else:
    valor_venda = 0
    print('Combustível invalido')

print(f'O valor da venda é {valor_venda}')

