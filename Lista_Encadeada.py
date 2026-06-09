import sys
import io

# Força a saída do terminal a aceitar caracteres UTF-8 (acentos)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Filme:
    """Representa um nó da lista encadeada."""
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.proximo = None  # Aponta para o próximo filme (inicialmente nenhum)

    def __str__(self):
        return f"Título: {self.titulo} | Gênero: {self.genero} | Ano: {self.ano}"


class CatalogoFilmes:
    """Representa a lista encadeada em si."""
    def __init__(self):
        self.cabeca = None  # O primeiro filme do catálogo

    def adicionar_filme(self, titulo, genero, ano):
        """Adiciona um novo filme ao final do catálogo."""
        novo_filme = Filme(titulo, genero, ano)
        
        # Se o catálogo estiver vazio, o novo filme se torna a cabeça
        if self.cabeca is None:
            self.cabeca = novo_filme
            print(f"Filme '{titulo}' adicionado como o primeiro do catálogo.")
            return
        
        # Caso contrário, percorre a lista até encontrar o último filme
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        
        # O último filme agora aponta para o novo filme
        atual.proximo = novo_filme
        print(f"Filme '{titulo}' adicionado ao final do catálogo.")

    def exibir_catalogo(self):
        """Percorre e exibe todos os filmes do catálogo."""
        if self.cabeca is None:
            print("O catálogo está vazio.")
            return
        
        print("\n--- CÁTALOGO DE FILMES ---")
        atual = self.cabeca
        posicao = 1
        while atual is not None:
            print(f"{posicao}. {atual}")
            atual = atual.proximo
            posicao += 1
        print("--------------------------\n")


# --- Testando a estrutura no seu sistema ---
if __name__ == "__main__":
    meu_catalogo = CatalogoFilmes()

    # Adicionando filmes dinamicamente
    meu_catalogo.adicionar_filme("Interestelar", "Ficção Científica", 2014)
    meu_catalogo.adicionar_filme("O Poderoso Chefão", "Drama/Crime", 1972)
    meu_catalogo.adicionar_filme("Matrix", "Ação/Ficção Científica", 1999)

    # Exibindo o catálogo completo
    meu_catalogo.exibir_catalogo()