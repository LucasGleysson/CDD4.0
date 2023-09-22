soma = 0
quantidade = int(input('Digite a quantidade de alunos da sala: '))
for aluno in range(quantidade):
    nota = float(input(f'Digite a nota do {aluno+1}º aluno: '))
    soma += nota
media = soma / quantidade
print(f'A média da turma é {media:.1f}')
