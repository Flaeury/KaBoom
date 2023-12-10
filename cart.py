import json
import flet as ft
from flet import *


def create_product_card(product):
    return ft.Card(
        elevation=10,
        content=ft.Container(
            bgcolor="#f5f5f5",
            width=450,
            height=190,
            border_radius=ft.border_radius.only(
                top_left=7, top_right=7, bottom_left=7, bottom_right=7,
            ),
            content=ft.Row([
                ft.Image(src=product["image"],
                         width=250,
                         height=180),
                ft.Container(
                    padding=10,
                    width=450,

                    height=190,
                    bgcolor="#f5f5f5",

                    content=ft.Column([

                        ft.Text(product["name"],
                                size=18,
                                color=ft.colors.ORANGE_600,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"R$ {product['price']}",
                                size=17,
                                color=ft.colors.BLACK, weight="bold"),
                        ft.Text(f"Estoque: {product['estoque']}",
                                size=17,
                                color=ft.colors.BLACK),
                    ])
                ),
                ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.IconButton(
                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                            icon_color="red400",
                            icon_size=40,
                            tooltip="Apagar produto",
                        ),
                    ])
                )
            ])
        )
    )


file_path = "./assets/BD/checkoutBD.txt"


def create_cards_from_file(file_path):
    cards = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:

            product_dict = json.loads(line.strip())
            cards.append(create_product_card(product_dict))
    return cards


def selected_products():
    return ft.ListView(
        # auto_scroll=True,
        spacing=10,
        padding=20,
        expand=1,
        controls=create_cards_from_file("./assets/BD/checkoutBD.txt")
    )


def change_screen(page):
    return ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.SHOPPING_CART_CHECKOUT), ft.Text("Finalizar Compra")], alignment="center", spacing=5
        ),
        bgcolor="#0c4b85",

        shape=ft.RoundedRectangleBorder(radius=5),
        width=190,
        on_click=lambda _: page.go("/payment")
    )
