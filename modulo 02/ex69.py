idade = cont_18 = cont_h = cont_m20 = 0
sexo = ''
continuar = ''
print('-'*30)
while True:
    continuar = 'S'
    
    while continuar == 'S':
        print('CADASTRE UMA PESSOA')
        print('-'*30)
        idade = int(input('Idade: '))
        while idade <= 0:
            idade = int(input('Idade: '))
        sexo = input('Sexo: [M/F] ').strip().upper()
        while sexo != 'M' and sexo != 'F':
            sexo = input('Sexo: [M/F] ').strip().upper()
        print('-'*30)
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        while continuar != 'S' and continuar != 'N':
            continuar = input('Quer continuar? [S/N] ').strip().upper()
        if idade > 18:
            cont_18 += 1
        if sexo == 'M':
            cont_h +=1
        if sexo == 'F' and idade < 20:
            cont_m20 += 1
        print('-'*30)
    break
           
print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {cont_18}')  
print(f'Ao todo temos {cont_h} homens cadastrados')
print(f'E temos {cont_m20} mulheres com menos de 20 anos') 

    

