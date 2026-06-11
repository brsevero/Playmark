import sys
import io

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from filme import Filme

class CatalogoFilmes:
    
    def __init__(self):
        self.cabeca = None  # Início do catálogo

    def adicionar_filme(self, titulo, genero):
        """Cria uma instância da entidade Filme e a adiciona ao final da lista."""
        # Criando o objeto/nó com os novos atributos
        novo_filme = Filme(titulo, genero)
        
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

