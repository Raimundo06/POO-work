Sistema de Gerenciamento de Biblioteca
Pessoal
Trabalho de Programação Orientada a Objetos
Universidade Federal do Cariri (UFCA)
Curso: Engenharia de Software
Disciplina: Programação Orientada a Objetos
Aluno: Raimundo Sebastião


Descrição do Projeto
Este projeto consiste no desenvolvimento de um Sistema de Gerenciamento de Biblioteca Pessoal,
implementado em Python, utilizando os principais conceitos de Programação Orientada a Objetos
(POO).
O sistema permite ao usuário cadastrar e gerenciar livros e revistas, controlar o status de leitura,
registrar anotações, realizar avaliações e gerar relatórios, mantendo todos os dados salvos mesmo
após o encerramento do programa, por meio de persistência em arquivo JSON.

# 📚 Sistema de Gerenciamento de Biblioteca Pessoal

> **Projeto de Programação Orientada a Objetos (POO)**
> **Universidade Federal do Cariri (UFCA)**
> **Curso:** Engenharia de Software
> **Aluno:** Raimundo Sebastião
> **Período:** 2025.2

---

## 🧠 Visão Geral

Este projeto consiste em um **Sistema de Gerenciamento de Biblioteca Pessoal**, desenvolvido em **Python**, aplicando de forma prática os principais conceitos da **Programação Orientada a Objetos (POO)**.

O sistema permite ao usuário cadastrar, consultar, atualizar e organizar publicações como **livros** e **revistas**, além de adicionar **anotações**, controlar **status de leitura** e gerar **relatórios**. Os dados são persistidos utilizando arquivos **JSON**, garantindo simplicidade e portabilidade.

---

## 🎯 Objetivos do Projeto

* Aplicar conceitos fundamentais de POO na prática
* Implementar **regras de negócio** claras

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* Manipulação de arquivos **JSON**
* Programação Orientada a Objetos (POO)

---

## 🗂️ Estrutura do Projeto

```
📦 biblioteca-poo
├── anotacao.py
├── publicacao.py
├── livro.py
├── revista.py
├── colecao.py
├── persistencia.py
├── relatorio.py
├── main.py
├── settings.json
└── README.md
```

### 📄 Descrição dos Arquivos

* **publicacao.py** → Classe base `Publicacao`
* **livro.py** → Classe `Livro` (herda de `Publicacao`)
* **revista.py** → Classe `Revista` (herda de `Publicacao`)
* **anotacao.py** → Classe responsável por anotações do usuário
* **colecao.py** → Gerencia a coleção de publicações
* **persistencia.py** → Leitura e escrita de dados em JSON
* **relatorio.py** → Geração de relatórios
* **main.py** → Interface via terminal
* **settings.json** → Configurações do sistema

---

## 🧩 Conceitos de POO Aplicados

### 🔹 Abstração

A classe `Publicacao` define atributos e comportamentos comuns a livros e revistas.

### 🔹 Herança

As classes `Livro` e `Revista` herdam de `Publicacao`, reutilizando e especializando comportamentos.

### 🔹 Encapsulamento

Os atributos são manipulados por métodos específicos, garantindo integridade dos dados.



---

## 📏 Regras de Negócio

* Não é permitido cadastrar publicações sem título
* O status da leitura deve ser válido (ex: *Não iniciado*, *Em andamento*, *Concluído*)
* A avaliação deve estar dentro de um intervalo válido
* Anotações não podem ser vazias

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd biblioteca-poo
   ```

3. Execute o sistema:

   ```bash
   python main.py
   ```

---

## 📊 Funcionalidades

* Cadastro de livros e revistas
* Busca por título
* Alteração de status de leitura
* Registro de avaliações
* Adição de anotações
* Geração de relatórios
* Persistência de dados em JSON

---



