import flet as ft
import dash
from flet import *


def main(page: ft.Page):
    page.padding = 50,
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text(
                            value='TechTemple',
                            color='#FFFFFF',
                            font_family='assets/fonts/BungeeSpice',
                            size=45,
                            italic=True,
                        ),
                        leading=ft.Icon(
                            name=ft.icons.GAMEPAD_ROUNDED,
                            size=25,
                            color='#FF7E20',
                            scale=10
                        ),
                        bgcolor='#0C4B85',
                        actions=[
                            ft.IconButton(ft.icons.SHOPPING_CART_ROUNDED,
                                          tooltip='Ir para o carrinho',
                                          icon_color='#FFFFFF',
                                          icon_size=30,
                                          on_click=lambda _: page.go("/cart"),
                                          ),
                        ],
                    ),
                    dash.create_product_grid(["assets/img/xbox/", "assets/img/placavideo/",
                                              "assets/img/notebooks/", "assets/img/playstation/", "assets/img/processadores/", "assets/img/assistentesvirtuais/", "assets/img/tablets/"]),
                ],
            )
        )
        if page.route == "/cart":
            page.views.append(
                ft.View(
                    "/cart",
                    [
                        ft.AppBar(
                            title=ft.Text(
                                value='TechTemple',
                                color='#FFFFFF',
                                font_family='assets/fonts/BungeeSpice',
                                size=45,
                                italic=True,
                            ),
                            leading=ft.Icon(
                                name=ft.icons.GAMEPAD_ROUNDED,
                                size=25,
                                color='#FF7E20',
                                scale=10
                            ),
                            bgcolor='#0C4B85',
                            toolbar_height=70,

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
