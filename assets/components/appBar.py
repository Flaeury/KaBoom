import flet as ft


def create_app_bar():

    return ft.AppBar(
        bgcolor='#0C4B85',

        toolbar_height=70,

        title=ft.Text('TechTemple', color=ft.colors.ORANGE_600,
                      font_family='LuckiestGuy'),
        # logo da plataforma
        leading=ft.Icon(name=ft.icons.VIDEOGAME_ASSET_OUTLINED,
                        color=ft.colors.ORANGE_600, size=50),
        leading_width=100,
        actions=[
            # icone do carrinho - adicionar a mudança de rota ainda
            ft.IconButton(ft.icons.SHOPPING_CART_ROUNDED,
                          tooltip='Ir para o carrinho',
                          icon_color='#FFFFFF',
                          icon_size=30,
                          ),

        ],
    )
