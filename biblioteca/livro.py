class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.fila_espera = []

    def __str__(self):
        return f"{self.titulo} ({self.autor}) [Código: {self.codigo}]"