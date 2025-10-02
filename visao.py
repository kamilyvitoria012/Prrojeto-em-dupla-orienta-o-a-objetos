# Importando as classes do modelo e o controle do sistema
from modelo import Clientes, Pedidos, Produto
from controle import ControledoSistema

# SUBMENU DE CLIENTES

def menu_clientes(sistema):
    while True:  # Loop infinito até o usuário escolher "0 - Voltar"
        print("\n=== MENU CLIENTES ===")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        # ---- CADASTRAR CLIENTE ----
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            cliente = Clientes(nome, telefone, cpf, email)  # Cria objeto cliente
            sistema.cadastrar_cliente(cliente)  # Salva no sistema
            print(" Cliente cadastrado com sucesso!")

        # ---- LISTAR CLIENTES ----
        elif opcao == "2":
            print("\n--- Clientes cadastrados ---")
            for c in sistema.lista_clientes():
                print(c)

        # ---- ATUALIZAR CLIENTE ----
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente para atualizar: ")
            novo_nome = input("Novo nome (Enter para manter): ")
            novo_telefone = input("Novo telefone (Enter para manter): ")
            novo_email = input("Novo email (Enter para manter): ")
            atualizado = sistema.atualizar_cliente(
                cpf,
                novo_nome if novo_nome else None,
                novo_telefone if novo_telefone else None,
                novo_email if novo_email else None
            )
            print(" Cliente atualizado!" if atualizado else "Cliente não encontrado.")

        # ---- DELETAR CLIENTE ----
        elif opcao == "4":
            cpf = input("Digite o CPF do cliente a ser deletado: ")
            if sistema.deletar_cliente(cpf):
                print(" Cliente removido com sucesso!")
            else:
                print("Cliente não encontrado.")

        # ---- VOLTAR ----
        elif opcao == "0":
            break  # Sai do submenu

        else:
            print(" Opção inválida.")

# SUBMENU DE PRODUTOS
def menu_produtos(sistema):
    while True:
        print("\n=== MENU PRODUTOS ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Deletar produto")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        # ---- CADASTRAR PRODUTO ----
        if opcao == "1":
            id_produto = input("ID do Produto: ")
            validade = input("Data de validade: ")
            produto = Produto(id_produto, validade)
            sistema.cadastrar_produto(produto)
            print("Produto cadastrado!")

        # ---- LISTAR PRODUTOS ----
        elif opcao == "2":
            print("\n--- Produtos cadastrados ---")
            for p in sistema.lista_produtos():
                print(p)

        # ---- DELETAR PRODUTO ----
        elif opcao == "3":
            id_produto = input("Digite o ID do produto a ser deletado: ")
            if sistema.deletar_produto(id_produto):
                print("Produto removido com sucesso!")
            else:
                print(" Produto não encontrado.")

        # ---- VOLTAR ----
        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


# SUBMENU DE PEDIDOS
def menu_pedidos(sistema):
    while True:
        print("\n=== MENU PEDIDOS ===")
        print("1 - Fazer pedido")
        print("2 - Listar pedidos")
        print("3 - Deletar pedido")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        # ---- FAZER PEDIDO ----
        if opcao == "1":
            id_pedido = input("ID do pedido: ")
            cpf = input("CPF do cliente: ")
            id_produto = input("ID do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço unitário: "))

            cliente = sistema.buscar_cliente(cpf)    # Busca cliente pelo cpf
            produto = sistema.buscar_produto(id_produto)  # Busca produto pelo ID do prod

            if cliente and produto:  # Só cria pedido se cliente e produto existirem
                pedido = Pedidos(id_pedido, cliente, produto, quantidade, preco)
                sistema.cadastrar_pedido(pedido)
                print(" Pedido cadastrado!")
            else:
                print(" Cliente ou produto não encontrado")

        # ---- LISTAR PEDIDOS ----
        elif opcao == "2":
            print("\n--- Pedidos cadastrados ---")
            for p in sistema.lista_pedidos():
                print(p)

        # ---- DELETAR PEDIDO ----
        elif opcao == "3":
            id_pedido = input("Digite o ID do pedido a ser deletado: ")
            if sistema.deletar_pedido(id_pedido):
                print(" Pedido removido com sucesso!")
            else:
                print(" Pedido não encontrado.")

        #---VOLTAR ----
        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

# MENU PRINCIPAL
def main():
    sistema = ControledoSistema()  # Criação  do banco de dados do sistema (listas)

    while True:  # Loop infinito do menu principal
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Menu de Clientes")
        print("2 - Menu de Produtos")
        print("3 - Menu de Pedidos")
        print("0 - Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes(sistema)   # Abre submenuj de clientes
        elif opcao == "2":
            menu_produtos(sistema)   # Abre submenu de produtos
        elif opcao == "3":
            menu_pedidos(sistema)    # Abre submenu de pedidos
        elif opcao == "0":
            print(" Saindo do sistema...")
            break
        else:
            print(" Opção inválida.")

#executar programa
if __name__ == "__main__":
    main()
