# Exemplo 1: if / if-else / elif
idade = 18
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")

# Exemplo 2: if aninhado
nota = 7
if nota >= 6:
    if nota >= 9:
        print("Excelente!")
    else:
        print("Aprovado!")
else:
    print("Reprovado!")

# Exemplo 3: if ternário
numero = 10
resultado = "Par" if numero % 2 == 0 else "Ímpar"
print(f"O número {numero} é {resultado}.")

