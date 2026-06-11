import os
from Lista_Encadeada import CatalogoFilmes
from arvore import Arvore_filmes, Filmes
from fila import FilaFavoritos

#Variaveis globais
catalogo = CatalogoFilmes()
arv_ranking = Arvore_filmes()
fila = FilaFavoritos()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")


# ============================================================
# FUNÇÕES (a serem implementadas depois com as estruturas)
# ============================================================

# 1. Biblioteca de filmes (lista encadeada)
def cadastrar_filme():
    print("Insira o nome do filme:")
    titulo = input()
    print("Insira o genero do filme:")
    genero = input()
    catalogo.adicionar_filme(titulo,genero)


def listar_filmes():
    catalogo.exibir_catalogo()


# 3. Lista de favoritos (fila)
def adicionar_favorito():
    print("Insira o nome do filme:")
    titulo = input()
    fila.adicionar_favorito(titulo)

def listar_favoritos():
    fila.listar_favoritos()

def remover_favorito():
    print("Insira o nome do filme:")
    titulo = input()
    fila.remover_favorito(titulo)


# 4. Categorização por gênero (grafo)
def associar_genero():
    print("\n[Associar Genero] -> implementar com GRAFO")

def listar_conexoes_genero():
    print("\n[Conexoes por Genero] -> implementar com GRAFO")


# 5. Histórico de visualização (hash table / dict)
def registrar_historico():
    print("\n[Registrar Historico] -> implementar com HASH TABLE (dict)")

def buscar_historico():
    print("\n[Buscar no Historico] -> implementar com HASH TABLE (dict)")


# 6. Comentários personalizados
def adicionar_comentario():
    print("\n[Adicionar Comentario] -> implementar (entidade Filme)")

def exibir_comentarios():
    print("\n[Exibir Comentarios] -> implementar (entidade Filme)")


# ============================================================
# SUBMENUS
# ============================================================

def menu_filmes():
    while True:
        limpar_tela()
        print("=========================================")
        print("        BIBLIOTECA DE FILMES")
        print("=========================================")
        print("1 - Cadastrar novo filme")
        print("2 - Listar todos os filmes")
        print("0 - Voltar")
        print("-----------------------------------------")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_filme()
            pausar()
        elif opcao == "2":
            listar_filmes()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
            pausar()


def menu_avaliacoes():
    while True:
        limpar_tela()
        arv_ranking.Menu()
        break

def menu_favoritos():
    while True:
        limpar_tela()
        print("=========================================")
        print("        LISTA DE FAVORITOS")
        print("=========================================")
        print("1 - Adicionar filme aos favoritos")
        print("2 - Listar favoritos")
        print("3 - Remover filme dos favoritos")
        print("0 - Voltar")
        print("-----------------------------------------")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            adicionar_favorito()
            pausar()
        elif opcao == "2":
            listar_favoritos()
            pausar()
        elif opcao == "3":
            remover_favorito()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
            pausar()


def menu_generos():
    while True:
        limpar_tela()
        print("=========================================")
        print("        CATEGORIZACAO POR GENERO")
        print("=========================================")
        print("1 - Associar genero(s) a um filme")
        print("2 - Listar conexoes entre filmes (grafo)")
        print("0 - Voltar")
        print("-----------------------------------------")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            associar_genero()
            pausar()
        elif opcao == "2":
            listar_conexoes_genero()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
            pausar()


def menu_historico():
    while True:
        limpar_tela()
        print("=========================================")
        print("        HISTORICO DE VISUALIZACAO")
        print("=========================================")
        print("1 - Registrar filme assistido")
        print("2 - Buscar filme no historico")
        print("0 - Voltar")
        print("-----------------------------------------")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            registrar_historico()
            pausar()
        elif opcao == "2":
            buscar_historico()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
            pausar()


def menu_comentarios():
    while True:
        limpar_tela()
        print("=========================================")
        print("        COMENTARIOS")
        print("=========================================")
        print("1 - Adicionar comentario a um filme")
        print("2 - Exibir comentarios de um filme")
        print("0 - Voltar")
        print("-----------------------------------------")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            adicionar_comentario()
            pausar()
        elif opcao == "2":
            exibir_comentarios()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")
            pausar()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal():
    while 1:
        limpar_tela()
        
        print("#########################################")
        print("#                PLAYMARK               #")
        print("#########################################")
        print("1 - Biblioteca de Filmes")
        print("2 - Avaliacoes e Ranking")
        print("3 - Lista de Favoritos")
        print("4 - Categorizacao por Genero")
        print("5 - Historico de Visualizacao")
        print("6 - Comentarios")
        print("0 - Sair")
        print("-----------------------------------------")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            menu_filmes()
        elif opcao == "2":
            menu_avaliacoes()
        elif opcao == "3":
            menu_favoritos()
        elif opcao == "4":
            menu_generos()
        elif opcao == "5":
            menu_historico()
        elif opcao == "6":
            menu_comentarios()
        elif opcao == "0":
            print("Saindo... ate logo!")
            break
        else:
            print("Opcao invalida!")
            pausar()


if __name__ == "__main__":
    menu_principal()