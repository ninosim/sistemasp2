# Obtenha dados da altura e o gênero (Masculino ou Feminino) de 15 pessoas e apresente os seguintes resultados:
# - A maior e a menor altura do grupo;
# - A média de altura das pessoas do gênero Masculino;
# - O número de pessoas do gênero Feminino.

masc = []
fem = []
total = []

print("== Lista de Alturas divididas por Gênero ==")
for i in range(3):
    altura = float(input("Digite a altura: "))
    genero = input("Qual o gênero? Digite M/F: ").strip().upper()[0]
    if genero == "M":
        masc.append(altura)
    else:
        fem.append(altura)

total = masc + fem
total.sort()
print("As alturas digitadas foram: " , (total))

# - A maior e a menor altura do grupo;
print("A maior altura do grupo é: " , (max(total)))
print("A menor altura do grupo é: " , (min(total)))

#Média de altura das pessoas do gênero Masculino
if len(masc) != 0:
    mediamasc = sum(masc) / len(masc)
    print("A média de altura de pessoas do gênero Masculino é: ", mediamasc)
else:
    print("A média de altura das pessoas do gênero Masculino é 0, porque nenhuma foi inserida.")

#O número de pessoas do gênero Feminino.
print("O número de pessoas do gênero Feminino é: ", len(fem))