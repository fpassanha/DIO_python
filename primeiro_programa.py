# primeiro_programa.py
#print("Oi, seja bem-vindo ao meu primeiro programa em python!")

#Tipo de dados

#print(11 + 10 + 1000)
#print(1.5 + 2.5)
#print(True)
#print(False)
#print("Python é uma linguagem de programação")

#Variáveis e constantes

#age = 44    
#name = "João"
#print(f'Meu nome é {name} e tenho {age} anos')

#age, name = 45, "Fabio"
#print(f'Meu nome é {name} e tenho {age} anos')

#Constantes 
#PI = 3.14 
#print(f'O valor de PI é {PI}')

#Convenção de tipos de dados

print(int(1.999))
print(int("10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)
print(100 // 2)  # Divisão inteira
print(100 % 3)   # Módulo (resto da divisão)   

# Funções de entrada e saída
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f'Olá {nome}, você tem {idade} anos')

