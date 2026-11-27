def calcula_bonus(v, s):
    b = v * .1
    s = s + b
    return b, s

#inicia o codigo
META = 12000

venda = float(input('Informe o valor das vendas: '))
salario = float(input('Informe o salário: '))

if venda >= META:
    # chama a função! p/ de 10% 
    bonus, novo_salario = calcula_bonus(venda, salario) 
    print(f'\nSeu bonus é de R$ {bonus}')
    print(f'Seu salário será de R$ {novo_salario}')

else:
    print('Você não atingiu a meta de vendas! Você não tem bonus a receber')
    print(f'Seu salário será de R$ {salario}')