nome = input('Digite o nome do aluno: ')
nota1 = float(input('1º Nota: '))
nota2 = float(input('2º Nota: '))
nota3 = float(input('3º Nota: '))
media = (nota1 + nota2 + nota3) / 3

if media < 4:
    print(nome, 'REPROVADO')
else:
    if media < 7:
        print(nome, 'RECUPERAÇÃO')
    else:
        print(nome, 'APROVADO!')
