class Grafo:
    # Cada livro é um nó; uma aresta existe se dois livros foram emprestados juntos
    def __init__(self):
        self.livros = {}  # codigo_livro: set(codigos relacionados)

    def adicionar_livro(self, codigo):
        if codigo not in self.livros:
            self.livros[codigo] = set()

    def adicionar_relacao(self, codigo1, codigo2):
        self.adicionar_livro(codigo1)
        self.adicionar_livro(codigo2)
        self.livros[codigo1].add(codigo2)
        self.livros[codigo2].add(codigo1)

    def recomendar(self, codigo):
        # Retorna códigos dos livros relacionados ao fornecido
        return list(self.livros.get(codigo, []))