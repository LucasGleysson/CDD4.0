qnt_alunos = int(input('Digite a quantidade de alunos: '))
lista_alunos = []

for p in range(qnt_alunos):
    nome_aluno = input(f'Digite o nome do {p + 1}º aluno: ')
    lista_alunos.append(nome_aluno)

print('-' * 5, 'LISTA DE ALUNOS', '-' * 5)
for e in range(qnt_alunos):
    print(f'A posição do Aluno {lista_alunos[e]} é {e}')
