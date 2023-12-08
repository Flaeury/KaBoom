import flet as ft

def appBar():
    return ft.AppBar(
        bgcolor='#0C4B85',

        title=ft.Text('TechTemple', color=ft.colors.ORANGE_600, font_family='LuckiestGuy'),
        #logo da plataforma
        leading=ft.Icon(name=ft.icons.VIDEOGAME_ASSET_OUTLINED, color=ft.colors.ORANGE_600, size=50),
        leading_width=100,
        actions=[
            #icone do carrinho - adicionar a mudança de rota ainda
            ft.IconButton(ft.icons.SHOPPING_CART_ROUNDED, tooltip='Ir para o carrinho', icon_color='#FFFFFF', icon_size=30),
        ]
    )

def main(page: ft.Page):
    page.fonts = {
        'LuckiestGuy':'fonts/LuckiestGuy-Regular.ttf',
    }
    page.theme_mode = ft.ThemeMode.LIGHT
    appbar = appBar()
    page.add(appbar)


ft.app(target=main)
