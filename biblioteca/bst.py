class NodoBST:
    def __init__(self, livro):
        self.livro = livro
        self.esq = None
        self.dir = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, livro):
        def _inserir(raiz, livro):
            if not raiz:
                return NodoBST(livro)
            if livro.titulo < raiz.livro.titulo:
                raiz.esq = _inserir(raiz.esq, livro)
            else:
                raiz.dir = _inserir(raiz.dir, livro)
            return raiz
        self.raiz = _inserir(self.raiz, livro)

    def buscar(self, titulo):
        def _buscar(raiz, titulo):
            if not raiz:
                return None
            if raiz.livro.titulo == titulo:
                return raiz.livro
            if titulo < raiz.livro.titulo:
                return _buscar(raiz.esq, titulo)
            else:
                return _buscar(raiz.dir, titulo)
        return _buscar(self.raiz, titulo)

    def em_ordem(self, raiz=None, lista=None):
        if lista is None:
            lista = []
        if raiz is None:
            raiz = self.raiz
        if raiz is not None:
            self.em_ordem(raiz.esq, lista)
            lista.append(raiz.livro)
            self.em_ordem(raiz.dir, lista)
        return lista