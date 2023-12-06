import flet as ft
from assets.components.appBar import create_app_bar
from assets.components.navigationRail import create_navigation_rail


def main(page: ft.Page):
    # AppBar
    app_bar = create_app_bar()

    # NavigationRail
    navigation_rail = create_navigation_rail()

    # Responsive Cards
    cards = ft.Row(
        [
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable without Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.GREEN_200,
                        width=190,
                        height=245,
                        border_radius=10,
                        on_click=lambda e: print(
                            "Clickable without Ink clicked!"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.CYAN_200,
                        width=190,
                        height=245,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print(
                            "Clickable with Ink clicked!"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable transparent with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        width=190,
                        height=245,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print(
                            "Clickable transparent with Ink clicked!"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.CYAN_200,
                        width=190,
                        height=245,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print(
                            "Clickable with Ink clicked!"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable transparent with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        width=190,
                        height=245,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print(
                            "Clickable transparent with Ink clicked!"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable without Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.GREEN_200,
                        width=190,
                        height=245,
                        border_radius=10,
                        on_click=lambda e: print(
                            "Clickable without Ink clicked!"),
                    ),
                ]
            ),
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Clickable with Ink"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.CYAN_200,
                        width=190,
                        height=245,
                        border_radius=10,
                        ink=True,
                        on_click=lambda e: print(
                            "Clickable with Ink clicked!"),
                    ),
                ]
            ),


        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    page.add(
        app_bar,
        ft.Row(
            [
                navigation_rail,
                ft.VerticalDivider(width=0.1), cards],
            expand=True,
        )
    )


# Inicializar o aplicativo
ft.app(target=main)
