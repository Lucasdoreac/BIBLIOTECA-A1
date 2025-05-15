# Algoritmos de Ordenação

Este documento fornece uma descrição detalhada dos algoritmos de ordenação implementados neste projeto, incluindo análise de complexidade, pseudocódigo e invariantes de laço.

## Algoritmos de Ordenação Simples

### Selection Sort (Ordenação por Seleção)

O Selection Sort é um algoritmo de ordenação que divide a lista em duas partes: uma parte ordenada no início e uma parte não ordenada no final. A cada iteração, o algoritmo encontra o menor elemento na parte não ordenada e o coloca na posição correta na parte ordenada.

#### Pseudocódigo

```
função selection_sort(lista):
    n = tamanho(lista)
    para i de 0 até n-1:
        indice_menor = i
        para j de i+1 até n-1:
            se lista[j] < lista[indice_menor]:
                indice_menor = j
        se indice_menor != i:
            troca lista[i] com lista[indice_menor]
    retorna lista
```

#### Invariante de Laço

A cada iteração `i`, os elementos em `lista[0...i-1]` estão ordenados e são os `i` menores elementos da lista original.

#### Análise de Complexidade

- **Tempo**: O(n²) no pior, médio e melhor caso
- **Espaço**: O(1), ordenação in-place

### Bubble Sort (Ordenação por Bolha)

O Bubble Sort percorre repetidamente a lista, comparando pares de elementos adjacentes e trocando-os se estiverem na ordem errada. A cada iteração, o maior elemento "borbulha" para o final da lista.

#### Pseudocódigo

```
função bubble_sort(lista):
    n = tamanho(lista)
    troca_realizada = verdadeiro
    iteracao = 0
    
    enquanto troca_realizada e iteracao < n:
        troca_realizada = falso
        para j de 0 até n-iteracao-2:
            se lista[j] > lista[j+1]:
                troca lista[j] com lista[j+1]
                troca_realizada = verdadeiro
        iteracao += 1
    
    retorna lista
```

#### Invariante de Laço

A cada iteração `i`, os `i` maiores elementos estão ordenados e em suas posições finais no final da lista.

#### Análise de Complexidade

- **Tempo**: O(n²) no pior e médio caso, O(n) no melhor caso (lista já ordenada)
- **Espaço**: O(1), ordenação in-place

## Algoritmos de Ordenação por Inserção

### Insertion Sort (Ordenação por Inserção)

O Insertion Sort constrói a lista ordenada um elemento por vez, inserindo cada novo elemento na posição correta. Funciona de maneira semelhante a como as pessoas ordenam cartas em um jogo de baralho.

#### Pseudocódigo

```
função insertion_sort(lista):
    para i de 1 até tamanho(lista) - 1:
        chave = lista[i]
        j = i - 1
        
        enquanto j >= 0 e lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        
        lista[j+1] = chave
    
    retorna lista
```

#### Invariante de Laço

A cada iteração `i`, os elementos em `lista[0...i]` estão ordenados entre si.

#### Análise de Complexidade

- **Tempo**: O(n²) no pior e médio caso, O(n) no melhor caso (lista já ordenada)
- **Espaço**: O(1), ordenação in-place

### Shell Sort

O Shell Sort é uma extensão do Insertion Sort que permite a troca de elementos distantes, reduzindo gradualmente a distância entre os elementos a serem comparados.

#### Pseudocódigo

```
função shell_sort(lista):
    n = tamanho(lista)
    intervalo = 1
    
    enquanto intervalo < n // 3:
        intervalo = 3 * intervalo + 1
    
    enquanto intervalo >= 1:
        para i de intervalo até n-1:
            j = i
            temp = lista[i]
            
            enquanto j >= intervalo e lista[j-intervalo] > temp:
                lista[j] = lista[j-intervalo]
                j -= intervalo
            
            lista[j] = temp
        
        intervalo //= 3
    
    retorna lista
```

#### Invariante de Laço

Para cada intervalo `h`, cada sublista formada por elementos separados por `h` posições está ordenada ao final da passagem.

#### Análise de Complexidade

