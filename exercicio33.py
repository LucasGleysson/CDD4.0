a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
m = a
for i in range(10):
    a[i] = int(input(f'Digite o {i+1}º valor: '))

digito = int(input('Digite o valor que vai mutiplicar os números: '))
for j in range(10):
    m[j] = a[j] * digito

print(m)
