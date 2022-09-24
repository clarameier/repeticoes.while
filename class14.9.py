#variáveis
resposta = 'S'
soma = 0
quantidade = 0
media = 0
maior = 0
menor = 0

#códigos
while resposta in 'Ss':
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar a digitar [S/N]? ')).strip().upper()[0]
media = soma / quantidade
print('Você digitou {} números e a média entre eles é de {}.'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor {}.'.format(maior, menor))