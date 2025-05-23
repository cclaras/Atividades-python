tamanho = int(input("Quantos elementos você deseja inserir no vetor? "))

numeros = []

for i in range (tamanho):
    numero = int(input(f"Adicione o {i + 1}º número inteiro: "))
    numeros.append(numero)

soma = 0 

for numero in numeros:
    soma = soma + numero

print(f"A soma dos números do seu vetor é: {soma}")