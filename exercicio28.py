num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
count = 0
while num2 == 0 or count < 5 :
    print('Não existe divisão por zero, tente novamente: ')
    num2 = int(input('Digite outro número: '))
    count += 1


if num2 == 0:
    print('Erro no código! Finalizado')
else:
    resultado = num1 / num2
    print(f'{num1} dividido por {num2} é igual a {resultado}')
