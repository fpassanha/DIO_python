# Exemplo 1: for
for i in range(5):
    print(f"For: {i}")

# Exemplo 2: while
contador = 0
while contador < 3:
    print(f"While: {contador}")
    contador += 1

# Exemplo 3: for em lista
nomes = ["Ana", "Bruno", "Carlos"]
for nome in nomes:
    print(f"Olá, {nome}!")

# Exemplo de tabuada do 5
print("Tabuada do 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Exemplo com break
print("Exemplo com break:")
for numero in range(1, 10):
    if numero == 5:
        print("Número 5 encontrado, interrompendo o loop.")
        break
    print(f"Número: {numero}")