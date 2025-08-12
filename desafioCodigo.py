#Descrição
#Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# Verifica se o cupom é válido e calcula o desconto
if cupom in descontos:
    desconto = descontos[cupom]
else:
    desconto = descontos["SEM_DESCONTO"]
# Calcula o preço final
preco_final = preco * (1 - desconto)    
# Exibe o preço final formatado
print(f"R$ {preco_final:.2f}")
