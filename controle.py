from modelo import Funcionarios, Clientes, Pedidos, Produto

#criação das clases responsavel pelo o controle do sistema
class ControledoSistema:
    def __init__(self): #Criei listas vazias para guardar os dados
     self.clientes = []
     self.funcionarios = []
     self.pedidos = []
     self.produtos = []
    

#Crud
#Cadastrando Cliente
    def cadastrar_cliente (self, cliente):
       self.clientes.append(cliente)
    
 #Listando cliente
    def lista_clientes (self):
       return self.clientes
 
 #Buscando cliente
    def buscar_cliente (self, cpf):
       for cliente in self.clientes:
          if cliente.cpf == cpf:
             return cliente
       return None

#Adicionando cliente    
    def atualizar_cliente (self, cpf, novo_nome = None , novo_telefone = None, novo_email = None):
       for cliente in self.clientes:
           if cliente.cpf == cpf:
             if novo_nome is not None:
              cliente.nome = novo_nome
             if novo_telefone is not None:
               cliente.telefone = novo_telefone
             if novo_email is not None:
                  cliente.email = novo_email
             return True 
       return False      

#Deletetando cliente
    def deletar_cliente(self, cpf):
       for cliente in self.clientes:
          if cliente.cpf == cpf:
             self.clientes.remove(cliente)
             return True
       return False
          


#Cadastrando funcionario
    def cadastrar_funcionario(self, funcionario):
     self.funcionarios.append(funcionario)

#listando
    def lista_funcionarios(self):
     return self.funcionarios

#Buscando    
    def buscar_funcionario (self, matricula):
       for funcionario in self.funcionarios:
          if funcionario.matricula == matricula:
             return funcionario
       return None

#Atualizando
    def atualizar_funcionario (self, matricula, novo_nome = None , novo_telefone = None):
       for funcionario in self.funcionarios:
         if funcionario.matricula == matricula:
           if novo_nome is not None:
            funcionario.nome = novo_nome 
            if novo_telefone is not None:
              funcionario.telefone = novo_telefone
            return True 
       return False
         

#Deletetando Funcionarios
    def deletar_funcionario(self, matricula):
       for funcionario in self.funcionarios:
          if funcionario.matricula == matricula:
             self.funcionarios.remove(funcionario)
             return True
       return False
    

#Cadastrando produto
    def cadastrar_produto (self, produto):
       self.produtos.append(produto)
    
 #Listando produto
    def lista_produtos (self):
       return self.produtos
 
 #Buscando produto
    def buscar_produto (self, id_produto):
       for produto in self.produtos:
          if produto.id_produto == id_produto:
             return produto
       return None

#Adicionando produto
    def atualizar_produto (self, id_produto,data_validade= None):
       for produto in self.produtos:
         if produto.id_produto == id_produto:
           if data_validade is not None:
             produto.data_validade = data_validade
             return True 
       return False

#Deletetando produto
    def deletar_produto(self, id_produto):
       for produto in self.produtos:
          if produto.id_produto == id_produto:
             self.produtos.remove(produto)
             return True
       return False
          

 #Cadastrando pedido
    def cadastrar_pedido (self, pedido):
       self.pedidos.append(pedido)
    
 #Listando pedido
    def lista_pedidos (self):
       return self.pedidos
 
 #Buscando pedido
    def buscar_pedido (self, id_pedido):
       for pedido in self.pedidos:
          if pedido.id_pedido == id_pedido:
             return pedido
       return None

#Adicionando pedido
    def atualizar_pedido(self, id_pedido, produto=None, quantidade=None, preco=None):
       for pedido in self.pedidos: 
          if pedido.id_pedido == id_pedido: 
             if produto is not None: pedido.produto = produto 
             if quantidade is not None:
                pedido.quantidade = quantidade 
             if preco is not None: pedido.preco = preco 
             return True 
       return False

#Deletetando pedido
    def deletar_pedido(self, id_pedido):
       for pedido in self.pedidos:
          if pedido.id_pedido == id_pedido:
             self.pedidos.remove(pedido)
             return True
       return False