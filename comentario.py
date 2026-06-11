from pessoa import Pessoa

class Comentario:
    def __init__(self, id_comentario, autor: Pessoa, texto, data_comentario="2026-06-10"):
        # Validação rigorosa: Apenas o perfil "Usuário" pode fazer comentários
        if autor.tipo_pessoa != "Usuário":
            raise ValueError(f"Operação negada! {autor.nome} possui o perfil '{autor.tipo_pessoa}'. Apenas Usuários podem comentar.")
            
        texto_tratado = str(texto).strip()
        if not texto_tratado:
            raise ValueError("O comentário não pode estar vazio.")

        self.id_comentario = id_comentario
        self.autor = autor
        self.texto = texto_tratado
        self.data_comentario = data_comentario
        
        # Ponteiro para o próximo comentário (Estrutura de Lista Encadeada)
        self.proximo_comentario = None 

    def __str__(self):
        return f"[{self.data_comentario}] {self.autor.nome}: \"{self.texto}\""