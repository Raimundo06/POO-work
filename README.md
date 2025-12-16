Sistema de Gerenciamento de Biblioteca
Pessoal
Trabalho de Programação Orientada a Objetos
Universidade Federal do Cariri (UFCA)
Curso: Engenharia de Software (ou Engenharia da Computação – ajuste conforme necessário)
Disciplina: Programação Orientada a Objetos
Aluno: Raimundo Sebastião


Descrição do Projeto
Este projeto consiste no desenvolvimento de um Sistema de Gerenciamento de Biblioteca Pessoal,
implementado em Python, utilizando os principais conceitos de Programação Orientada a Objetos
(POO).
O sistema permite ao usuário cadastrar e gerenciar livros e revistas, controlar o status de leitura,
registrar anotações, realizar avaliações e gerar relatórios, mantendo todos os dados salvos mesmo
após o encerramento do programa, por meio de persistência em arquivo JSON.
O projeto foi desenvolvido com foco em organização, reutilização de código, separação de
responsabilidades e aplicação correta dos princípios de POO, conforme os critérios acadêmicos da

Objetivos Específicos
Aplicar os conceitos de classes e objetos
Utilizar herança para evitar duplicação de código
Implementar encapsulamento e abstração
Trabalhar com composição entre classes
Implementar persistência de dados utilizando JSON
Desenvolver uma interface de interação via menu em terminal

Descrição das Principais Classes
 Publicacao
Classe base que representa uma publicação genérica.
Atributos principais: - titulo - autor - ano - genero - num_paginas - status - avaliacao - anotacoes
Responsabilidade: Centralizar atributos e comportamentos comuns a livros e revistas.
 Livro
Classe que herda de Publicacao .
Responsabilidade: Representar livros sem adicionar atributos extras, aproveitando totalmente a
herança.
 Revista
Classe que herda de Publicacao .
•
•
•
•
•
•
2
Atributo adicional: - edicao
Responsabilidade: Representar revistas, estendendo a classe base com informações específicas.
 Anotacao
Classe responsável por armazenar anotações feitas pelo usuário durante a leitura.
Atributos: - texto - trecho - data
 Colecao
Classe responsável por gerenciar o conjunto de publicações.
Funções principais: - Adicionar publicações - Listar publicações - Buscar por título - Salvar dados
 Persistencia
Módulo responsável por salvar e carregar os dados da aplicação em um arquivo JSON.
Responsabilidade: Garantir que os dados permaneçam disponíveis mesmo após o encerramento do
programa.
 Persistência de Dados
O sistema utiliza um arquivo dados.json para armazenar todas as informações das publicações.
O arquivo é criado automaticamente ao salvar os dados
Os dados são carregados automaticamente ao iniciar o sistema
O formato JSON foi escolhido por ser simples, legível e amplamente utilizado
 Funcionamento do Menu
O usuário interage com o sistema através de um menu em terminal, com as seguintes opções:
Cadastrar Livro
Cadastrar Revista
Listar Publicações
Iniciar Leitura
Concluir Leitura
Adicionar Anotação
Avaliar Publicação
Gerar Relatório
Salvar e Sair
