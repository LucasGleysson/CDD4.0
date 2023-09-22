count = 0
soma = 0
qnt_alunos = int(input('Digite a quantidade de alunos: '))

# while count < qnt_alunos:
#     nota = float(input(f'Digite a nota do {count+1}º aluno: '))
#     soma += nota
#     count += 1

for i in range(qnt_alunos):
    nota = float(input(f'Digite a nota do {i + 1}º aluno: '))
    soma += nota

media = soma / qnt_alunos
print(f'A média da turma é: {media:.1f}')
