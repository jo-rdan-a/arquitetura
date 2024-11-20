def gerar_registro(dados):
    dados_lista = dados.split(';')
    
    registro = {
        "nome": dados[0],
        "cidade": dados[1],
        "idade": int(dados[2]),
        "renda": float(dados[3])
    }
    
    return registro