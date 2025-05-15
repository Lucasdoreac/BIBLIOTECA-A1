# Algoritmos de Busca

Este documento fornece uma descrição detalhada dos algoritmos de busca implementados neste projeto, incluindo análise de complexidade, pseudocódigo e invariantes de laço.

## Busca Sequencial (Linear Search)

A busca sequencial é o algoritmo de busca mais simples. Ele percorre a lista sequencialmente do início ao fim, comparando cada elemento com o item procurado.

### Pseudocódigo

```
função busca_sequencial(lista, item):
    para i de 0 até tamanho(lista) - 1:
        se lista[i] == item:
            retorna i
    retorna -1
```

### Invariante de Laço

A cada iteração `i`, todos os elementos em `lista[0...i-1]` são diferentes de `item`.

### Análise de Complexidade

- **Tempo**: O(n) no pior caso, onde n é o tamanho da lista
- **Espaço**: O(1), espaço constante

### Vantagens e Desvantagens

**Vantagens:**
- Simples de implementar e entender
- Funciona em listas não ordenadas
- Não requer pré-processamento da lista

**Desvantagens:**
- Ineficiente para listas grandes
- Não aproveita qualquer ordenação que a lista possa ter

## Busca Binária (Binary Search)

A busca binária é um algoritmo eficiente para encontrar um elemento em uma lista ordenada. Ele divide repetidamente pela metade o espaço de busca, comparando o item procurado com o elemento no meio da lista.

### Pseudocódigo

```
função busca_binaria(lista, item):
    inicio = 0
    fim = tamanho(lista) - 1
    
    enquanto inicio <= fim:
        meio = (inicio + fim) // 2
        
        se lista[meio] == item:
            retorna meio
        senão se lista[meio] > item:
            fim = meio - 1
        senão:
            inicio = meio + 1
    
    retorna -1
```

### Invariante de Laço

Se o item existe na lista, então está no intervalo `lista[inicio...fim]`.

### Análise de Complexidade

- **Tempo**: O(log n) no pior caso, onde n é o tamanho da lista
- **Espaço**: O(1) para implementação iterativa, O(log n) para recursiva

### Vantagens e Desvantagens

**Vantagens:**
- Muito eficiente para listas grandes
- Logarítmico em vez de linear como a busca sequencial

**Desvantagens:**
- Requer que a lista esteja ordenada
- Mais complexo de implementar que a busca sequencial
- Não pode ser usado com listas baseadas em acesso sequencial (como listas ligadas)

## Comparação entre Busca Sequencial e Busca Binária

| Algoritmo | Complexidade de Tempo | Requer Ordenação | Uso Recomendado |
|-----------|------------------------|-------------------|-----------------|
| Busca Sequencial | O(n) | Não | Listas pequenas, listas não ordenadas |
| Busca Binária | O(log n) | Sim | Listas ordenadas, listas grandes |

A busca binária é muito mais eficiente que a busca sequencial para listas grandes. Para uma lista com 1 milhão de elementos, a busca sequencial pode precisar de até 1 milhão de comparações, enquanto a busca binária precisará de no máximo 20 comparações.

No entanto, a busca binária só pode ser usada se a lista estiver ordenada. Se a lista não estiver ordenada e você precisar fazer poucas buscas, pode ser mais eficiente usar a busca sequencial diretamente, em vez de ordenar a lista e então usar a busca binária.
