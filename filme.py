from comentario import Comentario

class Filme:
    """Representa a entidade Filme (e também o nó da lista encadeada)."""
    
    def __init__(self, titulo, genero, avaliacao):
        self.titulo = titulo
        self.genero = genero
        
        # Iniciamos com 0 e chamamos o método avaliar para validar a nota inicial
        self.avaliacao = 0
        self.avaliar(avaliacao)
        
        self.comentarios_head = None
        self.proximo = None  # Ponteiro para o próximo filme na lista

    def avaliar(self, nova_nota):
        """Define ou atualiza a nota do filme, garantindo que esteja entre 0 e 10."""
        try:
            # Tenta converter o input para float (caso venha como string do terminal)
            nota_convertida = float(nova_nota)
        except (ValueError, TypeError):
            raise ValueError("A avaliação deve ser um número válido (inteiro ou decimal).")

        # Garante o limite estipulado no método __str__ (Nota: X/10)
        if nota_convertida < 0 or nota_convertida > 10:
            raise ValueError("A nota do filme deve ser um valor entre 0 e 10.")

        # Arredonda para uma casa decimal (ex: 8.56 vira 8.6)
        self.avaliacao = round(nota_convertida, 1)

    def adicionar_comentario(self, novo_comentario: Comentario):
        """Adiciona um comentário no final da lista encadeada do filme."""
        if self.comentarios_head is None:
            # Se a lista estiver vazia, este é o primeiro comentário
            self.comentarios_head = novo_comentario
        else:
            # Percorre a lista até achar o último nó
            atual = self.comentarios_head
            while atual.proximo_comentario is not None:
                atual = atual.proximo_comentario
            
            # Adiciona o novo comentário ao final
            atual.proximo_comentario = novo_comentario

    def __str__(self):
        return (f"Título: {self.titulo} | Gênero: {self.genero} | "
                f"Nota: {self.avaliacao}/10\n")
    
    def exibir_comentarios(self):
        """Percorre a lista encadeada e exibe todos os comentários."""
        print(f"\n===== COMENTÁRIOS: {self.titulo.upper()} =====")
        
        atual = self.comentarios_head
        if atual is None:
            print("Nenhum comentário registrado ainda.")
        else:
            while atual is not None:
                print(atual)
                atual = atual.proximo_comentario
        print("=" * (19 + len(self.titulo)))