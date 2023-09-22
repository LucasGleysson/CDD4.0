notas = [0, 0, 0, 0, 0]
soma = 0

for i in range(5):
    nota = float(input(f'Digite a {i+1}º nota: '))
    notas[i] = nota

for j in range(5):
    soma += notas[j]

media = soma / 5
print(f'A média da tuma é {media}')
for n in range(5):
    if notas[n] >= media:
        print(f'O {n+1}º está acima da média com nota {notas[n]:.1f}')
