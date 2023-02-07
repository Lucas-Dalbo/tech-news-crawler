[Read it in English!](./README-Eng.md)

# Projeto: Tech News Scraping
Este projeto foi desenvolvido enquanto estudante da Trybe no módulo de Ciências da Computação.

---
## Objetivo
Utilizar o **Python** para implementar funções que realizam a raspagem de dados e, em seguida, utilizam essas informações para popular um banco de dados não relacional, o **MongoDB**.

O site utilizado para a raspagem é o [Blog da Trybe](https://blog.betrybe.com), com as devidas permissões.

---
## Habilidades desenvolvidas
 - Utilização do terminal interativo do Python;
 - Como escrever os próprios módulos e importá-los em outros arquivos;
 - Aplicação de técnicas de raspagem de dados.
 - Extração de conteúdos HTML.
 - Como armazenar os dados obtidos em um banco de dados.

---
## Requisitos
  01. Função `fetch`, responsável por extrair o conteúdo HTML de uma página.
  02. Função `scrape_updates`, que realiza a raspagem para extrair as URL's das notícias.
  03. Função `scrape_next_page_link`, faz a raspagem para buscar a URL da próxima pagina.
  04. Função `scrape_news`, faz a raspagem das notícias e estrutura as informações em um dict.
  05. Função `get_tech_news`, utiliza as funções criadas previamente para realizar uma raspagem mais robusta, capaz de paginação e de adicionar as notícias ao banco de dados.
  06. Função `search_by_title`, realiza uma busca no banco de dados conforme o título da notícia.
  07. Função `search_by_date`, realiza uma busca no banco de dados segundo a data da notícia.
  08. Função `search_by_tag`, realiza uma busca no banco de dados conforme as tags da notícia.
  09. Função `search_by_category`, realiza uma busca no banco de dados segundo a categoria da notícia.
  10. Função `top_5_news`, que lista as notícias mais populares, o critério é o número de comentários.
  11. Função `top_5_categories`, que lista as categorias com maior ocorrência no banco de dados.
  12. Função `analyzer_menu`, o menu do programa, dando opções que utilizam as funcionalidades criadas anteriormente.
  13. Implementar as funcionalidades do menu criado no requisito 12.

---
## O que foi utilizado?
 - Python.
 - Parsel, Requests, BeutifulSoup4.
 - Python-Decouple.
 - Pymongo.
 - Pytest, Pytest-Mock, Pytest-Json.
 - Flake8, Black, Wheel.
 - Dockerfile e Docker-Compose (Construção do Banco de Dados)

---
## Rodando Localmente
1. Clone o repositório e abra a pasta raiz.
2. Ative o ambiente virtual do python pelo terminal:
  ```bash
    python3 -m venv .venv & source .venv/bin/activate
  ```
3. Instale as dependências pelo terminal:
  ```bash
    python3 -m pip install -r dev-requirements.txt
  ```
4. Inicie o banco de dados através do docker pelo terminal:
  ```bash
    docker-compose up -d mongodb
  ```
5. No terminal, execute menu.py:
  ```bash
    python3 -m tech_news/menu.py
  ```