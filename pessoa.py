import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Pessoa:
    OPCOES_GENERO = ("Feminino", "Masculino", "Prefiro Não Dizer")
    OPCOES_TIPO = ("Usuário", "Diretor", "Ator/Atriz")
    
    def __init__(self, id_pessoa, nome, data_nascimento, genero, tipo_pessoa, data_atual="2026-06-10"):
        
        # --- 1. TRATAMENTO DO GÊNERO (Sanitização e Acentos) ---
        genero_input = str(genero).strip().title()
        
        # Criação de um mapa de tradução para remover acentos
        com_acentos = "ÁÀÃÂÉÈÊÍÏÓÔÕÖÚÇÑáàãâéèêíïóôõöúçñ"
        sem_acentos = "AAAAEEEIIOOOOUCNaaaaeeeiiooooucn"
        mapa_acentos = str.maketrans(com_acentos, sem_acentos)
        
        # Remove os acentos do que o usuário digitou
        genero_limpo = genero_input.translate(mapa_acentos)
        
        # Busca qual opção oficial corresponde ao texto digitado
        genero_final = None
        for opcao_oficial in self.OPCOES_GENERO:
            # Compara a versão sem acento da opção oficial com a versão sem acento do usuário
            if opcao_oficial.translate(mapa_acentos) == genero_limpo:
                genero_final = opcao_oficial  # Salva a opção oficial, preservando o acento correto!
                break
                
        # Se após a busca não encontrou correspondência, bloqueia
        if genero_final is None:
            raise ValueError(f"Gênero inválido! Escolha: {self.OPCOES_GENERO}")
            
        # --- 2. Validação do Tipo de Pessoa ---
        # (Podemos aplicar a mesma lógica de acentos aqui no futuro, se quiser!)
        tipo_input = str(tipo_pessoa).strip().title()
        if tipo_input not in self.OPCOES_TIPO:
            raise ValueError(f"Tipo inválido! Escolha: {self.OPCOES_TIPO}")
            
        # --- 3. Validação de Idade ---
        partes_nasc = data_nascimento.split("-")
        ano_nasc = int(partes_nasc[0])
        mes_nasc = int(partes_nasc[1])
        dia_nasc = int(partes_nasc[2])
        
        partes_hoje = data_atual.split("-")
        ano_atual = int(partes_hoje[0])
        mes_atual = int(partes_hoje[1])
        dia_atual = int(partes_hoje[2])
        
        idade = ano_atual - ano_nasc
        
        if mes_atual < mes_nasc or (mes_atual == mes_nasc and dia_atual < dia_nasc):
            idade -= 1
            
        if idade < 18:
            raise ValueError(f"Cadastro bloqueado: {nome} tem {idade} anos. É obrigatório ter 18 anos ou mais.")
            
        # Atribuição final
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero_final  # Salva a variável que pegou a opção oficial correta
        self.tipo_pessoa = tipo_input

    def __str__(self):
        return f"[{self.id_pessoa}] {self.nome} - {self.tipo_pessoa} | Nasc: {self.data_nascimento} | Gênero: {self.genero}"


# --- Testando a Tolerância a Falhas ---

if __name__ == "__main__":
    print("Testando as Verificações e o Tratamento dos Dados...")
    
    # Teste 1: Sem acento e tudo minúsculo
    p1 = Pessoa(1, "Julio", "1990-05-10", "prefiro nao dizer", "Usuário")
    print(p1)
    # Resultado: Gênero: Prefiro Não Dizer (Corrigiu e devolveu o acento e as maiúsculas)
    
    # Teste 2: Usuário digitou acentos errados (ex: Féminino)
    p2 = Pessoa(2, "Carla", "1985-08-20", "  Féminíno  ", "Diretor")
    print(p2)
    # Resultado: Gênero: Feminino (Removeu a bagunça e salvou o correto)