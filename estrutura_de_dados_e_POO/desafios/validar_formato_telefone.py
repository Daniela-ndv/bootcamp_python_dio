# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. 
# Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de 
# telefone tem o formato correto.

# Módulo 're' que fornece operações com expressões regulares.
import re

def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"

    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    if re.match(pattern, phone_number):
        msg = "Número de telefone válido."
        return msg
    else:
        msg = "Número de telefone inválido."
        return msg

print("Número de telefone: ")
phone_number = input()  

result = validate_numero_telefone(phone_number)

print(result)
