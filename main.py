from pessoa import Pessoa
from filme import Filme
from comentario import Comentario

print("===== INICIANDO SISTEMA PLAY MARK =====\n")

user1 = Pessoa(1, "Lucas Medeiros", "2000-05-12", "Masculino", "Usuário")
user2 = Pessoa(2, "Beatriz Souza", "1998-11-23", "feminino", "u s u a r i o")
diretor = Pessoa(3, "Christopher Nolan", "1970-07-30", "Masculino", "Diretor")


filme = Filme("Interestelar", "Ficção Científica", 8.5)
print("--- Estado Inicial do Filme ---")
print(filme)


print("--- Atualizando a Avaliação do Filme ---")
filme.avaliar(9.8)
print(filme)

# Teste de segurança da avaliação (Evitando notas absurdas)
try:
    filme.avaliar(12.5)  # Nota maior que 10
except ValueError as e:
    print(f"[Bloqueio de Nota Invalida]: {e}\n")


# 4. Criando e inserindo os comentários na lista encadeada
try:
    c1 = Comentario(1, user1, "A trilha sonora é de chorar. Obra-prima!")
    c2 = Comentario(2, user2, "Achei confuso no final, mas a fotografia é linda.")
    
    # Inserindo na lista encadeada do filme
    filme.adicionar_comentario(c1)
    filme.adicionar_comentario(c2)
    
except ValueError as e:
    print(f"Erro ao criar comentário: {e}")

filme.exibir_comentarios()


# 6. Testando a barreira de segurança de perfil (Diretor tentando comentar)
try:
    c3 = Comentario(3, diretor, "Obrigado por assistirem ao meu filme!")
    filme.adicionar_comentario(c3)
except ValueError as e:
    print(f"\n[Bloqueio de Segurança Funcional]: {e}")