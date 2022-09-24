#teste1
for c in range (1,5):
    valor = int(input('Digite o {}° valor: '.format(c)))
print('fim.')


#teste2
c = 0
while c < 20:
    print(c, end=', ')
    c += 1
print('fim')

#teste3
resposta = 'S'
while resposta == 'S':
    for c in range (1,5):
        numero = int(input('Digite o {}° valor: '.format(c)))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('fim')

#teste4
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))