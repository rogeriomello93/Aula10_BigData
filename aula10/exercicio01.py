def multa(p):
    m = p * MULTA
    return m


LIMITE = 100
MULTA = 4 

peso = float(input('Digite o peso do pescado: '))
if peso > LIMITE:
    excedente = peso - LIMITE
    calcula_multa = multa(excedente)
    print(f'O peso total do pescado foi de {peso} e você excedeu em {excedente}kgs a carga permitida!')
    print(f'Você terá de pagar uma multa de R$ {calcula_multa}')

else: 
    print('Você não precisa pagar multa')
    print(f'Você pescou apenas {peso}kgs.')
