sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dado inválido, por favor digite novamente o seu sexo como F ou M de Femino e Masculino: ')).strip().upper()[0]
print('Obrigada pela sua participação!')    
