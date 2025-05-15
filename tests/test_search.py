"""
Módulo de testes para os algoritmos de busca.

Este módulo contém testes para verificar a corretude e o desempenho dos
algoritmos de busca implementados no módulo search_algorithms.py.
"""

import unittest
import time
import random
from search.search_algorithms import busca_sequencial, busca_binaria, busca_binaria_recursiva


class TestAlgoritmosBusca(unittest.TestCase):
    """
    Classe de testes para os algoritmos de busca.
    """
    
    def setUp(self):
        """
        Configura os dados para os testes.
        """
        # Lista pequena para testes básicos
        self.lista_pequena = [1, 3, 5, 7, 9]
        
        # Lista média para testes mais elaborados
        self.lista_media = list(range(0, 1000, 2))  # Números pares de 0 a 998
        
        # Lista grande para testes de desempenho
        self.lista_grande = list(range(10000))
    
    def test_busca_sequencial_elemento_presente(self):
        """
        Testa a busca sequencial quando o elemento está presente na lista.
        """
        # Testa na lista pequena
        self.assertEqual(busca_sequencial(self.lista_pequena, 5), 2)
        
        # Testa na lista média
        self.assertEqual(busca_sequencial(self.lista_media, 500), 250)
    
    def test_busca_sequencial_elemento_ausente(self):
        """
        Testa a busca sequencial quando o elemento não está presente na lista.
        """
        # Testa na lista pequena
        self.assertEqual(busca_sequencial(self.lista_pequena, 4), -1)
        
        # Testa na lista média
        self.assertEqual(busca_sequencial(self.lista_media, 501), -1)
    
    def test_busca_binaria_elemento_presente(self):
        """
        Testa a busca binária quando o elemento está presente na lista.
        """
        # Testa na lista pequena
        self.assertEqual(busca_binaria(self.lista_pequena, 5), 2)
        
        # Testa na lista média
        self.assertEqual(busca_binaria(self.lista_media, 500), 250)
        
        # Testa na lista grande
        self.assertEqual(busca_binaria(self.lista_grande, 5000), 5000)
    
    def test_busca_binaria_elemento_ausente(self):
        """
        Testa a busca binária quando o elemento não está presente na lista.
        """
        # Testa na lista pequena
        self.assertEqual(busca_binaria(self.lista_pequena, 4), -1)
        
        # Testa na lista média
        self.assertEqual(busca_binaria(self.lista_media, 501), -1)
        
        # Testa na lista grande
        self.assertEqual(busca_binaria(self.lista_grande, 10001), -1)
    
    def test_busca_binaria_recursiva(self):
        """
        Testa a implementação recursiva da busca binária.
        """
        # Testa na lista pequena
        self.assertEqual(busca_binaria_recursiva(self.lista_pequena, 5), 2)
        self.assertEqual(busca_binaria_recursiva(self.lista_pequena, 4), -1)
        
        # Testa na lista média
        self.assertEqual(busca_binaria_recursiva(self.lista_media, 500), 250)
        self.assertEqual(busca_binaria_recursiva(self.lista_media, 501), -1)
    
    def test_comparacao_desempenho(self):
        """
        Compara o desempenho dos algoritmos de busca.
        """
        # Elemento presente no final da lista (pior caso para busca sequencial)
        elemento = self.lista_grande[-1]
        
        # Mede o tempo da busca sequencial
        inicio = time.time()
        busca_sequencial(self.lista_grande, elemento)
        tempo_sequencial = time.time() - inicio
        
        # Mede o tempo da busca binária
        inicio = time.time()
        busca_binaria(self.lista_grande, elemento)
        tempo_binario = time.time() - inicio
        
        # Mede o tempo da busca binária recursiva
        inicio = time.time()
        busca_binaria_recursiva(self.lista_grande, elemento)
        tempo_recursivo = time.time() - inicio
        
        # Imprime os resultados
        print(f"\nTempo de busca sequencial: {tempo_sequencial:.6f} segundos")
        print(f"Tempo de busca binária: {tempo_binario:.6f} segundos")
        print(f"Tempo de busca binária recursiva: {tempo_recursivo:.6f} segundos")
        
        # A busca binária deve ser mais rápida que a sequencial para listas grandes
        # Essa comparação pode falhar em sistemas muito rápidos ou com pouca carga,
        # então não usamos assert aqui
        
    def test_casos_de_borda(self):
        """
        Testa casos de borda, como listas vazias ou com um único elemento.
        """
        # Lista vazia
        self.assertEqual(busca_sequencial([], 5), -1)
        self.assertEqual(busca_binaria([], 5), -1)
        self.assertEqual(busca_binaria_recursiva([], 5), -1)
        
        # Lista com um único elemento (presente)
        self.assertEqual(busca_sequencial([5], 5), 0)
        self.assertEqual(busca_binaria([5], 5), 0)
        self.assertEqual(busca_binaria_recursiva([5], 5), 0)
        
        # Lista com um único elemento (ausente)
        self.assertEqual(busca_sequencial([1], 5), -1)
        self.assertEqual(busca_binaria([1], 5), -1)
        self.assertEqual(busca_binaria_recursiva([1], 5), -1)


if __name__ == "__main__":
    unittest.main()
