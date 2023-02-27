import sys

# Requisitos 11 e 12
menu_options = (
    "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
    ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
    " 3 - Buscar notícias por categoria;\n "
    "4 - Listar top 5 categorias;\n 5 - Sair."
)

second_options = [
    "Digite quantas notícias serão buscadas:\n",
    "Digite o título:\n",
    "Digite a data no formato aaaa-mm-dd:\n",
    "Digite a categoria:",
]


def analyzer_menu():
    selected_option = input(menu_options)

    if selected_option and 0 <= int(selected_option) <= 3:
        selected_option = input(second_options[selected_option])

    elif selected_option == "4":
        pass

    elif selected_option == "5":
        pass

    else:
        sys.stderr.write("Opção inválida")
