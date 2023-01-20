# Requisito 12
import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def analyzer_menu():
    """Seu código deve vir aqui"""
    options = {
        "0": get_tech_news_caller,
        "1": search_by_title_caller,
        "2": search_by_date_caller,
        "3": search_by_tag_caller,
        "4": search_by_categoty_caller,
        "5": top_5_news,
        "6": top_5_categories,
        "7": close_app,
    }

    print(
        "Selecione uma das opções a seguir:",
        " 0 - Popular o banco com notícias;",
        " 1 - Buscar notícias por título;",
        " 2 - Buscar notícias por data;",
        " 3 - Buscar notícias por tag;",
        " 4 - Buscar notícias por categoria;",
        " 5 - Listar top 5 notícias;",
        " 6 - Listar top 5 categorias;",
        " 7 - Sair.",
        sep='\n'
    )
    choice = input()
    try:
        options[choice]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)


def get_tech_news_caller():
    input("Digite quantas notícias serão buscadas:")


def search_by_title_caller():
    input("Digite o título:")


def search_by_date_caller():
    input("Digite a data no formato aaaa-mm-dd:")


def search_by_tag_caller():
    input("Digite a tag:")


def search_by_categoty_caller():
    input("Digite a categoria:")


def close_app():
    print("Encerrando script")


if __name__ == "__main__":
    analyzer_menu()
