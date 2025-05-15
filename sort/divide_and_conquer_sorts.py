"""
Módulo de implementação de algoritmos de ordenação por divisão e conquista.

Este módulo contém implementações dos seguintes algoritmos de ordenação:
1. Merge Sort
2. Quick Sort

Cada algoritmo é implementado com documentação detalhada, incluindo:
- Descrição do algoritmo
- Análise de complexidade
- Invariantes de laço para demonstração de corretude
- Exemplos de uso
"""

def merge_sort(lista):
    """
    Implementação do algoritmo de ordenação por mesclagem (Merge Sort).
    
    Este algoritmo usa a estratégia de divisão e conquista: divide a lista pela
    metade recursivamente até ter sublistas de tamanho 1, ordena essas sublistas
    e depois as mescla de volta em uma única lista ordenada.
    
    Invariante de algoritmo:
    - A função merge sempre mescla duas listas ordenadas em uma única lista ordenada.
    
    Complexidade:
    - Tempo: O(n log n) no pior, médio e melhor caso
    - Espaço: O(n), requer espaço adicional
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Nova lista ordenada (a lista original não é modificada)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> merge_sort(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original não é modificada
        [5, 3, 1, 4, 2]
    """
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista[:]
    
    # Divide a lista pela metade
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Recursivamente ordena as duas metades
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)
    
    # Mescla as duas metades ordenadas
    return mesclar(esquerda_ordenada, direita_ordenada)


def mesclar(esquerda, direita):
    """
    Função auxiliar para mesclar duas listas ordenadas.
    
    Args:
        esquerda: Primeira lista ordenada
        direita: Segunda lista ordenada
        
    Returns:
        Lista mesclada e ordenada
    """
    resultado = []
    i = j = 0
    
    # Mescla elementos comparando os próximos de cada lista
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado


def merge_sort_in_place(lista, inicio=0, fim=None):
    """
    Implementação alternativa do Merge Sort que tenta minimizar a criação
    de novas listas, embora ainda use espaço adicional durante a mesclagem.
    
    Args:
        lista: Lista a ser ordenada
        inicio: Índice inicial da sublista a ser ordenada (padrão = 0)
        fim: Índice final da sublista a ser ordenada (padrão = len(lista) - 1)
        
    Returns:
        Lista ordenada (a ordenação também modifica a lista original)
    """
    # Inicializa o fim na primeira chamada
    if fim is None:
        fim = len(lista) - 1
    
    # Caso base: sublista com 0 ou 1 elemento já está ordenada
    if fim <= inicio:
        return
    
    # Divide a lista pela metade
    meio = (inicio + fim) // 2
    
    # Recursivamente ordena as duas metades
    merge_sort_in_place(lista, inicio, meio)
    merge_sort_in_place(lista, meio + 1, fim)
    
    # Mescla as duas metades ordenadas
    mesclar_in_place(lista, inicio, meio, fim)
    
    return lista


def mesclar_in_place(lista, inicio, meio, fim):
    """
    Função auxiliar para mesclar duas sublistas ordenadas in-place.
    
    Args:
        lista: Lista contendo as sublistas a serem mescladas
        inicio: Índice inicial da primeira sublista
        meio: Índice final da primeira sublista
        fim: Índice final da segunda sublista
    """
    # Cria listas temporárias
    esquerda = lista[inicio:meio + 1]
    direita = lista[meio + 1:fim + 1]
    
    # Índices para percorrer as listas
    i = j = 0
    k = inicio
    
    # Mescla as duas sublistas de volta na lista original
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1
    
    # Adiciona os elementos restantes (se houver)
    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1
    
    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1


def quick_sort(lista):
    """
    Implementação do algoritmo de ordenação rápida (Quick Sort).
    
    Este algoritmo também usa a estratégia de divisão e conquista: seleciona um
    elemento como pivô e particiona a lista em duas sublistas, uma com elementos
    menores que o pivô e outra com elementos maiores. Em seguida, aplica o mesmo
    processo recursivamente nas sublistas.
    
    Invariante de algoritmo:
    - Após a partição, todos os elementos à esquerda do pivô são menores ou iguais
      ao pivô, e todos os elementos à direita são maiores.
    
    Complexidade:
    - Tempo: O(n log n) no caso médio e melhor, O(n²) no pior caso
    - Espaço: O(log n) para a pilha de chamadas recursivas
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Nova lista ordenada (a lista original não é modificada)
    
    Exemplos:
        >>> l = [5, 3, 1, 4, 2]
        >>> quick_sort(l)
        [1, 2, 3, 4, 5]
        >>> l  # A lista original não é modificada
        [5, 3, 1, 4, 2]
    """
    # Cria uma cópia para não modificar a lista original
    lista_copia = lista[:]
    
    # Chama a função auxiliar para ordenar a cópia
    _quick_sort(lista_copia, 0, len(lista_copia) - 1)
    
    return lista_copia


