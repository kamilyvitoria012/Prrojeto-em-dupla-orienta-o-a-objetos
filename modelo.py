#Clientes, Pedidos e Funcionários
#- Descrição: Um restaurante recebe vários pedidos. Cada pedido é
#feito por um cliente específico no restaurante
class Pessoas:
    def __init__(self,nome, telefone,cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

class Funcionarios(Pessoas):
 
    def __init__(self, nome,telefone,cpf,matricula,funcao):
        super().__init__(nome,telefone,cpf)
        self.matricula = matricula
        self.funcao = funcao

    def __str__(self):
        return f"  Nome do funcionário: {self.nome} -Telefone :{self.telefone}- Cpf : { self.cpf}- Matrícula: {self.matricula} - Função: {self.funcao}" 


class Clientes(Pessoas):
    def __init__(self,nome, telefone,cpf,email):
        super().__init__(nome, telefone,cpf)
        self.email = email
        
    def __str__(self):
        return f" Nome do Cliente: {self.nome} -Telefone :{self.telefone} Cpf :{ self.cpf} Email:{self.email}"


class Pedidos:
    def __init__(self,id_pedido,cliente,produto,quantidade,preco):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.preco =  preco
    
    def __str__(self):
        return f"Pedido :{self.id_pedido} Cliente: {self.cliente} Produto:{self.produto} - Quantidade: {self.quantidade} - valor: {self.preco}"
    
    def calcular_preco(self):
        return self.preco * self.quantidade
    
class Produto:
    
    def __init__(self,id_produto,data_validade):
        self.id_produto = id_produto
        self.data_validade = data_validade
    def __str__(self):
        return f"Id Produto :{self.id_produto} data de validade {self.data_validade}"
