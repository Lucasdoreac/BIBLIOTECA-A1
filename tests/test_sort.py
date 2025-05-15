"""
Módulo de testes para os algoritmos de ordenação.

Este módulo contém testes para verificar a corretude e o desempenho dos
algoritmos de ordenação implementados nos módulos:
- simple_sorts.py (Selection Sort e Bubble Sort)
- insertion_sorts.py (Insertion Sort e Shell Sort)
- divide_and_conquer_sorts.py (Merge Sort e Quick Sort)
"""

import unittest
import time
import random
import copy

# Importação dos algoritmos de ordenação
from sort.simple_sorts import selection_sort, bubble_sort, bubble_sort_otimizado
from sort.insertion_sorts import insertion_sort, shell_sort, insertion_sort_binario
from sort.divide_and_conquer_sorts import merge_sort, quick_sort, quick_sort_mediana_de_tres


class TestAlgoritmosOrdenacao(unittest.TestCase):
    """
    Classe de testes para os algoritmos de ordenação.
    """
    
    def setUp(self):
        """
        Configura os dados para os testes.
        """
        # Lista já ordenada
        self.lista_ordenada = list(range(100))
        
        # Lista em ordem inversa
        self.lista_inversa = list(range(100, 0, -1))
        
        # Lista com elementos aleatórios
        random.seed(42)  # Garante que os mesmos números "aleatórios" sejam gerados
        self.lista_aleatoria = random.sample(range(1000), 100)
        
        # Cópias das listas para cada algoritmo
        self.listas = {}
        for algo in ["selection", "bubble", "bubble_otimizado", "insertion", 
                     "shell", "insertion_binario", "merge", "quick", "quick_mediana"]:
            self.listas[algo] = {
                "ordenada": copy.deepcopy(self.lista_ordenada),
                "inversa": copy.deepcopy(self.lista_inversa),
                "aleatoria": copy.deepcopy(self.lista_aleatoria)
            }
        
        # Tempo de execução para cada algoritmo
        self.tempos = {}
    
    def test_corretude(self):
        """
        Testa se todos os algoritmos ordenam corretamente as listas.
        """
        # Resultado esperado (lista ordenada)
        esperado_ordenada = sorted(self.lista_ordenada)
        esperado_inversa = sorted(self.lista_inversa)
        esperado_aleatoria = sorted(self.lista_aleatoria)
        
        # Algoritmos e suas funções correspondentes
        algoritmos = {
            "selection": selection_sort,
            "bubble": bubble_sort,
            "bubble_otimizado": bubble_sort_otimizado,
            "insertion": insertion_sort,
            "shell": shell_sort,
            "insertion_binario": insertion_sort_binario,
            "merge": merge_sort,
            "quick": quick_sort,
            "quick_mediana": quick_sort_mediana_de_tres
        }
        
        # Testa cada algoritmo com cada tipo de lista
        for nome, func in algoritmos.items():
            # Lista já ordenada
            inicio = time.time()
            resultado = func(self.listas[nome]["ordenada"])
            self.tempos[nome + "_ordenada"] = time.time() - inicio
            self.assertEqual(resultado, esperado_ordenada)
            
            # Lista em ordem inversa
            inicio = time.time()
            resultado = func(self.listas[nome]["inversa"])
            self.tempos[nome + "_inversa"] = time.time() - inicio
            self.assertEqual(resultado, esperado_inversa)
            
            # Lista aleatória
            inicio = time.time()
            resultado = func(self.listas[nome]["aleatoria"])
            self.tempos[nome + "_aleatoria"] = time.time() - inicio
            self.assertEqual(resultado, esperado_aleatoria)
    
    def test_desempenho_lista_grande(self):
        """
        Testa o desempenho dos algoritmos com uma lista grande.
        """
        # Lista grande com elementos aleatórios
        random.seed(42)
        lista_grande = random.sample(range(10000), 1000)
        
        # Algoritmos e suas funções correspondentes
        algoritmos = {
            "selection": selection_sort,
            "bubble": bubble_sort,
            "bubble_otimizado": bubble_sort_otimizado,
            "insertion": insertion_sort,
            "shell": shell_sort,
            "insertion_binario": insertion_sort_binario,
            "merge": merge_sort,
            "quick": quick_sort,
            "quick_mediana": quick_sort_mediana_de_tres
        }
        
        print("\nTempo de execução para ordenar uma lista grande (1000 elementos):")
        
        # Testa cada algoritmo
        for nome, func in algoritmos.items():
            # Cria uma cópia da lista para não interferir nos outros algoritmos
            lista_copia = copy.deepcopy(lista_grande)
            
            # Mede o tempo de execução
            inicio = time.time()
            resultado = func(lista_copia)
            tempo = time.time() - inicio
            
            # Verifica se a lista foi ordenada corretamente
            self.assertEqual(resultado, sorted(lista_grande))
            
            # Armazena e imprime o tempo
            self.tempos[nome + "_grande"] = tempo
            print(f"{nome.ljust(20)}: {tempo:.6f} segundos")
    
    def test_caso_especial_pior_caso_quicksort(self):
        """
        Testa o pior caso do Quick Sort (lista já ordenada) e compara com a
        versão que usa a mediana de três como pivô.
        """
        # Lista já ordenada (pior caso para Quick Sort simples)
        lista_ordenada = list(range(1000))
        
        # Cópias para cada algoritmo
        lista_quick = copy.deepcopy(lista_ordenada)
        lista_quick_mediana = copy.deepcopy(lista_ordenada)
        
        # Mede o tempo do Quick Sort simples
        inicio = time.time()
        quick_sort(lista_quick)
        tempo_quick = time.time() - inicio
        
        # Mede o tempo do Quick Sort com mediana de três
        inicio = time.time()
        quick_sort_mediana_de_tres(lista_quick_mediana)
        tempo_quick_mediana = time.time() - inicio
        
        print("\nComparação do Quick Sort para o pior caso (lista já ordenada):")
        print(f"Quick Sort simples: {tempo_quick:.6f} segundos")
        print(f"Quick Sort com mediana: {tempo_quick_mediana:.6f} segundos")
        
        # Para a maioria dos casos, o Quick Sort com mediana de três é mais
        # eficiente para listas já ordenadas, mas não garantimos isso no teste
    
    def test_caso_de_borda(self):
        """
        Testa casos de borda, como listas vazias ou com um único elemento.
        """
        # Algoritmos e suas funções correspondentes
        algoritmos = {
            "selection": selection_sort,
            "bubble": bubble_sort,
            "bubble_otimizado": bubble_sort_otimizado,
            "insertion": insertion_sort,
            "shell": shell_sort,
            "insertion_binario": insertion_sort_binario,
            "merge": merge_sort,
            "quick": quick_sort,
            "quick_mediana": quick_sort_mediana_de_tres
        }
        
        # Testa cada algoritmo com cada tipo de caso de borda
        for nome, func in algoritmos.items():
            # Lista vazia
            self.assertEqual(func([]), [])
            
            # Lista com um único elemento
            self.assertEqual(func([42]), [42])
            
            # Lista com elementos repetidos
            self.assertEqual(func([3, 1, 3, 2, 3]), [1, 2, 3, 3, 3])
    
    def tearDown(self):
        """
        Exibe um resumo dos tempos de execução após a execução dos testes.
        """
        # Imprime os tempos de execução para listas pequenas (opcional)
        if hasattr(self, '_outcome') and hasattr(self._outcome, 'errors'):
            # Verificar se todos os testes passaram
            errors = [e for e in getattr(self._outcome, 'errors', []) if e[1] is not None]
            if not errors:
                print("\nResumo dos tempos de execução para listas pequenas (100 elementos):")
                
                tipos_lista = ["ordenada", "inversa", "aleatoria"]
                algoritmos = ["selection", "bubble", "bubble_otimizado", "insertion", 
                              "shell", "insertion_binario", "merge", "quick", "quick_mediana"]
                
                for tipo in tipos_lista:
                    print(f"\nLista {tipo}:")
                    for algo in algoritmos:
                        tempo = self.tempos.get(algo + "_" + tipo, 0)
                        print(f"{algo.ljust(20)}: {tempo:.6f} segundos")


if __name__ == "__main__":
    unittest.main()
