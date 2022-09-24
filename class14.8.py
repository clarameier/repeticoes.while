n = 0
ntotais = 0
soma = 0
n = int(input('Digite um número inteiro [digite 999 para o programa parar]: '))
while n != 999:
    soma += n
    ntotais += 1
    n = int(input('Digite um número inteiro [digite 999 para o programa parar]: '))
print('Você digitou {} números, e a soma de todos eles foi de: {}.'.format(ntotais, soma))