- **Tempo**: Depende da sequência de intervalos, mas está entre O(n log² n) e O(n²)
- **Espaço**: O(1), ordenação in-place

## Algoritmos de Ordenação por Divisão e Conquista

### Merge Sort (Ordenação por Mesclagem)

O Merge Sort usa a estratégia de divisão e conquista: divide a lista pela metade recursivamente até ter sublistas de tamanho 1, ordena essas sublistas e depois as mescla de volta em uma única lista ordenada.

#### Pseudocódigo

```
função merge_sort(lista):
    se tamanho(lista) <= 1:
        retorna lista
    
    meio = tamanho(lista) // 2
    esquerda = lista[0:meio]
    direita = lista[meio:tamanho(lista)]
    
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)
    
    retorna mesclar(esquerda_ordenada, direita_ordenada)

função mesclar(esquerda, direita):
    resultado = []
    i = j = 0
    
    enquanto i < tamanho(esquerda) e j < tamanho(direita):
        se esquerda[i] <= direita[j]:
            adiciona esquerda[i] ao resultado
            i += 1
        senão:
            adiciona direita[j] ao resultado
            j += 1
    
    adiciona os elementos restantes de esquerda ao resultado
    adiciona os elementos restantes de direita ao resultado
    
    retorna resultado
```

#### Invariante de Algoritmo

A função `mesclar` sempre mescla duas listas ordenadas em uma única lista ordenada.

#### Análise de Complexidade

- **Tempo**: O(n log n) no pior, médio e melhor caso
- **Espaço**: O(n), requer espaço adicional

### Quick Sort (Ordenação Rápida)

O Quick Sort também usa a estratégia de divisão e conquista: seleciona um elemento como pivô e particiona a lista em duas sublistas, uma com elementos menores que o pivô e outra com elementos maiores. Em seguida, aplica o mesmo processo recursivamente nas sublistas.

#### Pseudocódigo

```
função quick_sort(lista):
    lista_copia = copia(lista)
    _quick_sort(lista_copia, 0, tamanho(lista_copia) - 1)
    retorna lista_copia

função _quick_sort(lista, inicio, fim):
    se inicio >= fim:
        retorna
    
    pos_pivo = particionar(lista, inicio, fim)
    _quick_sort(lista, inicio, pos_pivo - 1)
    _quick_sort(lista, pos_pivo + 1, fim)

função particionar(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1
    
    para j de inicio até fim - 1:
        se lista[j] <= pivo:
            i += 1
            troca lista[i] com lista[j]
    
    troca lista[i+1] com lista[fim]
    retorna i + 1
```

#### Invariante de Algoritmo

Após a partição, todos os elementos à esquerda do pivô são menores ou iguais ao pivô, e todos os elementos à direita são maiores.

#### Análise de Complexidade

- **Tempo**: O(n log n) no caso médio e melhor, O(n²) no pior caso
- **Espaço**: O(log n) para a pilha de chamadas recursivas

## Comparação entre Algoritmos de Ordenação

| Algoritmo | Complexidade de Tempo (Melhor) | Complexidade de Tempo (Médio) | Complexidade de Tempo (Pior) | Complexidade de Espaço | Estável | In-Place |
|-----------|-------------------------------|------------------------------|----------------------------|------------------------|---------|----------|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | Não | Sim |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Sim | Sim |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Sim | Sim |
| Shell Sort | O(n log n) | Depende | O(n²) | O(1) | Não | Sim |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Sim | Não |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | Não | Sim |

### Recomendações de Uso

- **Selection Sort**: Útil para listas pequenas ou quando o custo de troca é alto.
- **Bubble Sort**: Simples, mas ineficiente para listas grandes.
- **Insertion Sort**: Bom para listas quase ordenadas ou pequenas.
- **Shell Sort**: Melhoria do Insertion Sort para listas maiores.
- **Merge Sort**: Eficiente para qualquer tamanho de lista, especialmente quando a estabilidade é importante.
- **Quick Sort**: Geralmente o mais rápido na prática para listas grandes, mas pode ter casos patológicos.
