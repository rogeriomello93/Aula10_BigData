import random
import subprocess

def dobrado(x):
    d = x * 2
    return d

def triplo(y):
    t = y * 3
    return t

def quad(z):
    q = z ** 2
    return q

subprocess.run('cls', shell=True)

num = random.randint(10,100)
print(num)

print("""
[1] - Dobro
[2] - Triplo
[3] - Quadrado
""")

opcao = int(input('Informe a opção: '))

match opcao:
    case 1:
        resultado = dobrado(num)
        # print(f'O dobro do numero é: {resultado}')

    case 2:
        resultado = triplo(num)
        # print(f'O triplo do numero é: {resultado}')

    case 3:
        resultado = quad(num)
        # print(f'O triplo do numero é: {resultado}')
    
    case _:
        resultado = 'Opção inválida'
        # print('Opção inválida')

print(f'Resultado: {resultado}')