# Sistema de Biblioteca Digital

Sistema desenvolvido em Python que demonstra a implementação e integração de diferentes estruturas de dados em um projeto prático e funcional.

## 📚 Estruturas de Dados Implementadas

- **Lista**: Armazenamento principal de todos os livros
- **Pilha**: Histórico de ações para funcionalidade de desfazer
- **Fila**: Gerenciamento de filas de empréstimo por livro
- **Árvore Binária de Busca (BST)**: Busca eficiente de livros por título
- **Tabela Hash**: Cadastro e busca rápida de usuários
- **Grafo**: Sistema de recomendações baseado em empréstimos conjuntos

## 🚀 Funcionalidades

### Gestão de Acervo
- Cadastro de livros com título, autor e código único
- Busca de livros por título (busca binária otimizada)
- Listagem ordenada de todos os livros

### Gestão de Usuários
- Cadastro de usuários com nome e ID
- Busca rápida por ID usando hash table

### Sistema de Empréstimos
- Fila de espera por livro
- Controle de devolução (FIFO - primeiro a pedir, primeiro a receber)
- Histórico de todas as operações

### Funcionalidades Avançadas
- **Desfazer**: Reverte a última operação realizada
- **Recomendações**: Sugere livros baseado em padrões de empréstimo

## 💻 Como Usar

1. Execute o sistema:
   ```bash
   cd biblioteca
   python main.py
   ```

2. Use o menu interativo para:
   - Cadastrar livros e usuários
   - Realizar empréstimos e devoluções
   - Buscar e listar informações
   - Obter recomendações de leitura

## 📁 Estrutura do Projeto

```
biblioteca/
├── livro.py          # Classe Livro
├── usuario.py        # Classe Usuario
├── fila.py           # Implementação de Fila
├── pilha.py          # Implementação de Pilha
├── bst.py            # Árvore Binária de Busca
├── grafo.py          # Grafo para recomendações
├── hash_table.py     # Tabela Hash (demonstrativa)
├── main.py           # Sistema principal
└── README.md         # Esta documentação
```

## 🎯 Objetivos Educacionais

Este projeto demonstra:
- Como diferentes estruturas de dados podem trabalhar juntas
- Aplicação prática de conceitos teóricos
- Integração de algoritmos de busca e ordenação
- Desenvolvimento de sistemas modulares em Python

## 🔧 Possíveis Melhorias Futuras

- Interface gráfica com tkinter ou PyQt
- Persistência de dados em arquivo/banco
- Sistema de multas e prazos
- Relatórios estatísticos
- API REST para integração externa
