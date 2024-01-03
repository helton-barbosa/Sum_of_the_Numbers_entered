number = int(input('Quantos números quer passar? '))

soma = 0
count = 0

while count < number:
    n = int(input('Número: '))
    soma += n
    count += 1

print(f'A soma de todos os números digitados é {soma}')
