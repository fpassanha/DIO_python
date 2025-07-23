def saudacao(nome):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá, visitante!")

for pessoa in ["Ana", "Bruno", ""]:
    saudacao(pessoa)

def depositar(valor):
    if valor > 0:
        print(f"Depósito de {valor} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")    

for valor in [100, -50, 0]:
    depositar(valor)
