primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da Progressão Aritmética: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('fim!')