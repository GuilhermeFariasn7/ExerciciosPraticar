print('\033[4;32m!Digite 3 valores para saber a soma deles ao quadrado!\033[m ')
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro e ultimo valor: "))
QUAD1 = n1**2
QUAD2 = n2**2
QUAD3 = n3**2
S = ((QUAD1)+(QUAD2)+(QUAD3))
print("A soma de {:.1f} + {:.1f}+ {:.1f}(já estão ao quadrado) é: {:.1f}".format(QUAD1,QUAD2,QUAD3,S))
