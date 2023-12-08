import flet as ft
import dashboard
import cart
import pagamentos


def init(p):
    global page, telas, produtosSelecionados
    page = p
    produtosSelecionados = []
    telas = {
        '0': dashboard.view(),
        '1': cart.view(),
        '2': pagamentos.view()
    }


def route_change(route):
    page.views.clear()
    page.views.append(
        telas[page.route]
    )
    page.update()


def barra_navegacao():
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
