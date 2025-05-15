"""
Módulo de implementação de hashing e mapa.

Este módulo contém:
1. Funções hash para diferentes tipos de dados
2. Implementação do tipo abstrato de dado mapa (map) usando hashing

Este módulo mostra como o hashing pode ser usado como uma técnica eficiente de busca,
permitindo acesso quase instantâneo aos dados, independentemente do tamanho da coleção.
"""

class HashMap:
    """
    Implementação do tipo abstrato de dado mapa (map) usando hashing.
    
    Um mapa é uma estrutura de dados que armazena pares chave-valor, onde cada
    chave é única. Esta implementação usa hashing para obter acesso eficiente
    aos dados.
    
    Esta implementação utiliza o método de tratamento de colisões por encadeamento,
    onde cada posição da tabela hash contém uma lista de pares chave-valor.
    
    Complexidade:
    - Tempo: O(1) em média para operações de busca, inserção e remoção
             O(n) no pior caso (quando há muitas colisões)
    - Espaço: O(n), onde n é o número de pares chave-valor
    
    Exemplos:
        >>> m = HashMap(10)
        >>> m.inserir("chave1", "valor1")
        >>> m.inserir("chave2", "valor2")
        >>> m.buscar("chave1")
        'valor1'
        >>> m.remover("chave1")
        >>> m.buscar("chave1")
        None
    """
    
    def __init__(self, tamanho=1024):
        """
        Inicializa um novo mapa com o tamanho especificado.
        
        Args:
            tamanho: Tamanho da tabela hash (padrão = 1024)
        """
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.qtd_elementos = 0
        # Fator de carga máximo antes de redimensionar
        self.fator_carga_max = 0.75
    
    def _hash(self, chave):
        """
        Função hash que converte uma chave em um índice da tabela.
        
        Esta implementação usa a função hash nativa do Python e aplica
        o operador módulo para garantir que o índice esteja dentro dos
        limites da tabela.
        
        Args:
            chave: A chave a ser hashada
            
        Returns:
            Índice na tabela hash
        """
        return hash(chave) % self.tamanho
    
    def inserir(self, chave, valor):
        """
        Insere um par chave-valor no mapa.
        
        Se a chave já existir, o valor será atualizado.
        
        Args:
            chave: A chave para o par
            valor: O valor para o par
        """
        indice = self._hash(chave)
        
        # Verifica se a chave já existe
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                # Atualiza o valor
                self.tabela[indice][i] = (chave, valor)
                return
        
        # Chave não existe, adiciona o par
        self.tabela[indice].append((chave, valor))
        self.qtd_elementos += 1
        
        # Verifica se precisa redimensionar
        if self.qtd_elementos / self.tamanho > self.fator_carga_max:
            self._redimensionar()
    
    def buscar(self, chave):
        """
        Busca um valor associado à chave especificada.
        
        Args:
            chave: A chave a ser buscada
            
        Returns:
            O valor associado à chave, ou None se a chave não existir
        """
        indice = self._hash(chave)
        
        # Busca a chave na lista de pares naquele índice
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        
        # Chave não encontrada
        return None
    
    def remover(self, chave):
        """
        Remove um par chave-valor do mapa.
        
        Args:
            chave: A chave do par a ser removido
            
        Returns:
            True se a chave foi removida, False se a chave não existia
        """
        indice = self._hash(chave)
        
        # Busca a chave na lista de pares naquele índice
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                # Remove o par
                del self.tabela[indice][i]
                self.qtd_elementos -= 1
                return True
        
        # Chave não encontrada
        return False
    
    def _redimensionar(self):
        """
        Redimensiona a tabela hash quando o fator de carga excede o limite.
        
        Esta operação dobra o tamanho da tabela e rehasheia todos os elementos.
        """
        # Armazena a tabela antiga
        tabela_antiga = self.tabela
        
        # Dobra o tamanho e cria uma nova tabela vazia
        self.tamanho *= 2
        self.tabela = [[] for _ in range(self.tamanho)]
        self.qtd_elementos = 0
        
        # Reinsere todos os elementos
        for lista in tabela_antiga:
            for chave, valor in lista:
                self.inserir(chave, valor)
    
    def __contains__(self, chave):
        """
        Verifica se uma chave existe no mapa.
        
        Esta implementação permite usar o operador 'in' com o mapa.
        
        Args:
            chave: A chave a ser verificada
            
        Returns:
            True se a chave existir, False caso contrário
        """
        return self.buscar(chave) is not None
    
    def __getitem__(self, chave):
        """
        Obtém o valor associado à chave especificada.
        
        Esta implementação permite usar a sintaxe mapa[chave].
        
        Args:
            chave: A chave do valor a ser obtido
            
        Returns:
            O valor associado à chave
            
        Raises:
            KeyError: Se a chave não existir
        """
        valor = self.buscar(chave)
        if valor is None:
            raise KeyError(chave)
        return valor
    
    def __setitem__(self, chave, valor):
        """
        Define ou atualiza o valor associado à chave especificada.
        
        Esta implementação permite usar a sintaxe mapa[chave] = valor.
        
        Args:
            chave: A chave do valor a ser definido
            valor: O valor a ser associado à chave
        """
        self.inserir(chave, valor)
    
    def __delitem__(self, chave):
        """
        Remove o par chave-valor associado à chave especificada.
        
        Esta implementação permite usar a sintaxe del mapa[chave].
        
        Args:
            chave: A chave do par a ser removido
            
        Raises:
            KeyError: Se a chave não existir
        """
        if not self.remover(chave):
            raise KeyError(chave)
    
    def __len__(self):
        """
        Retorna o número de pares chave-valor no mapa.
        
        Esta implementação permite usar a função len() com o mapa.
        
        Returns:
            O número de pares chave-valor no mapa
        """
        return self.qtd_elementos
    
    def __str__(self):
        """
        Retorna uma representação string do mapa.
        
        Returns:
            Uma string representando o mapa
        """
        itens = []
        for lista in self.tabela:
            itens.extend(lista)
        
        return "{" + ", ".join(f"{repr(k)}: {repr(v)}" for k, v in itens) + "}"
    
    def obter_chaves(self):
        """
        Retorna uma lista com todas as chaves do mapa.
        
        Returns:
            Lista de chaves
        """
        chaves = []
        for lista in self.tabela:
            for k, _ in lista:
                chaves.append(k)
        return chaves
    
    def obter_valores(self):
        """
        Retorna uma lista com todos os valores do mapa.
        
        Returns:
            Lista de valores
        """
        valores = []
        for lista in self.tabela:
            for _, v in lista:
                valores.append(v)
        return valores
    
    def obter_itens(self):
        """
        Retorna uma lista com todos os pares chave-valor do mapa.
        
        Returns:
            Lista de tuplas (chave, valor)
        """
        itens = []
        for lista in self.tabela:
            itens.extend(lista)
        return itens


