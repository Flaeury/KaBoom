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
                                          on_click=lambda _: page.go("/cart"),
                                          ),

                        ],
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
                                ft.ElevatedButton(
                                    "Voltar", on_click=lambda _: page.go("/")),

                            ],
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
