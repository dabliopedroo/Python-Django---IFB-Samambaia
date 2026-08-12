# 🐍 Lista de Exercícios — Python + Django

Repositório destinado ao desenvolvimento da **Lista de Exercícios de Python**, utilizando o framework **Django**.

As atividades têm como objetivo praticar conceitos fundamentais da linguagem Python, estruturas de dados, funções, estruturas condicionais, laços de repetição e criação de sistemas interativos.

## 🚀 Tecnologias

* **Python**
* **Django**
* HTML/CSS
* Git e GitHub

## 📚 Atividades

### 01 — Custo de um carro

Calcular o custo final de um carro considerando o custo de fábrica, a porcentagem do distribuidor e os impostos.

**Conceitos:** entrada de dados, operações matemáticas e porcentagens.

### 02 — Troca de valores

Ler dois números inteiros e realizar a troca dos valores armazenados nas variáveis.

**Conceitos:** variáveis e manipulação de valores.

### 03 — Tempo de download

Calcular o tempo aproximado necessário para realizar o download de um arquivo, considerando seu tamanho e a velocidade da conexão.

**Conceitos:** conversão de unidades e operações matemáticas.

### 04 — Média e aprovação

Calcular as médias das provas e dos trabalhos e determinar se o aluno foi aprovado ou não.

**Conceitos:** médias, operações matemáticas e estruturas condicionais.

### 05 — Classificação de temperatura

Classificar uma temperatura em categorias:

* Frio extremo
* Frio
* Ameno
* Quente
* Muito quente

**Conceitos:** estruturas condicionais.

### 06 — Conversor de moedas

Converter um valor em reais para:

* Dólar
* Euro
* Libra
* Iene

O usuário deverá escolher a moeda através de um menu.

**Conceitos:** menu, condicionais e operações matemáticas.

### 07 — Sistema bancário

Criar um sistema bancário com saldo inicial de **R$ 1.000,00**, permitindo:

* Depositar
* Sacar
* Consultar saldo
* Sair

**Conceitos:** funções, menu, laços de repetição e condicionais.

### 08 — Exponenciação

Calcular `xʸ` utilizando multiplicações sucessivas e uma função.

**Conceitos:** funções e laços de repetição.

### 09 — Múltiplos

Exibir todos os múltiplos de um número informado pelo usuário entre 1 e 100.

**Conceitos:** funções, laços e operadores matemáticos.

### 10 — Lista de tarefas

Desenvolver um sistema para gerenciamento de tarefas pessoais com as opções:

* Adicionar tarefa
* Listar tarefas
* Remover tarefa
* Sair

As tarefas deverão ser armazenadas em uma lista.

**Conceitos:** listas, funções, menus e laços de repetição.

### 11 — Controle de cinema

Criar um sistema para controlar os **10 assentos** de uma sala de cinema.

Funcionalidades:

* Reservar assento
* Liberar assento
* Mostrar mapa de ocupação
* Sair

Os assentos serão representados utilizando valores booleanos.

**Conceitos:** listas, booleanos, funções e menus.

### 12 — Notas dos alunos

Criar um sistema para armazenar notas utilizando **tuplas** no formato:

```text
(nome_do_aluno, nota, disciplina)
```

Funcionalidades:

* Adicionar nota
* Mostrar melhor aluno por disciplina
* Consultar notas por aluno
* Exibir notas ordenadas
* Sair

**Conceitos:** tuplas, listas, funções e ordenação.

### 13 — Participação em eventos

Controlar a participação dos alunos em dois eventos:

* Palestra de Inteligência Artificial
* Workshop de Python

Utilizar conjuntos para realizar:

* Interseção
* Diferença
* União
* Consulta de participação

**Conceitos:** conjuntos (`set`), união, interseção, diferença e funções.

### 14 — Controle de estoque

Criar um sistema de controle de estoque de uma livraria utilizando um **dicionário**.

Funcionalidades:

* Adicionar livro
* Remover unidades
* Consultar estoque
* Listar livros em ordem alfabética
* Sair

**Conceitos:** dicionários, funções, menus e ordenação.

### 15 — Campeonato de futebol

Criar um sistema para gerenciamento de um campeonato utilizando um **dicionário**, armazenando os times e seus respectivos pontos.

Funcionalidades:

* Adicionar time
* Registrar resultado
* Atualizar pontuação
* Mostrar classificação
* Remover time
* Sair

Pontuação:

| Resultado | Pontos |
| --------- | -----: |
| Vitória   |      3 |
| Empate    |      1 |
| Derrota   |      0 |

**Conceitos:** dicionários, funções, condicionais, laços e ordenação.

---

## 🏗️ Estrutura do Projeto

Cada exercício será desenvolvido como uma funcionalidade dentro do projeto Django.

```text
lista-exercicios/
│
├── manage.py
├── README.md
│
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── exercicios/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
│
├── templates/
│   ├── base.html
│   └── exercicios/
│       ├── exercicio01.html
│       ├── exercicio02.html
│       ├── ...
│       └── exercicio15.html
│
└── static/
    ├── css/
    └── js/
```

## 🎯 Objetivos

* Praticar a linguagem **Python**
* Desenvolver aplicações utilizando **Django**
* Trabalhar com estruturas condicionais
* Utilizar laços de repetição
* Criar e utilizar funções
* Manipular listas, tuplas, conjuntos e dicionários
* Desenvolver interfaces simples para interação com os exercícios
* Aplicar conceitos de organização de projetos web

## 📌 Status

| Exercício                         | Status |
| --------------------------------- | :----: |
| 01 — Custo de um carro            |    ✅   |
| 02 — Troca de valores             |    ✅   |
| 03 — Tempo de download            |    ⬜   |
| 04 — Média e aprovação            |    ⬜   |
| 05 — Classificação de temperatura |    ⬜   |
| 06 — Conversor de moedas          |    ⬜   |
| 07 — Sistema bancário             |    ⬜   |
| 08 — Exponenciação                |    ⬜   |
| 09 — Múltiplos                    |    ⬜   |
| 10 — Lista de tarefas             |    ⬜   |
| 11 — Controle de cinema           |    ⬜   |
| 12 — Notas dos alunos             |    ⬜   |
| 13 — Participação em eventos      |    ⬜   |
| 14 — Controle de estoque          |    ⬜   |
| 15 — Campeonato de futebol        |    ⬜   |


## 👨‍💻 Desenvolvimento

Projeto desenvolvido para fins acadêmicos, com foco na prática de **Python e Django** através da resolução progressiva das 15 atividades propostas.
