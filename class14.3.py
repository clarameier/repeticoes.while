print('='*55)
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0

#menu
while menu != 5:
    print('='*55)
    print('MENU')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    menu = int(input('Digite o número, de 1 a 5, que deseja: '))
    print('='*55)

#somar
    if menu == 1:
        soma = num1 + num2
        print('A soma dos números {} e {} é igual a {}!'.format(num1, num2, soma))

#multiplicar
    elif menu == 2:
        multiplica = num1 * num2
        print('A multiplicação dos números {} e {} é igual a {}!'.format(num1, num2, multiplica))

#maior
    elif menu == 3:
        if num1 > num2:
            print('Entre os números {} e {}, o {} é o maior número digitado!'.format(num1, num2, num1))
        if num2 > num1:
            print('Entre os números {} e {}, o {} é o maior número digitado!'.format(num1, num2, num2))
        if num1 == num2:
            print('Nenhum número digitado é maior que o outro, os dois tem o mesmo valor!')

#novos números
    elif menu == 4:
        print('Informe novos números que você deseja!')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))   

#sair do programa
    elif menu == 5:
        print('Obrigada por usar nosso programa, até mais! Tchau tchau!')

#número inválido
    else:
        print('MENU')
        print('[1] somar')
        print('[2] multiplicar')
        print('[3] maior')
        print('[4] novos números')
        print('[5] sair do programa')
        menu = int(input('Dado inválido. Digite um número, de 1 a 5, que deseja: '))
    print('='*55)