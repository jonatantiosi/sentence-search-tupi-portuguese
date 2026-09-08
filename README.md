# sentence-search-tupi-portuguese

The goal of this project is to use technology to contribuite to Quality Education and Industry, Innovation and Infrastructure which are some of UN's SDGs (Sustainable Development Goals). For that, I created a digital collection/database using JSON that stores sentences and words in Tupi, a South American indigenous language, as well as portuguese translations.

# Ekar SSTP

### Sentence Search Tupi-Português

O **Ekar SSTP** é uma aplicação desenvolvida em Python para consulta e organização de palavras e sentenças em Tupi acompanhadas de suas respectivas traduções para o português.

O projeto foi desenvolvido como parte de uma atividade extensionista do curso de **Sistemas de Informação**, buscando aplicar recursos tecnológicos ao aprendizado de línguas e à organização e valorização de conhecimentos relacionados às línguas indígenas.

---

## Sobre o projeto

O Ekar SSTP surgiu a partir da ideia de adaptar para a língua Tupi um recurso utilizado durante o aprendizado de outros idiomas: a busca por sentenças de exemplo.

A proposta é reunir em um acervo palavras, definições e sentenças em Tupi acompanhadas de suas traduções para o português. Dessa forma, o usuário pode consultar exemplos de uso e também contribuir com novos registros.

Atualmente, o projeto funciona como uma aplicação de **linha de comando (CLI)** desenvolvida em Python, utilizando arquivos JSON para armazenar os dados.

---

## Funcionalidades

O sistema possui quatro opções principais:

### Pesquisar palavra

Permite pesquisar uma palavra no acervo.

Quando encontrada, a aplicação apresenta:

- A sentença em Tupi;
- A tradução da sentença para o português;
- A definição da palavra, quando disponível.

### Adicionar nova frase

Permite adicionar uma nova sentença ao acervo.

O usuário informa:

1. A frase em Tupi;
2. A tradução correspondente em português.

### Adicionar nova palavra

Permite adicionar uma palavra ao acervo juntamente com sua definição em português.

### Sair

Encerra a aplicação e salva as alterações realizadas nos arquivos do acervo.

---

## Tecnologias utilizadas

- **Python**
- **JSON**
- **Git / GitHub**

O projeto utiliza apenas recursos da biblioteca padrão do Python, não sendo necessário instalar bibliotecas externas para sua execução.

---

## Requisitos

Para executar o projeto, é necessário ter:

- **Python 3.10 ou superior**
- Git, caso opte por clonar o repositório

A versão mínima do Python é 3.10 devido à utilização da estrutura `match/case` no código.

---

## Como baixar

### Opção 1 — Download pelo GitHub

1. Acesse o repositório do projeto.
2. Clique em **Code**.
3. Selecione **Download ZIP**.
4. Extraia os arquivos em uma pasta de sua preferência.

### Opção 2 — Clonar o repositório

No terminal, execute:

```bash
git clone URL_DO_REPOSITORIO
