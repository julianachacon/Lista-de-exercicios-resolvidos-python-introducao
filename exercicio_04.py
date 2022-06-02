n = input('Digite algo: ')
print(type(n))
num = n.isnumeric() 
alphabet = n.isalpha()
alnum = n.isalnum()
ascii = n.isascii() #vazio; codigos numericos de 0 a 127 que presentam letras; simbolos; e U+0000-U+007F.
decimal = n.isdecimal()
digit = n.isdigit()
ident = n.isidentifier() #identificavel pelo python
minusculo = n.islower()
maiusculo = n.isupper()
impress = n.isprintable # vazio ou passeiveis de impressão/print
space = n.isspace () #Os caracteres usados ​​para espaçamento são chamados de caracteres de espaço em branco. Por exemplo: tabulações, espaços, nova linha, etc.
title = n.istitle ()

print('É numérico?', num)
print('É Alfabético?', alphabet)
print('É alfanumérico? ', alnum)
print('É Ascii?', ascii)
print('É Decimal?', decimal)
print('É Digito?', digit)
print('É identificavel pelo python?', ident)
print('Esta minusculo?', minusculo)
print('Esta maiusculo?', maiusculo)
print('É passivel de impressão?', impress)
print('É um caractere usado para espaçamento no Python?', space)
print('É um titulo?', title)
