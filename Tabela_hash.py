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

if __name__ == "__main__":

    print("  REGISTRANDO FILMES")
    registrar_filme("Interestelar",       2014, 10, "2025-01-15")
    registrar_filme("Parasita",           2019,  9, "2025-02-03")
    registrar_filme("O Poderoso Chefão",  1972, 10, "2025-03-20")
    registrar_filme("Clube da Luta",      1999,  8, "2025-04-11")
    registrar_filme("Matrix",             1999,  9, "2025-05-02")

    print("\n  HISTÓRICO COMPLETO")
    listar_historico()
    titulo_digitado = input("\n  Digite o nome do filme que quer buscar: ")
    buscar_filme(titulo_digitado)