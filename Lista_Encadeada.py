import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from filme import Filme

class CatalogoFilmes:
    
    def __init__(self):
        self.cabeca = None  # Início do catálogo

    def adicionar_filme(self, titulo, genero, avaliacao, comentarios):
        """Cria uma instância da entidade Filme e a adiciona ao final da lista."""
        # Criando o objeto/nó com os novos atributos
        novo_filme = Filme(titulo, genero, avaliacao, comentarios)
        
        # Se a lista estiver vazia
        if self.cabeca is None:
            self.cabeca = novo_filme
            print(f"-> '{titulo}' adicionado como o primeiro filme do catálogo.")
            return
        
        # Se já houverem filmes, percorre até o último
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        
        # Conecta o último filme ao novo filme
        atual.proximo = novo_filme
        print(f"-> '{titulo}' adicionado ao catálogo.")

    def exibir_catalogo(self):
        """Percorre a lista encadeada e exibe todos os filmes."""
        if self.cabeca is None:
            print("O catálogo está vazio.")
            return
        
        print("\n==========================================")
        print("          MEU CATÁLOGO DE FILMES          ")
        print("==========================================")
        
        atual = self.cabeca
        posicao = 1
        while atual is not None:
            print(f"{posicao}. {atual}")
            print("-" * 42)
            atual = atual.proximo
            posicao += 1

# --- Testando a Integração ---
if __name__ == "__main__":
    meu_sistema = CatalogoFilmes()

    # Adicionando filmes com os novos atributos (Título, Gênero, Avaliação, Comentários)
    meu_sistema.adicionar_filme(
        "Interestelar", 
        "Ficção Científica", 
        9.5, 
        "Excelente abordagem sobre física quântica e viagem no tempo. Visual incrível!"
    )
    
    meu_sistema.adicionar_filme(
        "O Auto da Compadecida", 
        "Comédia/Drama", 
        10.0, 
        "Um clássico do cinema brasileiro. Chicó e João Grilo são eternos."
    )

    meu_sistema.exibir_catalogo()