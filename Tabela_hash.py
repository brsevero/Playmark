historico = {}  

def registrar_filme(titulo: str, ano: int, nota: int, data: str) -> None:
    chave = titulo.strip().title()
    historico[chave] = {
        "ano":  ano,
        "nota": nota,
        "data": data,
    }

def buscar_filme(titulo: str) -> dict | None:
    chave = titulo.strip().title()
    if chave in historico:
        dados = historico[chave]
        print(f'\n  🎬 Encontrado: "{chave}"')
        print(f'     Ano  : {dados["ano"]}')
        print(f'     Nota : {dados["nota"]}/10')
        print(f'     Data : {dados["data"]}')
        return dados
    else:
        print(f'\n  ✖ "{chave}" não está no histórico.')
        return None

def listar_historico() -> None:
    if not historico:
        print("  O histórico está vazio.")
        return

    print(f"\n  {'TÍTULO':<30} {'ANO':<6} {'NOTA':<6} {'DATA ASSISTIDO'}")

    for titulo, dados in historico.items():
        print(f"  {titulo:<30} {dados['ano']:<6} {dados['nota']:<6} {dados['data']}")
