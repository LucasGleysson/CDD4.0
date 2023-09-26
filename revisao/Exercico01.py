nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
situacao = "APROVADO"

if media < 7:
    situacao = "RECUPERACAO"
elif media < 4:
    situacao = "REPROVADO"

print(f'A média é {media:.1f}')
