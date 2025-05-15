"""
Módulo de implementação de algoritmos de ordenação por inserção.

Este módulo contém implementações dos seguintes algoritmos de ordenação:
1. Insertion Sort (Ordenação por Inserção)
2. Shell Sort

Cada algoritmo é implementado com documentação detalhada, incluindo:
- Descrição do algoritmo
- Análise de complexidade
- Invariantes de laço para demonstração de corretude
- Exemplos de uso
"""

def insertion_sort(lista):
    """
    Implementação do algoritmo de ordenação por inserção (Insertion Sort).
    
    Este algoritmo constrói a lista ordenada um elemento por vez, inserindo cada
    novo elemento na posição correta. Funciona de maneira semelhante a como as
    pessoas ordenam cartas em um jogo de baralho.
    
    Invariante de laço:
    - A cada iteração i, os elementos em lista[0...i] estão ordenados entre si.
    
    Complexidade:
    - Tempo: O(n²) no pior e médio caso, O(n) no melhor caso (lista já ordenada)
    - Espaço: O(1), ordenação in-place
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Lista ordenada (a ordenação também é feita in-place)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> insertion_sort(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original é modificada
        [1, 2, 3, 4, 5]
    """
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        # Elemento a ser inserido na posição correta
        chave = lista[i]
        
        # Índice para comparação com elementos anteriores
        j = i - 1
        
        # Move elementos maiores que a chave uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insere a chave na posição correta
        lista[j + 1] = chave
    
    return lista


def shell_sort(lista):
    """
    Implementação do algoritmo Shell Sort.
    
    O Shell Sort é uma extensão do Insertion Sort que permite a troca de 
    elementos distantes, reduzindo gradualmente a distância entre os elementos
    a serem comparados. Isso torna o algoritmo muito mais eficiente que o 
    Insertion Sort para listas grandes.
    
    Este algoritmo usa a sequência de intervalos de Sedgewick, que oferece
    bom desempenho na prática.
    
    Invariante de laço:
    - Para cada intervalo h, cada sublista formada por elementos separados
      por h posições está ordenada ao final da passagem.
    
    Complexidade:
    - Tempo: Depende da sequência de intervalos, mas está entre O(n log² n) e O(n²)
    - Espaço: O(1), ordenação in-place
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Lista ordenada (a ordenação também é feita in-place)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> shell_sort(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original é modificada
        [1, 2, 3, 4, 5]
    """
    n = len(lista)
    
    # Inicializa o intervalo (gap) usando a sequência de Sedgewick
    # Esta é uma implementação simplificada, usando a sequência 2^k - 1
    intervalo = 1
    while intervalo < n // 3:
        intervalo = 3 * intervalo + 1
    
    # Diminui o intervalo até chegar a 1
    while intervalo >= 1:
        # Realiza insertion sort com o intervalo atual
        for i in range(intervalo, n):
            j = i
            temp = lista[i]
            
            # Insertion sort modificado para o intervalo atual
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            
            lista[j] = temp
        
        # Reduz o intervalo para a próxima iteração
        intervalo //= 3
    
    return lista


def insertion_sort_binario(lista):
    """
    Implementação do algoritmo de ordenação por inserção com busca binária.
    
    Esta variação do Insertion Sort usa a busca binária para encontrar a posição 
    correta de inserção, reduzindo o número de comparações necessárias.
    
    Invariante de laço:
    - A cada iteração i, os elementos em lista[0...i] estão ordenados entre si.
    
    Complexidade:
    - Tempo: O(n log n) para comparações, mas ainda O(n²) para movimentações
    - Espaço: O(1), ordenação in-place
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Lista ordenada (a ordenação também é feita in-place)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> insertion_sort_binario(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original é modificada
        [1, 2, 3, 4, 5]
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        
        # Usa busca binária para encontrar a posição correta
        left = 0
        right = i - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if lista[mid] < chave:
                left = mid + 1
            else:
                right = mid - 1
        
        # Posição correta para inserção é left
        # Desloca todos os elementos maiores que a chave
        for j in range(i, left, -1):
            lista[j] = lista[j - 1]
        
        # Insere a chave na posição correta
        lista[left] = chave
    
    return lista
