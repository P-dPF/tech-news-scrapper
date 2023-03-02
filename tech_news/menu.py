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
    "Choose one of the options below:\n 0 - Populate database with news"
    ";\n 1 - Search news by title;\n 2 - Search news by date;\n"
    " 3 - Search news by category;\n "
    "4 - List top 5 categories;\n 5 - Exit.\n"
)

second_menu_options = [
    "Type in the amount of news to fetch:\n",
    "Type in the title:\n",
    "Type in the date in the format yyyy-mm-dd:\n",
    "Type in the category:\n",
]


def execute_menu_option_0():
    amount = input(second_menu_options[0])
    print("Fetching news")
    result = get_tech_news(amount)
    print("News fetched!")
    return result


def exectute_menu_option_1():
    title = input(second_menu_options[1])
    print(search_by_title(title))


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

    while int(main_manu_selected_option) != 5:
        menu_functions_list[int(main_manu_selected_option)]()
        main_manu_selected_option = input(main_menu_options)
