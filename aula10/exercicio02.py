def soma(x,y):
    s = x + y
    return s


def sub(x,y):
    t = x - y
    return t


def mult(x,y):
    q = x * y
    return q


def div(x,y):
    q = x / y
    return q


num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

print("""
[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
""")

opcao = int(input('Escolha uma opção: \n'))

match opcao:
    case 1:
        resultado = soma(num1, num2)
        print(f'A soma dos dois numeros é: {resultado}')

    case 2:
        resultado = sub(num1, num2)
        print(f'A subtração dos dois numeros é:: {resultado}')

    case 3:
        resultado = mult(num1, num2)
        print(f'A multiplicação dos dois numeros é: {resultado}')
    
    case 4:
        resultado = div(num1, num2)
        print(f'A divisão dos dois numeros é: {resultado}')

    case _:
        print('Opção inválida')
        # print('Opção inválida')