tamanho = int(input("Quantos elementos você deseja inserir no vetor? "))

vetor = []

for i in range(tamanho):
    elemento = int(input(f"Digite um número para adicionar {i + 1}º: "))
    vetor.append(elemento)

print(f"O vetor criado é: {vetor}")