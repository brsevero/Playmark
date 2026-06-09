class Filme:
    """Representa a entidade Filme (e também o nó da lista encadeada)."""
    
    def __init__(self, titulo, genero, avaliacao, comentarios):
        self.titulo = titulo
        self.genero = genero
        self.avaliacao = avaliacao
        self.comentarios = comentarios
        self.proximo = None  # Ponteiro para o próximo filme na lista

    def __str__(self):
        return (f"Título: {self.titulo} | Gênero: {self.genero} | "
                f"Nota: {self.avaliacao}/10\n"
                f"   Comentários: {self.comentarios}")