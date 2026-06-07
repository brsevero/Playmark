class Filme:
    def __init__(self, nome, pop):
        self.nome = nome
        self.notas = []   # Lista de avaliações de 1 a 5
        self.pop = pop

    def media(self):
        """Retorna a média das notas ou 0.0 se ainda não há avaliações."""
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

class No:
    def __init__(self, filme):
        self.filme = filme
        self.esquerda = None
        self.direita = None

class Arvore_filmes:
    def __init__(self):
        self.raiz = None

    # ─────────────────────────────────────────
    # INSERÇÃO
    # A chave da árvore é (media, nome), para que filmes com mesma média sejam diferenciados.
    
    def inserir(self, filme):
        novo = No(filme)
        if self.raiz is None:
            self.raiz = novo
            return
        atual = self.raiz
        chave_novo = (filme.media(), filme.nome)
        while True:
            chave_atual = (atual.filme.media(), atual.filme.nome)
            if chave_novo < chave_atual:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita

    def remover(self, no, media, nome):
        if no is None:
            return None

        chave = (media, nome)
        chave_atual = (no.filme.media(), no.filme.nome)

        # VAI PARA ESQUERDA
        if chave < chave_atual:
            no.esquerda = self.remover(no.esquerda, media, nome)

        # VAI PARA DIREITA
        elif chave > chave_atual:
            no.direita = self.remover(no.direita, media, nome)

        # ENCONTROU O NÓ
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            # DOIS FILHOS: substitui pelo sucessor in-order (menor da subárvore direita)
            temp = no.direita
            while temp.esquerda is not None:
                temp = temp.esquerda

            no.filme = temp.filme
            no.direita = self.remover(no.direita, temp.filme.media(), temp.filme.nome)

        return no
    # ─────────────────────────────────────────
    # BUSCA POR NOME (percurso completo)
    
    def buscar_por_nome(self, no, nome):
        if no is None:
            return None
        if no.filme.nome.lower() == nome.lower():
            return no
        encontrado = self.buscar_por_nome(no.esquerda, nome)
        if encontrado:
            return encontrado
        return self.buscar_por_nome(no.direita, nome)
    # ─────────────────────────────────────────
    # REMOÇÃO PÚBLICA (busca por nome + remove)
    
    def remover_filme(self, nome):
        encontrado = self.buscar_por_nome(self.raiz, nome)
        if encontrado is None:
            print("Filme não encontrado.")
            return
        filme = encontrado.filme
        self.raiz = self.remover(self.raiz, filme.media(), filme.nome)
        print(f"\nFilme '{nome}' removido com sucesso!")
    # ─────────────────────────────────────────
    # ADIÇÃO PÚBLICA (impede duplicatas por nome)
    
    def adicionar_filme(self, filme):
        if self.buscar_por_nome(self.raiz, filme.nome) is not None:
            print(f"Filme '{filme.nome}' já está cadastrado.")
            return False
        self.inserir(filme)
        return True
    # ─────────────────────────────────────────
    # AVALIAÇÃO
    # Remove o nó, adiciona a nota ao objeto e reinsere com a nova média — mantendo a BST consistente.
    
    def avaliar_filme(self, nome, nota):
        encontrado = self.buscar_por_nome(self.raiz, nome)
        if encontrado is None:
            print("Filme não encontrado.")
            return
        filme = encontrado.filme

        # Remove com a chave antiga (média atual)
        self.raiz = self.remover(self.raiz, filme.media(), filme.nome)

        # Adiciona a nova nota
        filme.notas.append(nota)

        # Reinsere com a nova chave (nova média)
        self.inserir(filme)

        estrelas = "★" * round(filme.media()) + "☆" * (5 - round(filme.media()))
        print(f"  Nota {nota} registrada! Média de '{filme.nome}': {filme.media():.2f} {estrelas}")
    # ─────────────────────────────────────────
    # COLETA EM ORDEM DECRESCENTE DE MÉDIA
    
    def _coletar_em_ordem(self, no, lista):
        """Percurso in-order invertido → lista do maior para o menor."""
        if no is not None:
            self._coletar_em_ordem(no.direita, lista)
            lista.append(no.filme)
            self._coletar_em_ordem(no.esquerda, lista)
    # ─────────────────────────────────────────
    # RANKING TOP N

    def ranking(self, limite=10):
        filmes = []
        self._coletar_em_ordem(self.raiz, filmes)

        if not filmes:
            print("Nenhum filme cadastrado.")
            return

        exibir = min(limite, len(filmes))
        print(f"\n{'='*58}")
        print(f"  🎬  TOP {exibir} FILMES")
        print(f"{'='*58}")
        print(f"  {'#':<4} {'Filme':<24} {'Média':<8} {'Votos':<8} {'Pop'}")
        print(f"  {'-'*54}")

        for i, filme in enumerate(filmes[:exibir], 1):
            media = filme.media()
            qtd   = len(filme.notas)
            estrelas = "★" * round(media) + "☆" * (5 - round(media))

            if qtd > 0:
                print(f"  {i:<4} {filme.nome:<24} {media:<6.2f} {estrelas}  {qtd:<8} {filme.pop}")
            else:
                print(f"  {i:<4} {filme.nome:<24} {'Sem avaliações':<20} {filme.pop}")

        print(f"{'='*58}")

def Menu():
    arv = Arvore_filmes()

    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar filme")
        print("2 - Ver ranking")
        print("3 - Remover filme")
        print("4 - Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            nome = input("Nome do filme: ").strip()
            if not nome:
                print("Nome inválido.")
                continue
            try:
                pop = int(input("Popularidade (número inteiro): "))
            except ValueError:
                print("Popularidade inválida.")
                continue

            if arv.adicionar_filme(Filme(nome, pop)):

                nota = float(input("Nota (1 a 5): "))
                if not (1 <= nota <= 5):
                    print("Nota inválida! Use um valor entre 1 e 5.")
                    continue
                nota = round(nota, 1)
            else:
                continue
            arv.avaliar_filme(nome, nota)
            
            print(f"   Filme '{nome}' adicionado com sucesso!")

        elif opcao == 2:
            try:
                entrada = input("Quantos filmes no ranking? (Enter = Top 10): ").strip()
                limite = int(entrada) if entrada else 10
                if limite <= 0:
                    print("Digite um número positivo.")
                    continue
            except ValueError:
                limite = 10
            arv.ranking(limite)

        elif opcao == 3:
            nome = input("Nome do filme a remover: ").strip()
            arv.remover_filme(nome)

        elif opcao == 4:
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


Menu()

