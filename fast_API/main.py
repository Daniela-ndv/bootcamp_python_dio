from fastapi import FastAPI
# import random 
import uvicorn

app = FastAPI()

#######################################
# Rota padrão
# @app.get('/')
# async def root():
#     return "API no ar!"

# @app.get('/random')
# async def get_random():
#     rn = random.randint(0,100)
#     return {'random': rn, 'limit': 100}

# @app.get('/random/{limit}')
# async def get_random(limit:int):
#     rn = random.randint(0,limit)
#     return {'random': rn, 'limit': limit}


#######################################
# Métodos GET e POST 

# class Inputs(BaseModel):
#     inp: int
#     inp2: str

# @app.get('/')
# def root():
#     return "API no ar!"

# # Método POST
# @app.post('/exemplo')
# def example(inputs: Inputs) -> str:
#     # ...
#     return inputs.inp2

#Inserir no POST utilizando postman:
# {
#     "inp": 120, 
#     "inp2": "Olá do POST!"
# }

# Saída do POST: inp2


#######################################
# MÉTODO GET EM UM DICIONÁRIO
vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
} 

@app.get('/')
async def root():
    return {"Vendas": len(vendas)}


@app.get('/vendas/{id_venda}')
async def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else: 
        return {"Erro": "ID da venda não encontrado"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000) 



