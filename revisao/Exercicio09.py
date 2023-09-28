mensagem = '''1 - Antecessor
2 - Sucessor
3 - Sair
Digite sua opção: '''

op = ''
while op != "3":
    num = int(input('Digite um número: '))
    op = input(mensagem)
    if op == "1":
        print('-'*15)
        print(f'Seu antecessor é {num-1}')
        print('-' * 15)
    elif op == "2":
        print('-' * 15)
        print(f'Seu sucessor é {num+1}')
        print('-' * 15)
        break
    elif op == "3":
        break
    else:
        print('OPÇÃO INVALIDA')
        op = input(mensagem)
print('-' * 15)
print('FINALIZADO')
print('-' * 15)

