"""
Módulo de testes para o HashMap.

Este módulo contém testes para verificar a corretude e o desempenho da
implementação do HashMap no módulo hash_map.py.
"""

import unittest
import time
import random
from hash.hash_map import HashMap, HashMapEndAberto


class TestHashMap(unittest.TestCase):
    """
    Classe de testes para a implementação do HashMap com encadeamento.
    """
    
    def setUp(self):
        """
        Configura os dados para os testes.
        """
        # HashMap com tamanho padrão
        self.mapa_padrao = HashMap()
        
        # HashMap com tamanho pequeno para forçar colisões
        self.mapa_pequeno = HashMap(10)
        
        # Dados para testes
        self.chaves_valores = [
            ("chave1", "valor1"),
            ("chave2", "valor2"),
            ("chave3", "valor3"),
            ("chave4", "valor4"),
            ("chave5", "valor5")
        ]
    
    def test_inserir_buscar(self):
        """
        Testa as operações básicas de inserção e busca.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa_padrao.inserir(chave, valor)
        
        # Verifica se os valores foram inseridos corretamente
        for chave, valor in self.chaves_valores:
            self.assertEqual(self.mapa_padrao.buscar(chave), valor)
        
        # Verifica busca de chave inexistente
        self.assertIsNone(self.mapa_padrao.buscar("chave_inexistente"))
    
    def test_remover(self):
        """
        Testa a operação de remoção.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa_padrao.inserir(chave, valor)
        
        # Remove uma chave e verifica
        self.assertTrue(self.mapa_padrao.remover("chave3"))
        self.assertIsNone(self.mapa_padrao.buscar("chave3"))
        
        # Verifica se as outras chaves ainda existem
        self.assertEqual(self.mapa_padrao.buscar("chave1"), "valor1")
        self.assertEqual(self.mapa_padrao.buscar("chave5"), "valor5")
        
        # Tenta remover uma chave inexistente
        self.assertFalse(self.mapa_padrao.remover("chave_inexistente"))
    
    def test_atualizacao(self):
        """
        Testa a atualização de valores para chaves existentes.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa_padrao.inserir(chave, valor)
        
        # Atualiza um valor
        self.mapa_padrao.inserir("chave2", "novo_valor2")
        
        # Verifica se o valor foi atualizado
        self.assertEqual(self.mapa_padrao.buscar("chave2"), "novo_valor2")
        
        # Verifica se as outras chaves não foram afetadas
        self.assertEqual(self.mapa_padrao.buscar("chave1"), "valor1")
        self.assertEqual(self.mapa_padrao.buscar("chave3"), "valor3")
    
    def test_contains(self):
        """
        Testa o operador 'in' (__contains__).
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa_padrao.inserir(chave, valor)
        
        # Verifica se as chaves existem
        self.assertTrue("chave1" in self.mapa_padrao)
        self.assertTrue("chave5" in self.mapa_padrao)
        
        # Verifica se uma chave inexistente não existe
        self.assertFalse("chave_inexistente" in self.mapa_padrao)
    
    def test_getitem_setitem(self):
        """
        Testa os operadores [] (__getitem__ e __setitem__).
        """
        # Insere pares chave-valor usando []
        for chave, valor in self.chaves_valores:
            self.mapa_padrao[chave] = valor
        
        # Verifica se os valores foram inseridos corretamente
        for chave, valor in self.chaves_valores:
            self.assertEqual(self.mapa_padrao[chave], valor)
        
        # Tenta acessar uma chave inexistente
        with self.assertRaises(KeyError):
            _ = self.mapa_padrao["chave_inexistente"]
    
    def test_delitem(self):
        """
        Testa o operador del (__delitem__).
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa_padrao[chave] = valor
        
        # Remove uma chave usando del
        del self.mapa_padrao["chave3"]
        
        # Verifica se a chave foi removida
        self.assertFalse("chave3" in self.mapa_padrao)
        
        # Tenta remover uma chave inexistente
        with self.assertRaises(KeyError):
            del self.mapa_padrao["chave_inexistente"]
    
    def test_len(self):
        """
        Testa o operador len (__len__).
        """
        # Verifica tamanho inicial
        self.assertEqual(len(self.mapa_padrao), 0)
        
        # Insere pares chave-valor
        for i, (chave, valor) in enumerate(self.chaves_valores):
            self.mapa_padrao[chave] = valor
            self.assertEqual(len(self.mapa_padrao), i + 1)
        
        # Remove uma chave
        del self.mapa_padrao["chave3"]
        self.assertEqual(len(self.mapa_padrao), 4)
    
    def test_redimensionamento(self):
        """
        Testa o redimensionamento automático da tabela hash.
        """
        # Insere muitos pares chave-valor no mapa pequeno
        for i in range(100):
            chave = f"chave{i}"
            valor = f"valor{i}"
            self.mapa_pequeno[chave] = valor
        
        # Verifica se todos os valores foram mantidos após redimensionamento
        for i in range(100):
            chave = f"chave{i}"
            valor = f"valor{i}"
            self.assertEqual(self.mapa_pequeno[chave], valor)
    
    def test_colisoes(self):
        """
        Testa o tratamento de colisões.
        """
        # Cria um mapa com apenas 1 posição para forçar colisões
        mapa_colisao = HashMap(1)
        
        # Insere vários pares que necessariamente colidirão
        for i in range(10):
            chave = f"chave{i}"
            valor = f"valor{i}"
            mapa_colisao[chave] = valor
        
        # Verifica se todos os valores foram mantidos
        for i in range(10):
            chave = f"chave{i}"
            valor = f"valor{i}"
            self.assertEqual(mapa_colisao[chave], valor)
    
    def test_desempenho(self):
        """
        Testa o desempenho do HashMap para um grande número de operações.
        """
        # Número de operações
        n = 10000
        
        # Gera chaves e valores aleatórios
        random.seed(42)
        chaves = [f"chave{i}" for i in range(n)]
        valores = [f"valor{i}" for i in range(n)]
        
        # Mede o tempo de inserção
        inicio = time.time()
        for i in range(n):
            self.mapa_padrao[chaves[i]] = valores[i]
        tempo_insercao = time.time() - inicio
        
        # Mede o tempo de busca
        inicio = time.time()
        for i in range(n):
            _ = self.mapa_padrao[chaves[i]]
        tempo_busca = time.time() - inicio
        
        # Mede o tempo de remoção
        inicio = time.time()
        for i in range(n):
            del self.mapa_padrao[chaves[i]]
        tempo_remocao = time.time() - inicio
        
        # Imprime os resultados
        print(f"\nDesempenho do HashMap para {n} operações:")
        print(f"Tempo de inserção: {tempo_insercao:.6f} segundos")
        print(f"Tempo de busca: {tempo_busca:.6f} segundos")
        print(f"Tempo de remoção: {tempo_remocao:.6f} segundos")
        
        # Para uma implementação eficiente, os tempos devem ser muito menores que O(n)
        # Não usamos assert aqui porque o desempenho depende do hardware


class TestHashMapEndAberto(unittest.TestCase):
    """
    Classe de testes para a implementação do HashMap com endereçamento aberto.
    """
    
    def setUp(self):
        """
        Configura os dados para os testes.
        """
        # HashMap com tamanho padrão
        self.mapa = HashMapEndAberto()
        
        # Dados para testes
        self.chaves_valores = [
            ("chave1", "valor1"),
            ("chave2", "valor2"),
            ("chave3", "valor3"),
            ("chave4", "valor4"),
            ("chave5", "valor5")
        ]
    
    def test_inserir_buscar(self):
        """
        Testa as operações básicas de inserção e busca.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa.inserir(chave, valor)
        
        # Verifica se os valores foram inseridos corretamente
        for chave, valor in self.chaves_valores:
            self.assertEqual(self.mapa.buscar(chave), valor)
        
        # Verifica busca de chave inexistente
        self.assertIsNone(self.mapa.buscar("chave_inexistente"))
    
    def test_remover(self):
        """
        Testa a operação de remoção.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa.inserir(chave, valor)
        
        # Remove uma chave e verifica
        self.assertTrue(self.mapa.remover("chave3"))
        self.assertIsNone(self.mapa.buscar("chave3"))
        
        # Verifica se as outras chaves ainda existem
        self.assertEqual(self.mapa.buscar("chave1"), "valor1")
        self.assertEqual(self.mapa.buscar("chave5"), "valor5")
        
        # Tenta remover uma chave inexistente
        self.assertFalse(self.mapa.remover("chave_inexistente"))
    
    def test_atualizacao(self):
        """
        Testa a atualização de valores para chaves existentes.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa.inserir(chave, valor)
        
        # Atualiza um valor
        self.mapa.inserir("chave2", "novo_valor2")
        
        # Verifica se o valor foi atualizado
        self.assertEqual(self.mapa.buscar("chave2"), "novo_valor2")
        
        # Verifica se as outras chaves não foram afetadas
        self.assertEqual(self.mapa.buscar("chave1"), "valor1")
        self.assertEqual(self.mapa.buscar("chave3"), "valor3")
    
    def test_insercao_apos_remocao(self):
        """
        Testa a inserção após remoção, para verificar se o marcador REMOVIDO
        está funcionando corretamente.
        """
        # Insere pares chave-valor
        for chave, valor in self.chaves_valores:
            self.mapa.inserir(chave, valor)
        
        # Remove uma chave
        self.mapa.remover("chave3")
        
        # Insere uma nova chave
        self.mapa.inserir("chave6", "valor6")
        
        # Verifica se a nova chave foi inserida corretamente
        self.assertEqual(self.mapa.buscar("chave6"), "valor6")
        
        # Reinsere a chave removida
        self.mapa.inserir("chave3", "novo_valor3")
        
        # Verifica se a chave removida foi reinserida corretamente
        self.assertEqual(self.mapa.buscar("chave3"), "novo_valor3")


if __name__ == "__main__":
    unittest.main()
