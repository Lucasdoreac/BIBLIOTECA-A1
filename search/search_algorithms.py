"""
Módulo de implementação de algoritmos de busca.

Este módulo contém implementações dos seguintes algoritmos de busca:
1. Busca Sequencial (Linear Search)
2. Busca Binária (Binary Search)

Cada algoritmo é implementado com documentação detalhada, incluindo:
- Descrição do algoritmo
- Análise de complexidade
- Invariantes de laço para demonstração de corretude
- Exemplos de uso
"""

def busca_sequencial(lista, item):
    """
    Implementação do algoritmo de busca sequencial (linear search).
    
    Este algoritmo percorre a lista sequencialmente do início ao fim,
    comparando cada elemento com o item procurado.
    
    Invariante de laço:
    - A cada iteração, todos os elementos em lista[0...i-1] são diferentes de item.
    
    Complexidade:
    - Tempo: O(n) no pior caso, onde n é o tamanho da lista
    - Espaço: O(1)
    
    Args:
        lista: Lista de elementos a ser pesquisada
        item: Elemento a ser procurado na lista
        
    Returns:
        Índice do elemento se encontrado, -1 caso contrário
    
    Exemplos:
        >>> busca_sequencial([1, 2, 3, 4, 5], 3)
        2
        >>> busca_sequencial([1, 2, 3, 4, 5], 6)
        -1
    """
    # Percorre cada elemento da lista
    for i in range(len(lista)):
        # Compara o elemento atual com o item procurado
        if lista[i] == item:
            return i  # Retorna o índice onde o item foi encontrado
    
    # Retorna -1 se o item não for encontrado
    return -1


def busca_binaria(lista, item):
    """
    Implementação do algoritmo de busca binária (binary search).
    
    Este algoritmo requer que a lista esteja ordenada. Ele divide repetidamente
    pela metade o espaço de busca, comparando o item procurado com o elemento
    no meio da lista.
    
    Invariante de laço:
    - Se o item existe na lista, então está no intervalo lista[inicio...fim].
    
    Complexidade:
    - Tempo: O(log n) no pior caso, onde n é o tamanho da lista
    - Espaço: O(1) para implementação iterativa, O(log n) para recursiva
    
    Args:
        lista: Lista ordenada de elementos a ser pesquisada
        item: Elemento a ser procurado na lista
        
    Returns:
        Índice do elemento se encontrado, -1 caso contrário
    
    Exemplos:
        >>> busca_binaria([1, 2, 3, 4, 5], 3)
        2
        >>> busca_binaria([1, 2, 3, 4, 5], 6)
        -1
    """
    # Inicializa os índices que definem os limites da busca
    inicio = 0
    fim = len(lista) - 1
    
    # Enquanto houver espaço de busca
    while inicio <= fim:
        # Calcula o índice do meio
        meio = (inicio + fim) // 2
        
        # Se o elemento do meio for o item procurado, retorna o índice
        if lista[meio] == item:
            return meio
        
        # Se o elemento do meio for maior que o item, busca na metade inferior
        elif lista[meio] > item:
            fim = meio - 1
        
        # Se o elemento do meio for menor que o item, busca na metade superior
        else:
            inicio = meio + 1
    
    # Retorna -1 se o item não for encontrado
    return -1


def busca_binaria_recursiva(lista, item, inicio=None, fim=None):
    """
    Implementação recursiva do algoritmo de busca binária.
    
    Esta é uma implementação alternativa da busca binária utilizando recursão.
    
    Invariante de laço:
    - A cada chamada recursiva, se o item existe na lista, então está no 
      intervalo lista[inicio...fim].
    
    Complexidade:
    - Tempo: O(log n) no pior caso, onde n é o tamanho da lista
    - Espaço: O(log n) devido à pilha de chamadas recursivas
    
    Args:
        lista: Lista ordenada de elementos a ser pesquisada
        item: Elemento a ser procurado na lista
        inicio: Índice inicial para a busca (padrão = 0)
        fim: Índice final para a busca (padrão = len(lista) - 1)
        
    Returns:
        Índice do elemento se encontrado, -1 caso contrário
    """
    # Inicializa os índices na primeira chamada
    if inicio is None:
        inicio = 0
    if fim is None:
        fim = len(lista) - 1
    
    # Caso base: espaço de busca vazio
    if inicio > fim:
        return -1
    
    # Calcula o índice do meio
    meio = (inicio + fim) // 2
    
    # Verifica se o elemento do meio é o item procurado
    if lista[meio] == item:
        return meio
    
    # Busca recursivamente na metade inferior
    elif lista[meio] > item:
        return busca_binaria_recursiva(lista, item, inicio, meio - 1)
    
    # Busca recursivamente na metade superior
    else:
        return busca_binaria_recursiva(lista, item, meio + 1, fim)
