import flet as ft
from components.TopBar import TopBar
from components.NavigationRail import NavigationRail

def main(page: ft.Page):
    # Crie instâncias dos componentes
    top_bar = TopBar()
    navigation_rail = NavigationRail()

    # Adicione os componentes à interface do usuário
    page.add(
        ft.Row(
            [
                top_bar,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )

    page.add(
        ft.Column(
            [
                navigation_rail,
                ft.VerticalDivider(width=1),
               
            ],
            expand=True,
        )
    )

# Chame o app com a função main como alvo
ft.app(target=main)
