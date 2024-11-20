import json

from util import gerar_registro

def calcular_medias(clientes):
    total_idade = 0
    total_renda = 0
    for cliente in clientes:
        total_idade += cliente['idade']
        total_renda += cliente['salario']
    
    media_idade = total_idade / len(clientes)
    media_renda = total_renda / len(clientes)
    
    return media_idade, media_renda

def main():  

    with open('c:/Users/paulo/OneDrive/Área de Trabalho/Atividade 3 Python - Paulo Victor/clientes.txt', 'r') as file:
        clientes_data = json.load(file)
    
    media_idade, media_renda = calcular_medias(clientes_data)
    
    print(f'Media de Idade: {media_idade:.2f}')
    print(f'Media de Renda: {media_renda:.2f}')

if __name__ == '__main__':
    main()