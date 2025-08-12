#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
#Desafio : Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
# Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
# Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato

#Operação de depósito : Deve ser possível depositar valores positivos para a minha conta bancária. 
# A v1 do projeto trabalha apenas com 1 usuario, dessa forma não precisamos nos preocupar em identificar 
# qual é o numero da agencia e conta bancaria. Todos os depositos dever ser armazenados em uma variavel e 
# exibidos na operação de extrato.

#Operação de saque : O sistema deve permitir realizar 3 saques diarios com limite maximo de R$ 500,00 por saque. 
# Caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não sera possivel 
# sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.

#Operação de extrato : Essa operação deve listar todos os depositos e saque realizados na conta. 
# No fim da listagem dever ser exibido o saldo atual da conta. Se o extrato estiver em branco, 
# exibir a mensagem : Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o 
# formato R$ xxx.xx, exemplo 1500.45 = R$ 1500.45

def main():
    saldo = 0
    extrato = []
    limite_saque = 500.00
    numero_saques = 0
    limite_saques = 3

    while True:
        print("\nBem-vindo ao sistema bancário!")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para depósito.")

        elif opcao == '2':
            if numero_saques < limite_saques:
                valor = float(input("Digite o valor do saque: R$ "))
                if valor > 0:
                    if valor <= saldo and valor <= limite_saque:
                        saldo -= valor
                        extrato.append(f"Saque: R$ {valor:.2f}")
                        numero_saques += 1
                        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                    elif valor > saldo:
                        print("Saldo insuficiente para realizar o saque.")
                    elif valor > limite_saque:
                        print(f"O valor máximo para saque é R$ {limite_saque:.2f}.")
                else:
                    print("Valor inválido para saque.")        
            else:
                print("Número máximo de saques diários atingido.")

        elif opcao == '3':
            if extrato:
                print("\n================ EXTRATO ================")
                for movimento in extrato:
                    print(movimento)
                print(f"\nSaldo atual: R$ {saldo:.2f}")
            else:
                print("Não foram realizadas movimentações.")

        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")   

if __name__ == "__main__":
    main()  
#Rodar o programa no terminal com python desafio.py