import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class Pessoa:
    OPCOES_GENERO = ("Feminino", "Masculino", "Prefiro Não Dizer")
    OPCOES_TIPO = ("Usuário", "Diretor", "Ator/Atriz")
    
    # Método auxiliar para limpar qualquer texto (remove acento, tira espaço, padroniza)
    def _normalizar_texto(self, texto):
        texto = str(texto).replace(" ", "").strip().title()
        com_acentos = "ÁÀÃÂÉÈÊÍÏÓÔÕÖÚÇÑáàãâéèêíïóôõöúçñ"
        sem_acentos = "AAAAEEEIIOOOOUCNaaaaeeeiiooooucn"
        mapa = str.maketrans(com_acentos, sem_acentos)
        return texto.translate(mapa)

    def __init__(self, id_pessoa, nome, data_nascimento, genero, tipo_pessoa, data_atual="2026-06-10"):
        
        genero_limpo = self._normalizar_texto(genero)
        genero_final = None
        for op in self.OPCOES_GENERO:
            if self._normalizar_texto(op) == genero_limpo:
                genero_final = op
                break
        if genero_final is None:
            raise ValueError(f"Gênero inválido! Escolha: {self.OPCOES_GENERO}")
        
        tipo_limpo = self._normalizar_texto(tipo_pessoa)
        tipo_final = None
        for op in self.OPCOES_TIPO:
            if self._normalizar_texto(op) == tipo_limpo:
                tipo_final = op
                break
        if tipo_final is None:
            raise ValueError(f"Tipo inválido! Escolha: {self.OPCOES_TIPO}")

        partes_nasc = data_nascimento.split("-")
        partes_hoje = data_atual.split("-")
        
        idade = int(partes_hoje[0]) - int(partes_nasc[0])
        if (int(partes_hoje[1]), int(partes_hoje[2])) < (int(partes_nasc[1]), int(partes_nasc[2])):
            idade -= 1
            
        if idade < 18:
            raise ValueError(f"Cadastro bloqueado: {nome} tem {idade} anos. Mínimo 18.")
            
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero_final
        self.tipo_pessoa = tipo_final

    def __str__(self):
        return f"[{self.id_pessoa}] {self.nome} - {self.tipo_pessoa} | Nasc: {self.data_nascimento} | Gênero: {self.genero}"


"""if __name__ == "__main__":
    p1 = Pessoa(1, "Ana", "1990-01-01", "Feminino", "usuario")        
    p2 = Pessoa(2, "Beto", "1990-01-01", "Masculino", "U S U A R I O") 
    p3 = Pessoa(3, "Caio", "1990-01-01", "Masculino", "USUÁRIO")
    
    print(p1)
    print(p2)
    print(p3)"""