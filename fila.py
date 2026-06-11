class No:
    def __init__(self, filme):
        self.filme = filme
        self.proximo = None


class FilaFavoritos:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def adicionar_favorito(self, filme):
        novo_no = No(filme)

        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

        self.tamanho += 1
        print(f'"{filme}" adicionado aos favoritos.')

    def remover_favorito(self,nome_filme):
        if self.esta_vazia():
            print("Nenhum filme favorito para remover.")
            return None

        atual = self.inicio
        anterior = None

        while atual:
            if atual.filme == nome_filme:

                # Remove o primeiro nó
                if anterior is None:
                    self.inicio = atual.proximo

                    if self.inicio is None:
                        self.fim = None

                # Remove um nó do meio ou do final
                else:
                    anterior.proximo = atual.proximo

                    if atual == self.fim:
                        self.fim = anterior

                self.tamanho -= 1
                print(f"Filme '{nome_filme}'  removido dos favoritos.")
            anterior = atual
            atual = atual.proximo

    print(f'Filme não encontrado nos favoritos.')
    
    def listar_favoritos(self):
        if self.esta_vazia():
            print("Nenhum filme favorito cadastrado.")
            return

        atual = self.inicio
        print("\n=== FILMES FAVORITOS ===")

        posicao = 1
        while atual:
            print(f"{posicao}. {atual.filme}")
            atual = atual.proximo
            posicao += 1

    def primeiro_favorito(self):
        if self.esta_vazia():
            return None
        return self.inicio.filme

    def quantidade(self):
        return self.tamanho