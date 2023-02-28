import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories

# Requisitos 11 e 12
main_menu_options = (
    "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
    ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
    " 3 - Buscar notícias por categoria;\n "
    "4 - Listar top 5 categorias;\n 5 - Sair."
)

second_menu_options = [
    "Digite quantas notícias serão buscadas:\n",
    "Digite o título:\n",
    "Digite a data no formato aaaa-mm-dd:\n",
    "Digite a categoria:",
]


def execute_menu_option_0():
    amount = input(second_menu_options[0])
    return get_tech_news(amount)


def exectute_menu_option_1():
    title = input(second_menu_options[1])
    return search_by_title(title)


def exectute_menu_option_2():
    date = input(second_menu_options[2])
    print(search_by_date(date))


def exectute_menu_option_3():
    category = input(second_menu_options[3])
    print(search_by_category(category))


def execute_menu_option_4():
    print(top_5_categories())


def execute_menu_option_5():
    sys.stdout.write("Encerrando script\n")


def execute_invalid_menu_option():
    sys.stderr.write("Opção inválida\n")


menu_functions_list = [
    execute_menu_option_0,
    exectute_menu_option_1,
    exectute_menu_option_2,
    exectute_menu_option_3,
    execute_menu_option_4,
    execute_menu_option_5,
    execute_invalid_menu_option,
]


def analyzer_menu():
    main_manu_selected_option = input(main_menu_options)

    menu_options = ["0", "1", "2", "3", "4", "5"]

    if main_manu_selected_option not in menu_options:
        return menu_functions_list[6]()

    if int(main_manu_selected_option) == 5:
        menu_functions_list[5]()

    return menu_functions_list[int(main_manu_selected_option)]()
