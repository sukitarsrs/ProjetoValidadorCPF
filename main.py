cpf = input('Digite um CPF: ')
numeros = [char for char in cpf if char.isdigit()]
soma1 = 0
multiplicador1 = 10

for char in cpf:
    if char in '.-':
        continue
    if multiplicador1 == 1: 
        break
    soma1 += int(char) * multiplicador1
    multiplicador1 -= 1

resultado1 = (soma1 * 10) % 11
if resultado1 > 9:
    resultado1 = 0

soma2 = 0
multiplicador2 = 11
for char in cpf:
    if char in '.-':
        continue
    if multiplicador2 == 1:
        break
    soma2 += int(char) * multiplicador2
    multiplicador2 -= 1

resultado2 = (soma2 * 10) % 11
if resultado2 > 9:
    resultado2 = 0

digito1 = int(numeros[9])
digito2 = int(numeros[10])

if resultado1 == digito1 and resultado2 == digito2:
    print('CPF valido')
else:
    print('CPF invalido')
