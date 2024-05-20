# Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações 
# sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para 
# solicitar ao usuário inserir até três equipamentos.

itens = []
cont = 0

while cont < 3:
    item = input("Digite o nome do equipamento (ou digite 'sair' para encerrar): ")
        
    itens.append(item)
    cont += 1

    if item.lower() == 'sair':
        itens.clear()
        break

print("\nLista de Equipamentos:")  
for item in itens:
    print(f"- {item}")
