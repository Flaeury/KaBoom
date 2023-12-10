import flet as ft
import dash
from flet import *
from assets.components.appBar import create_app_bar_cart, create_app_bar_dash, create_app_bar_payment
import os
import cart

def main(page: ft.Page):
    dash.init(page)
    page.fonts = {
        'BungeeSpice': 'fonts/BungeeSpice-Regular.ttf',
    }
    page.padding = 50
    page.title = "KaBoom!"
    # page.window_full_screen=True
    page.theme_mode = ft.ThemeMode.DARK

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    create_app_bar_dash(page),

                    dash.create_product_grid("./assets/BD/products.txt"),
                ],
            )
        )
        if page.route == "/cart":
            page.views.append(
                ft.View(
                    "/cart",
                    [   # AppBar do carrinho
                        create_app_bar_cart(page),

                    ],
                    cart.selected_products(),
                    cart.change_screen(page),
                )
            )
        elif page.route == "/payment":
            page.views.append(
                ft.View(
                    "/cart",
                    [   # AppBar do carrinho
                        create_app_bar_payment(page),

                    ],
                    Text("Pagar")
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
