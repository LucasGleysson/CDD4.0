qnt = int(input('Digite a quantidade de números que serão calculados: '))
soma = 0
for i in range(qnt):
    num = float(input(f'Digite o {qnt+1}º número: '))
    soma += num

media = soma / qnt+1
print(f'A soma dos números digitados é {soma}')
print(f'A média dos números é: {media}')
