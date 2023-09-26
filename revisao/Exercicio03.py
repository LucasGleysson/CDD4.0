ano_atual = 2023
mes_atual = int(input('Digite o número do mês atual: '))
mes_nascimento = int(input('Digite o mês em que você nasceu: '))
idade = int(input('Digite a idade: '))

if mes_atual < mes_nascimento:
    ano_atual -= 1

ano_nascimento = ano_atual - idade
print(f'A pessoa nasceu no ano de {ano_nascimento}')
