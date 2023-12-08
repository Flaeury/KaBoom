import flet as ft
import dash


def main(page: ft.Page):
    page.title = "Routes Example"

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
                        leading=ft.Icon(name=ft.icons.VIDEOGAME_ASSET_OUTLINED,
                                        color=ft.colors.ORANGE_600, size=50),
                        leading_width=100,
                        actions=[
                            ft.IconButton(ft.icons.SHOPPING_CART_ROUNDED,
                                          tooltip='Ir para o carrinho',
                                          icon_color='#FFFFFF',
                                          icon_size=30,
                                          on_click=lambda _: page.go("/store"),
                                          ),
                        ],
                    ),
                    dash.create_product_grid(["assets/img/xbox/",
                                              "assets/img/notebooks/", "assets/img/playstation/"]),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(
                            bgcolor='#0C4B85',
                            toolbar_height=70,
                            title=ft.Text("Carrinho", color=ft.colors.ORANGE_600,
                                          font_family='LuckiestGuy'),
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
