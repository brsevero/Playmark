class Filme:
    def __init__(self, nome, nota, pop): #pop = popularidade
        self.nome = nome
        self.nota = nota
        self.pop = pop

class No:
    def __init__(self, filme):
        self.filme = filme
        self.esquerda = None
        self.direita = None

class Arvore_filmes():
    def __init__(self):
        self.raiz = None

    def inserir(self, filme):
        novo = No(filme)

        if self.raiz is None:
            self.raiz = novo
            return
        atual = self.raiz

        while True:
            if (filme.nota , filme.nome) < (atual.filme.nota , atual.filme.nome):
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita
    
    
    def ranking(self, no):
        
        if no is not None:
            self.ranking(no.direita)
            print(f"\nFilme: {no.filme.nome} | Nota: {no.filme.nota} | Popularidade: {no.filme.pop}\n")
            self.ranking(no.esquerda)

    def remover(self, no, nota, nome):
        if no is None:
            return None

        chave = (nota, nome)

        chave_atual = (
            no.filme.nota,
            no.filme.nome
        )

        # VAI PARA ESQUERDA
        if chave < chave_atual:

            no.esquerda = self.remover(
                no.esquerda,
                nota,
                nome
            )

        # VAI PARA DIREITA
        elif chave > chave_atual:

            no.direita = self.remover(
                no.direita,
                nota,
                nome
            )

        else:

            if no.esquerda is None:
                return no.direita

            elif no.direita is None:
                return no.esquerda


            # DOIS FILHOS

            temp = no.direita
          
            while temp.esquerda is not None:      # anda para a esquerda
                temp = temp.esquerda

            no.filme = temp.filme        # substitui o filme

            no.direita = self.remover(      # remove o duplicado
                no.direita,
                temp.filme.nota,
                temp.filme.nome)
            
        return no

    def buscar_por_nome(self, no, nome):

        if no is None:
            return None

        if no.filme.nome.lower() == nome.lower():
            return no

        encontrado = self.buscar_por_nome(
            no.esquerda,
            nome)
        
        if encontrado:
            return encontrado

        return self.buscar_por_nome(
            no.direita,
            nome )

    def remover_filme(self, nome):

        encontrado = self.buscar_por_nome(
            self.raiz,
            nome)

        if encontrado is None:

            print("Filme não encontrado.")
            return

        self.raiz = self.remover(
            self.raiz,
            encontrado.filme.nota,
            encontrado.filme.nome)

        print("Filme removido com sucesso!")

def Menu():
    arv = Arvore_filmes()
    while True:

        print("\n===== MENU =====")
        print("1 - Adicionar filme")
        print("2 - Mostrar ranking")
        print("3 - Remover Filme")
        print("4 - Sair")

        try:   
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:

            nome = input("Digite o nome do filme: ")
            nota = float(input("Nota do filme: "))
            pop = int(input("Popularidade do filme: "))

            filme = Filme(nome, nota, pop)
            arv.inserir(filme)
            print("Filme adicionado com sucesso!")

        elif opcao == 2:
            if arv.raiz is None:
                print("Nenhum filme cadastrado.")
            else:
                arv.ranking(arv.raiz)
        elif opcao == 3:
            nome = input("\nDigite o nome do Filme que quer remover: ")

            arv.remover_filme(nome)
        elif opcao == 4:
            break
            
Menu()
