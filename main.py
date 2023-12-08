import flet as ft
from dashboard import main


def main(page: ft.Page):
    dashboard = main()

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
                                    ft.IconButton(
                                            ft.icons.SHOPPING_CART_ROUNDED,
                                            tooltip='Ir para o carrinho',
                                            icon_color='#FFFFFF',
                                            icon_size=30,
                                            on_click=lambda _: page.go("/cart")
                                        )
                                    ]
                                ),
                    dashboard,
                ],
            ),
        ),

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
                            actions=[
                                    ft.IconButton(
                                            ft.icons.SHOPPING_CART_ROUNDED,
                                            tooltip='Ir para o carrinho',
                                            icon_color='#FFFFFF',
                                            icon_size=30,
                                            on_click=lambda _: page.go("/cart")
                                        )
                                    ]
                                ),
                        # ALGO AQUI PARA O CART
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
