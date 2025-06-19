from livro import Livro
from usuario import Usuario
from fila import Fila
from pilha import Pilha
from bst import BST
from grafo import Grafo

def menu():
    print("\n========= Biblioteca Digital =========")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Buscar livro")
    print("4. Realizar empréstimo")
    print("5. Devolver livro")
    print("6. Desfazer última ação")
    print("7. Recomendar livros")
    print("8. Listar livros cadastrados")
    print("9. Sair")
    return input("Escolha uma opção: ")

# Estruturas globais
livros_lista = []
usuarios_hash = {}
historico_pilha = Pilha()
livros_bst = BST()
grafo_recomendacoes = Grafo()
filas_emprestimo = {}

def main():
    while True:
        op = menu()
        
        if op == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            codigo = input("Código: ")
            livro = Livro(titulo, autor, codigo)
            livros_lista.append(livro)
            livros_bst.inserir(livro)
            filas_emprestimo[codigo] = Fila()
            grafo_recomendacoes.adicionar_livro(codigo)
            historico_pilha.empilhar(("livro", livro))
            print("Livro cadastrado com sucesso!")

        elif op == "2":
            nome = input("Nome do usuário: ")
            id = input("ID do usuário: ")
            usuario = Usuario(nome, id)
            usuarios_hash[id] = usuario
            historico_pilha.empilhar(("usuario", usuario))
            print("Usuário cadastrado!")

        elif op == "3":
            titulo = input("Título do livro: ")
            livro = livros_bst.buscar(titulo)
            if livro:
                print(f"Encontrado: {livro}")
            else:
                print("Livro não encontrado.")

        elif op == "4":
            id = input("ID do usuário: ")
            codigo = input("Código do livro: ")
            usuario = usuarios_hash.get(id)
            fila = filas_emprestimo.get(codigo)
            if usuario and fila:
                fila.enfileirar(usuario)
                historico_pilha.empilhar(("emprestimo", usuario, codigo))
                print("Usuário entrou na fila de empréstimo.")
            else:
                print("Usuário ou livro não encontrado.")

        elif op == "5":
            codigo = input("Código do livro: ")
            fila = filas_emprestimo.get(codigo)
            if fila and not fila.vazio():
                usuario = fila.desenfileirar()
                print(f"{usuario.nome} devolveu o livro.")
                historico_pilha.empilhar(("devolucao", usuario, codigo))
            else:
                print("Nenhum usuário na fila deste livro.")

        elif op == "6":
            if historico_pilha.vazio():
                print("Nada para desfazer.")
            else:
                acao = historico_pilha.desempilhar()
                if acao[0] == "livro":
                    livro = acao[1]
                    livros_lista.remove(livro)
                    print("Desfeito cadastro de livro.")
                elif acao[0] == "usuario":
                    usuario = acao[1]
                    usuarios_hash.pop(usuario.id, None)
                    print("Desfeito cadastro de usuário.")
                elif acao[0] == "emprestimo":
                    usuario, codigo = acao[1], acao[2]
                    if codigo in filas_emprestimo:
                        fila = filas_emprestimo[codigo]
                        fila.itens = [u for u in fila.itens if u.id != usuario.id]
                        print("Desfeito empréstimo.")
                elif acao[0] == "devolucao":
                    usuario, codigo = acao[1], acao[2]
                    if codigo in filas_emprestimo:
                        filas_emprestimo[codigo].itens.insert(0, usuario)
                        print("Desfeita devolução.")

        elif op == "7":
            codigo = input("Código do livro: ")
            recomendados = grafo_recomendacoes.recomendar(codigo)
            if recomendados:
                print("Usuários que pegaram este livro também pegaram:")
                for cod in recomendados:
                    livro = next((l for l in livros_lista if l.codigo == cod), None)
                    if livro:
                        print(f"- {livro}")
            else:
                print("Nenhuma recomendação disponível.")

        elif op == "8":
            print("\n--- Livros cadastrados ---")
            for livro in livros_bst.em_ordem():
                print(livro)
                
        elif op == "9":
            print("Saindo...")
            break
            
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
