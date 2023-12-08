import flet as ft


def create_app_bar(page):
    return ft.AppBar(
        title=ft.Text(
                        value='TechTemple',
                        color='#FFFFFF',
                        font_family='BungeeSpice',
                        size=45,
                        italic=True,
        ),
        leading=ft.Icon(
                        name=ft.icons.GAMEPAD_ROUNDED,
                        size=41,
                        color='#FF7E20',
                        scale=10
            ),
        bgcolor='#0C4B85',
        actions=[
                ft.IconButton(
                    ft.icons.SHOPPING_CART_ROUNDED,
                    tooltip='Ir para o carrinho',
                    icon_color='#FFFFFF',
                    icon_size=30,
                    on_click=lambda _: page.go("/cart")
                )
        ]
    )
