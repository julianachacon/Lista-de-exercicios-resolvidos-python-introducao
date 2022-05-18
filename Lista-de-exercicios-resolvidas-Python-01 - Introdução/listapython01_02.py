numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
exponenciacao = numero1 ** numero2


print('A soma vale', soma)
print('A subtração vale', subtracao)
print('A mutiplicação vale', multiplicacao)
print('A exponenciação vale', exponenciacao)

# Divisão por zero corrigido

if numero2 != 0:
    divisao = numero1 / numero2
    divisao_inteira = numero1 // numero2
    resto_da_divisao = numero1 % numero2
    print('A divisão vale', divisao)
    print('A divisão inteira vale', divisao_inteira)
    print('O resto da divisão é', resto_da_divisao)

else:
    print("Não se pode dividir por 0")
