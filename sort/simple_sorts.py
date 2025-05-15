"""
Módulo de implementação de algoritmos de ordenação simples.

Este módulo contém implementações dos seguintes algoritmos de ordenação:
1. Selection Sort (Ordenação por Seleção)
2. Bubble Sort (Ordenação por Bolha)

Cada algoritmo é implementado com documentação detalhada, incluindo:
- Descrição do algoritmo
- Análise de complexidade
- Invariantes de laço para demonstração de corretude
- Exemplos de uso
"""

def selection_sort(lista):
    """
    Implementação do algoritmo de ordenação por seleção (Selection Sort).
    
    Este algoritmo divide a lista em duas partes: uma parte ordenada no início
    e uma parte não ordenada no final. A cada iteração, o algoritmo encontra o
    menor elemento na parte não ordenada e o coloca na posição correta na parte ordenada.
    
    Invariante de laço:
    - A cada iteração i, os elementos em lista[0...i-1] estão ordenados e são
      os i menores elementos da lista original.
    
    Complexidade:
    - Tempo: O(n²) no pior, médio e melhor caso, onde n é o tamanho da lista
    - Espaço: O(1), ordenação in-place
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Lista ordenada (a ordenação também é feita in-place)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> selection_sort(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original é modificada
        [1, 2, 3, 4, 5]
    """
    # Obtém o tamanho da lista
    n = len(lista)
    
    # Percorre a lista
    for i in range(n):
        # Encontra o índice do menor elemento na parte não ordenada
        indice_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        
        # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    
    return lista


def bubble_sort(lista):
    """
    Implementação do algoritmo de ordenação bolha (Bubble Sort).
    
    Este algoritmo percorre repetidamente a lista, comparando pares de elementos
    adjacentes e trocando-os se estiverem na ordem errada. A cada iteração, o
    maior elemento "borbulha" para o final da lista.
    
    Invariante de laço:
    - A cada iteração i, os i maiores elementos estão ordenados e em suas
      posições finais no final da lista.
    
    Complexidade:
    - Tempo: O(n²) no pior e médio caso, O(n) no melhor caso (lista já ordenada)
    - Espaço: O(1), ordenação in-place
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Lista ordenada (a ordenação também é feita in-place)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> bubble_sort(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original é modificada
        [1, 2, 3, 4, 5]
    """
    # Obtém o tamanho da lista
    n = len(lista)
    
    # Flag para otimização: indica se houve troca na última passagem
    troca_realizada = True
    
    # Contador de iterações
    iteracao = 0
    
    # Continua enquanto houver trocas
    while troca_realizada and iteracao < n:
        # Assume que não haverá trocas nesta passagem
        troca_realizada = False
        
        # Percorre a lista até o final não ordenado
        for j in range(0, n - iteracao - 1):
            # Compara elementos adjacentes
            if lista[j] > lista[j + 1]:
                # Realiza a troca
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Marca que houve troca
                troca_realizada = True
        
        # Incrementa o contador de iterações
        iteracao += 1
    
    return lista


def bubble_sort_otimizado(lista):
    """
    Implementação otimizada do algoritmo de ordenação bolha (Bubble Sort).
    
    Esta versão inclui duas otimizações:
    1. Parada quando nenhuma troca é realizada em uma passagem completa
    2. Redução do tamanho da parte não ordenada a cada iteração
    
    Invariante de laço:
    - A cada iteração i, os i maiores elementos estão ordenados e em suas
      posições finais no final da lista.
    
    Complexidade:
    - Tempo: O(n²) no pior e médio caso, O(n) no melhor caso (lista já ordenada)
    - Espaço: O(1), ordenação in-place
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Lista ordenada (a ordenação também é feita in-place)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> bubble_sort_otimizado(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original é modificada
        [1, 2, 3, 4, 5]
    """
    # Obtém o tamanho da lista
    n = len(lista)
    
    # Inicializa a variável que armazena a posição da última troca
    ultima_troca = n - 1
    
    # Continua enquanto houver trocas
    while ultima_troca > 0:
        # Armazena a posição da última troca nesta passagem
        posicao_ultima_troca = 0
        
        # Percorre a lista até a posição da última troca na passagem anterior
        for j in range(0, ultima_troca):
            # Compara elementos adjacentes
            if lista[j] > lista[j + 1]:
                # Realiza a troca
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Marca a posição da última troca
                posicao_ultima_troca = j
        
        # Atualiza a posição da última troca para a próxima passagem
        ultima_troca = posicao_ultima_troca
    
    return lista
