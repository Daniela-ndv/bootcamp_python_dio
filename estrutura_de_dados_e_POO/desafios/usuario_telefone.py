# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial 
# e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número 
# de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra

# class UsuarioTelefone:
#     def __init__(self, nome, numero, plano):
#         self.nome = nome
#         self.numero = numero
#         self.plano = plano

#     def __str__(self):
#         return f"Usuário {self.nome} criado com sucesso."

# # Entrada dos dados
# nome = input()  
# numero = input()  
# plano = input()  

# # Criação do objeto UsuarioTelefone
# usuario = UsuarioTelefone(nome, numero, plano)

# # Impressão do resultado
# print(usuario)



# Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. 
# Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 
# 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  
# 'mensagem_personalizada' para gerar uma mensagem personalizada.
# Condições da verificação do saldo:
# - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
# - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
# - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# class PlanoTelefone:
#     def __init__(self, nome, saldo):
#         self.nome = nome
#         self.saldo = saldo
    
#     def verificar_saldo(self):
#         return self.saldo

#     def mensagem_personalizada(self):
#         if self.saldo < 10:
#             return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
#         elif self.saldo >= 50:
#             return "Parabéns! Continue aproveitando seu plano sem preocupações."
#         else:
#             return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
                 
# nome = input("Nome: ") 
# plano = input("Plano: ")  
# saldo = int(input("Saldo: "))

# plano = PlanoTelefone(nome, saldo)

# print(plano.mensagem_personalizada())



# Adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. 
# Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto.
# Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e 
# duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar 
# o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if self.plano.verificar_saldo() >= custo:
            self.plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class Plano:
    def __init__(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial

    def verificar_saldo(self):
        return self.saldo_inicial

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        self.saldo_inicial -= valor

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input("Nome: ")
numero = input("Número: ")
saldo_inicial = float(input("Saldo inicial: "))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("Destinatário: ")
duracao = int(input("Duração da chamada (minutos): "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))

