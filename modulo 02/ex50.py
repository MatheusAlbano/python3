soma = 0
for c in range(0,6):
    n = int(input("Digite o {} valor: ".format(c+1)))
    if (n % 2 == 0):
        soma = soma + n
print("A soma dos números pares digitados é igual a {}".format(soma))        

