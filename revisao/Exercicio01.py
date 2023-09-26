repete = 's'
while repete != 'n':
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    media = (nota1 + nota2) / 2

    situacao = "APROVADO"
    if media < 4:
        situacao = "REPROVADO"
    elif media < 7:
        situacao = "RECUPERAÇÃO"

    print(f'A média é {media:.1f}')
    print(f'O aluno está {situacao}')

    repete = input('Você quer repetir? (s / n): ')