class HashMapEndAberto:
    """
    Implementação alternativa do HashMap usando endereçamento aberto.
    
    No endereçamento aberto, quando ocorre uma colisão, busca-se outra posição
    na tabela seguindo uma estratégia de sondagem. Esta implementação usa a
    sondagem linear.
    
    Complexidade:
    - Tempo: O(1) em média para operações de busca, inserção e remoção
             O(n) no pior caso (quando há muitas colisões)
    - Espaço: O(n), onde n é o número de pares chave-valor
    """
    
    # Constante usada para marcar posições que já tiveram elementos, mas foram removidos
    REMOVIDO = object()
    
    def __init__(self, tamanho=1024):
        """
        Inicializa um novo mapa com o tamanho especificado.
        
        Args:
            tamanho: Tamanho da tabela hash (padrão = 1024)
        """
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.qtd_elementos = 0
        # Fator de carga máximo antes de redimensionar (menor para endereçamento aberto)
        self.fator_carga_max = 0.5
    
    def _hash(self, chave):
        """
        Função hash que converte uma chave em um índice da tabela.
        
        Args:
            chave: A chave a ser hashada
            
        Returns:
            Índice na tabela hash
        """
        return hash(chave) % self.tamanho
    
    def _sondagem_linear(self, indice_base, i):
        """
        Função de sondagem linear para resolver colisões.
        
        Args:
            indice_base: Índice hash original
            i: Tentativa atual de sondagem
            
        Returns:
            Próximo índice a ser tentado
        """
        return (indice_base + i) % self.tamanho
    
    def inserir(self, chave, valor):
        """
        Insere um par chave-valor no mapa.
        
        Se a chave já existir, o valor será atualizado.
        
        Args:
            chave: A chave para o par
            valor: O valor para o par
        """
        # Verifica se precisa redimensionar
        if self.qtd_elementos / self.tamanho > self.fator_carga_max:
            self._redimensionar()
        
        indice_base = self._hash(chave)
        
        # Tenta encontrar uma posição para inserir
        i = 0
        while i < self.tamanho:
            indice = self._sondagem_linear(indice_base, i)
            
            # Posição vazia ou marcada como removida
            if self.tabela[indice] is None or self.tabela[indice] is self.REMOVIDO:
                self.tabela[indice] = (chave, valor)
                self.qtd_elementos += 1
                return
            
            # Chave já existe, atualiza o valor
            if self.tabela[indice][0] == chave:
                self.tabela[indice] = (chave, valor)
                return
            
            i += 1
        
        # Tabela está cheia (não deveria acontecer devido ao redimensionamento)
        raise OverflowError("Tabela hash está cheia")
    
    def buscar(self, chave):
        """
        Busca um valor associado à chave especificada.
        
        Args:
            chave: A chave a ser buscada
            
        Returns:
            O valor associado à chave, ou None se a chave não existir
        """
        indice_base = self._hash(chave)
        
        # Tenta encontrar a chave
        i = 0
        while i < self.tamanho:
            indice = self._sondagem_linear(indice_base, i)
            
            # Posição vazia, a chave não existe
            if self.tabela[indice] is None:
                return None
            
            # Posição marcada como removida, continua a busca
            if self.tabela[indice] is self.REMOVIDO:
                i += 1
                continue
            
            # Chave encontrada
            if self.tabela[indice][0] == chave:
                return self.tabela[indice][1]
            
            i += 1
        
        # Chave não encontrada
        return None
    
    def remover(self, chave):
        """
        Remove um par chave-valor do mapa.
        
        Args:
            chave: A chave do par a ser removido
            
        Returns:
            True se a chave foi removida, False se a chave não existia
        """
        indice_base = self._hash(chave)
        
        # Tenta encontrar a chave
        i = 0
        while i < self.tamanho:
            indice = self._sondagem_linear(indice_base, i)
            
            # Posição vazia, a chave não existe
            if self.tabela[indice] is None:
                return False
            
            # Posição marcada como removida, continua a busca
            if self.tabela[indice] is self.REMOVIDO:
                i += 1
                continue
            
            # Chave encontrada
            if self.tabela[indice][0] == chave:
                self.tabela[indice] = self.REMOVIDO
                self.qtd_elementos -= 1
                return True
            
            i += 1
        
        # Chave não encontrada
        return False
    
    def _redimensionar(self):
        """
        Redimensiona a tabela hash quando o fator de carga excede o limite.
        
        Esta operação dobra o tamanho da tabela e rehasheia todos os elementos.
        """
        # Armazena a tabela antiga
        tabela_antiga = self.tabela
        
        # Dobra o tamanho e cria uma nova tabela vazia
        self.tamanho *= 2
        self.tabela = [None] * self.tamanho
        self.qtd_elementos = 0
        
        # Reinsere todos os elementos
        for item in tabela_antiga:
            if item is not None and item is not self.REMOVIDO:
                chave, valor = item
                self.inserir(chave, valor)
    
    # Os métodos __contains__, __getitem__, __setitem__, __delitem__, __len__,
    # __str__, obter_chaves, obter_valores e obter_itens são similares aos da 
    # classe HashMap e são omitidos para brevidade
