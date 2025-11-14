# Dicionário para agrupar participantes por tema
eventos = {}

print("Entrada dos participantes e seus temas: ")
# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    
    # Separa o nome do participante e o tema por ", "
    partes = linha.split(", ")
    
    # Separa o nome do participante e o tema
    participante = partes[0]
    tema = partes[1]
    
    # Adiciona ao dicionário de eventos
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participante)

print("Dados dos eventos organizados:")
# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")