# 4-	Crie um algoritmo que leia um número e mostre o seu sobro, triplo e raiz quadrada.

n = int(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz_quadrada = pow(n, (1/2))  # ou usar -> n ** (1/2)
print("O dobro de {} é igual a {}. ".format(n, dobro,))
print("O triplo de {} é igual a {}. ".format(n, triplo,))
print("A raiz quadrada de {} é igual a {:.2f}. ".format(n, raiz_quadrada,))
