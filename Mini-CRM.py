clientes = []

#função de cadastro
def cadastrar_cliente(nome, email, idade, cidade):
    cliente = {
    "nome": nome,
    "email": email,
    "idade": idade,
    "cidade": cidade,
    }
    clientes.append(cliente)
cadastrar_cliente("Gabriel", "gabriel@gmail.com", 21, "Salvador")
#listar todos os cliente
def listar_clientes():
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, Email: {cliente['email']}, Idade: {cliente['idade']}, Cidade: {cliente['cidade']}")
        
#Busca especifica
def buscar_cliente(chave):
    for cliente in clientes:
        if cliente["nome"] == chave or cliente["email"] == chave:
            return cliente
    return None

#atualizar
def atualizar_clientes(email, novo_nome=None, nova_idade=None, nova_cidade=None):
    for cliente in clientes:
        if cliente["email"] == email:
            if novo_nome:
                cliente["nome"] = novo_nome
            if nova_idade:
                cliente["idade"] = nova_idade
            if nova_cidade:
                cliente["cidade"] = nova_cidade
            return True
    return False
    
#remover
def remover_clientes(email):
    for i, cliente in enumerate(clientes):
        if cliente["email"] == email:
            del clientes[i]
            return True
    return False
    
#relatorio geral
def gerar_relatorio():
    total = len(clientes)
    if total == 0:
        print("Nenhum cliente cadastrado.")
        return
        
        
    soma_idades = sum(c["idade"] for c in clientes)
    media_idades = soma_idades / total
    
    cidades = {}
    for c in clientes:
        cidades[c["cidade"]] = cidades.get(c["cidade"], 0) +1
    
    print(f"Total de clientes: {total}")
    print(f"Média de idade: {media_idades:.1f}")
    print("Clientes por cidade:")
    for cidade, qtd in cidades.items():
        print(f"- {cidade}: {qtd}")
        
#menu interativo
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar clientes")
        print("4. Atualizar cliente")
        print("5. Remover cliente")
        print("6. Relatório")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            cidade = input("Cidade: ")
            cadastrar_cliente(nome, email, idade, cidade)
            
        elif opcao == "2":
            listar_clientes()
        
        elif opcao == "3":
            chave = input("Digite o nome ou email: ")
            cliente = buscar_cliente(chave)
            print(cliente if cliente else "Cliente não encontrado.")
            
        elif opcao == "4":
            email = input("Email do cliente a atualizar: ")
            novo_nome = input("Novo nome (ou Enter para manter): ")
            nova_idade = input("Nova idade (ou Enter para manter)")
            nova_cidade = input("Nova cidade (ou Enter para manter)")
            atualizar_clientes(
            		email,
                novo_nome or None,
                int(nova_idade) if nova_idade else None,
                nova_cidade or None
            )
        elif opcao == "5":
            email = input("Email do cliente a remover: ")
            if remover_clientes(email):
                print("Removido com sucesso!")
            else:
                print("Cliente não encontrado.")
                
        elif opcao == "6":
            gerar_relatorio()
            
        elif opcao == "0":
            break
            
        else:
            print("Opção inválida.'")
            
            
menu()