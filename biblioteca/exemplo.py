#!/usr/bin/env python3
"""
Exemplo de uso do Sistema de Biblioteca Digital
Este arquivo demonstra como utilizar as funcionalidades do sistema programaticamente
"""

from livro import Livro
from usuario import Usuario
from fila import Fila
from pilha import Pilha
from bst import BST
from grafo import Grafo

def exemplo_uso():
    print("=== DEMONSTRAÇÃO DO SISTEMA DE BIBLIOTECA ===\n")
    
    # Inicialização das estruturas
    livros_lista = []
    usuarios_hash = {}
    historico_pilha = Pilha()
    livros_bst = BST()
    grafo_recomendacoes = Grafo()
    filas_emprestimo = {}
    
    print("1. CADASTRANDO LIVROS...")
    # Cadastro de livros
    livros_dados = [
        ("1984", "George Orwell", "L001"),
        ("Dom Casmurro", "Machado de Assis", "L002"),
        ("O Cortiço", "Aluísio Azevedo", "L003"),
        ("Fahrenheit 451", "Ray Bradbury", "L004"),
        ("Neuromancer", "William Gibson", "L005")
    ]
    
    for titulo, autor, codigo in livros_dados:
        livro = Livro(titulo, autor, codigo)
        livros_lista.append(livro)
        livros_bst.inserir(livro)
        filas_emprestimo[codigo] = Fila()
        grafo_recomendacoes.adicionar_livro(codigo)
        historico_pilha.empilhar(("livro", livro))
        print(f"   ✓ {livro}")
    
    print(f"\nTotal de livros cadastrados: {len(livros_lista)}")
    
    print("\n2. CADASTRANDO USUÁRIOS...")
    # Cadastro de usuários
    usuarios_dados = [
        ("Ana Silva", "U001"),
        ("Carlos Santos", "U002"),
        ("Maria Oliveira", "U003"),
        ("João Costa", "U004")
    ]
    
    for nome, id_usuario in usuarios_dados:
        usuario = Usuario(nome, id_usuario)
        usuarios_hash[id_usuario] = usuario
        historico_pilha.empilhar(("usuario", usuario))
        print(f"   ✓ {usuario}")
    
    print(f"\nTotal de usuários cadastrados: {len(usuarios_hash)}")
    
    print("\n3. TESTANDO BUSCA DE LIVROS...")
    # Teste de busca
    busca_teste = "1984"
    livro_encontrado = livros_bst.buscar(busca_teste)
    if livro_encontrado:
        print(f"   ✓ Livro encontrado: {livro_encontrado}")
    else:
        print(f"   ✗ Livro '{busca_teste}' não encontrado")
    
    print("\n4. SIMULANDO EMPRÉSTIMOS...")
    # Simulação de empréstimos
    emprestimos = [
        ("U001", "L001"),  # Ana pega 1984
        ("U002", "L001"),  # Carlos quer 1984 (vai para fila)
        ("U003", "L002"),  # Maria pega Dom Casmurro
        ("U001", "L002"),  # Ana quer Dom Casmurro (vai para fila)
        ("U004", "L003"),  # João pega O Cortiço
    ]
    
    for id_usuario, codigo_livro in emprestimos:
        usuario = usuarios_hash.get(id_usuario)
        fila = filas_emprestimo.get(codigo_livro)
        if usuario and fila:
            fila.enfileirar(usuario)
            livro = next((l for l in livros_lista if l.codigo == codigo_livro), None)
            print(f"   ✓ {usuario.nome} entrou na fila para '{livro.titulo}'")
            # Adiciona relação no grafo para recomendações
            for outro_codigo in filas_emprestimo:
                if outro_codigo != codigo_livro and not filas_emprestimo[outro_codigo].vazio():
                    grafo_recomendacoes.adicionar_relacao(codigo_livro, outro_codigo)
    
    print("\n5. VERIFICANDO FILAS DE EMPRÉSTIMO...")
    for codigo, fila in filas_emprestimo.items():
        if not fila.vazio():
            livro = next((l for l in livros_lista if l.codigo == codigo), None)
            print(f"   📚 {livro.titulo}: {len(fila)} usuário(s) na fila")
            for i, usuario in enumerate(fila.itens, 1):
                print(f"      {i}º - {usuario.nome}")
    
    print("\n6. SIMULANDO DEVOLUÇÕES...")
    # Simulação de devoluções
    for codigo in ["L001", "L002"]:
        fila = filas_emprestimo[codigo]
        if not fila.vazio():
            usuario = fila.desenfileirar()
            livro = next((l for l in livros_lista if l.codigo == codigo), None)
            print(f"   ✓ {usuario.nome} retirou '{livro.titulo}'")
    
    print("\n7. TESTANDO RECOMENDAÇÕES...")
    # Teste de recomendações
    codigo_teste = "L001"
    recomendados = grafo_recomendacoes.recomendar(codigo_teste)
    livro_ref = next((l for l in livros_lista if l.codigo == codigo_teste), None)
    print(f"   📖 Usuários que pegaram '{livro_ref.titulo}' também se interessaram por:")
    for cod in recomendados:
        livro = next((l for l in livros_lista if l.codigo == cod), None)
        if livro:
            print(f"      • {livro.titulo}")
    
    print("\n8. LISTANDO LIVROS ORDENADOS...")
    print("   📚 Acervo completo (ordem alfabética):")
    for livro in livros_bst.em_ordem():
        print(f"      • {livro}")
    
    print("\n9. TESTANDO FUNCIONALIDADE DESFAZER...")
    print(f"   Ações no histórico: {len(historico_pilha)}")
    if not historico_pilha.vazio():
        ultima_acao = historico_pilha.desempilhar()
        print(f"   ↶ Desfazendo: {ultima_acao[0]} - {ultima_acao[1]}")
    
    print("\n=== DEMONSTRAÇÃO CONCLUÍDA ===")
    print("Para uso interativo, execute: python main.py")

if __name__ == "__main__":
    exemplo_uso()
