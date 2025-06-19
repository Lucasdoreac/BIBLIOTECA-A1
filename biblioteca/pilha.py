class Pilha:
    def __init__(self):
        self.itens = []
        
    def empilhar(self, item):
        self.itens.append(item)
        
    def desempilhar(self):
        return self.itens.pop() if self.itens else None
        
    def vazio(self):
        return len(self.itens) == 0
        
    def topo(self):
        return self.itens[-1] if self.itens else None
        
    def __len__(self):
        return len(self.itens)