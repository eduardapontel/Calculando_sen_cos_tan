from math import radians, sin, cos, tan

bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CALCULANDO SEN COS E TAN'))
print(bordas)
print()

a = ''

while type(a) != float:
    try:
        a = float(input('Digite um ângulo: '))
    except:
        print('Por favor digite um ângulo válido!')

print(bordas)
print('SEN -> Para calcular o seno')
print('COS -> Para calcular o cosseno')
print('TAN -> Para calcular a tangente')
print(bordas)

while True:
    convert = input('Digite a opção desejada: ').strip().upper()
    match convert:
        case 'SEN':
            print(f'\nO seno do ângulo é {sin(radians(a)):.2f}')
            break
        case 'COS':
            print(f'\nO cosseno do ângulo é {cos(radians(a)):.2f}')
            break
        case 'TAN':
            print(f'\nA tangente do ângulo é {tan(radians(a)):.2f}')
            break
        case _:
            print('Por favor digite uma opção válida!')
