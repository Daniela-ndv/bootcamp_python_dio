#### Parte 1:
Sistema bancário com as funções de sacar, depositor e visualizar extrato. Requisitos: 
- Limite de 3 saldos diários, valor máximo R$ 500,00
- Deve existir mensagens de erro 
- Todos o saques e depósitos devem ser listados 

#### Parte 2:
Otimizando:
- Criar funções
- Adicionar funcs cadastrar usuário e cadastrar conta bancária

#### Parte 3:
Atualizar a implementação 
- Armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários
- O código deve seguir o modelo UML disponibilizado
- Desafio extra: Atualizar os métodos que tratam as opções do menu para funcionarem com as classes modeladas

#### Parte 4:
Implementar funcionalidades:
- Decorador de log: aplicado a todas as funções de transações. Deve printar o tipo, a hora e a data de cada transação.
- Gerador de relatórios: permite iterar sobre as transações de uma conta e retorne as transações que foram realizadas. Deve ter uma forma de filtrar baseado no tipo de transação
- Iterador personalizado: implementar um iterador personalizado ContaIterador que retorne informações básicas de cada conta
- Informações: Limite de 10 transações diárias, deve haver alerta caso o usuário exceder esse limite

#### Parte 5: 
Manipulação de arquivos: 
- Modificar o decorador de log para salvar as informações de log em um arquivo
