import flet as ft
import dash
from flet import *
from assets.components.appBar import create_app_bar

def main(page: ft.Page):
    page.fonts = {
        'BungeeSpice': 'fonts/BungeeSpice-Regular.ttf',
    }
    page.padding = 50
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [   # AppBar Principal
                    create_app_bar(page),
                    # Página Principal
                    dash.create_product_grid(["assets/img/xbox/", "assets/img/placavideo/",
                                              "assets/img/notebooks/", "assets/img/playstation/", "assets/img/processadores/", "assets/img/assistentesvirtuais/", "assets/img/tablets/"]),
                ],
            )
        )
        if page.route == "/cart":
            page.views.append(
                ft.View(
                    "/cart",
                    [   # AppBar do carrinho
                        ft.AppBar(
                            bgcolor='#0C4B85',
                            toolbar_height=70,
                            title=ft.Text("Carrinho", color=ft.colors.ORANGE_600,
                                          font_family='BungeeSpice'),
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets")
