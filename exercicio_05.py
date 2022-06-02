# 3-	Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor.

n = int(input('Digite um numero: '))
sucessor = n + 1
antecessor = n - 1
print("O número {} possui como sucessor o número {} e como antecessor o número {}".format(
    n, sucessor, antecessor))

# se não for usar as variaveis depois
#print("O número {} possui como sucessor o número {} e como antecessor o número {}".format(n, (n + 1), (n - 1)))