def _quick_sort(lista, inicio, fim):
    """
    Função auxiliar para implementar o Quick Sort recursivamente.
    
    Args:
        lista: Lista a ser ordenada
        inicio: Índice inicial da sublista
        fim: Índice final da sublista
    """
    # Caso base: sublista com 0 ou 1 elemento já está ordenada
    if inicio >= fim:
        return
    
    # Particiona a lista e retorna a posição do pivô
    pos_pivo = particionar(lista, inicio, fim)
    
    # Recursivamente ordena as sublistas à esquerda e à direita do pivô
    _quick_sort(lista, inicio, pos_pivo - 1)
    _quick_sort(lista, pos_pivo + 1, fim)


def particionar(lista, inicio, fim):
    """
    Função auxiliar para particionar a lista ao redor de um pivô.
    
    Esta implementação seleciona o último elemento como pivô e rearranja
    a lista de modo que todos os elementos menores que o pivô fiquem à esquerda
    e todos os maiores fiquem à direita.
    
    Args:
        lista: Lista a ser particionada
        inicio: Índice inicial da sublista
        fim: Índice final da sublista
        
    Returns:
        Posição final do pivô após a partição
    """
    # Seleciona o pivô (último elemento)
    pivo = lista[fim]
    
    # Índice do menor elemento
    i = inicio - 1
    
    # Percorre a lista comparando os elementos com o pivô
    for j in range(inicio, fim):
        # Se o elemento atual é menor ou igual ao pivô
        if lista[j] <= pivo:
            # Incrementa o índice do menor elemento
            i += 1
            # Troca os elementos
            lista[i], lista[j] = lista[j], lista[i]
    
    # Coloca o pivô na posição correta
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    
    # Retorna a posição do pivô
    return i + 1


def quick_sort_mediana_de_tres(lista):
    """
    Implementação do Quick Sort com seleção de pivô pela mediana de três.
    
    Esta versão do Quick Sort seleciona o pivô usando a mediana entre o
    primeiro, o último e o elemento central da lista, o que reduz a chance
    de encontrar o pior caso em listas parcialmente ordenadas.
    
    Complexidade:
    - Tempo: O(n log n) no caso médio e melhor, O(n²) no pior caso
    - Espaço: O(log n) para a pilha de chamadas recursivas
    
    Args:
        lista: Lista de elementos a ser ordenada
        
    Returns:
        Nova lista ordenada (a lista original não é modificada)
    """
    # Cria uma cópia para não modificar a lista original
    lista_copia = lista[:]
    
    # Chama a função auxiliar para ordenar a cópia
    _quick_sort_mediana_de_tres(lista_copia, 0, len(lista_copia) - 1)
    
    return lista_copia


def _quick_sort_mediana_de_tres(lista, inicio, fim):
    """
    Função auxiliar para implementar o Quick Sort com mediana de três.
    
    Args:
        lista: Lista a ser ordenada
        inicio: Índice inicial da sublista
        fim: Índice final da sublista
    """
    # Caso base: sublista com 0 ou 1 elemento já está ordenada
    if inicio >= fim:
        return
    
    # Seleciona o pivô usando a mediana de três
    meio = (inicio + fim) // 2
    
    # Ordena inicio, meio, fim
    if lista[meio] < lista[inicio]:
        lista[inicio], lista[meio] = lista[meio], lista[inicio]
    if lista[fim] < lista[inicio]:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
    if lista[fim] < lista[meio]:
        lista[meio], lista[fim] = lista[fim], lista[meio]
    
    # Coloca o pivô (mediana) na penúltima posição
    lista[meio], lista[fim - 1] = lista[fim - 1], lista[meio]
    pivo = lista[fim - 1]
    
    # Particiona usando a mediana como pivô
    i = inicio
    j = fim - 1
    
    while True:
        i += 1
        while lista[i] < pivo:
            i += 1
        
        j -= 1
        while lista[j] > pivo:
            j -= 1
        
        if i >= j:
            break
        
        lista[i], lista[j] = lista[j], lista[i]
    
    # Coloca o pivô na posição correta
    lista[i], lista[fim - 1] = lista[fim - 1], lista[i]
    
    # Recursivamente ordena as sublistas
    _quick_sort_mediana_de_tres(lista, inicio, i - 1)
    _quick_sort_mediana_de_tres(lista, i + 1, fim)
