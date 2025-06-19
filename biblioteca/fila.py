class Fila:
    def __init__(self):
        self.itens = []
        
    def enfileirar(self, item):
        self.itens.append(item)
        
    def desenfileirar(self):
        return self.itens.pop(0) if self.itens else None
        
    def vazio(self):
        return len(self.itens) == 0
        
    def primeiro(self):
        return self.itens[0] if self.itens else None
        
    def __len__(self):
        return len(self.itens)