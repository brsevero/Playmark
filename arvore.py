class Filme:
    def __init__(self, nome, nota, pop): #pop = popularidade
        self.nome = nome
        self.nota = nota
        self.pop = pop

class no:
    def __init__(self, filme):
        self.filme = filme
        self.esquerda = None
        self.direita = None

class Arvore_filmes:
    def __init__(self):
        self.raiz = None

    def inserir(self, filme):
        novo = no(filme)

        if self.raiz == None:
            self.raiz = novo
            return
        atual = self.raiz

        while True:
            if filme.nota < atual.filme.nota:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita
    
    
    def mostrar_ranking(self):
        self._mostrar_ranking(self.raiz)

    def _mostrar_ranking(self, no):

        if no is not None:
            self._mostrar_ranking(no.direita)
            print(f"\nFilme: {no.filme.nome} | Nota: {no.filme.nota} | Popularidade: {no.filme.pop}\n")
            self._mostrar_ranking(no.esquerda)

def main():
    arv = Arvore_filmes()
    while True:

        print("\n===== MENU =====")
        print("1 - Adicionar filme")
        print("2 - Mostrar ranking")
        print("3 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:

            nome = input("Digite o nome do filme: ")
            nota = float(input("Nota do filme: "))
            pop = int(input("Popularidade do filme: "))

            filme = Filme(nome, nota, pop)
            arv.inserir(filme)
            print("Filme adicionado com sucesso!")

        elif opcao == 2:
            arv.mostrar_ranking()
        elif opcao == 3:
            break
            
main()

        
    