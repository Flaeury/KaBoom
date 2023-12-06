import flet as ft


def create_app_bar():
    return ft.AppBar(
        leading=ft.Icon(name=ft.icons.GAMES_OUTLINED, color=ft.colors.BLUE),
        leading_width=40,
        bgcolor=ft.colors.SURFACE_VARIANT,
        title=ft.Text("TechTemple"),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.SHOPPING_CART_OUTLINED),
        ],
    )
