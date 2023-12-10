import json
import flet as ft
from flet import *


def create_product_card(product):
    return ft.Card(
        elevation=10,
        content=ft.Container(
            bgcolor="white",
            width="auto",
            height=150,
            border_radius=ft.border_radius.only(
                top_left=7, top_right=7, bottom_left=7, bottom_right=7,
            ),
            content=ft.Row([
                ft.Image(src=product["image"],
                         width=290,
                         height=230),
                ft.Container(
                    padding=10,
                    width="auto",

                    height=230,
                    bgcolor="white",

                    content=ft.Column([

                        ft.Text(product["name"],
                                size=17,
                                color=ft.colors.ORANGE_600,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"R$ {product['price']}",
                                size=16,
                                color=ft.colors.BLACK, weight="bold"),
                        ft.Text(f"Estoque: {product['estoque']}",
                                size=15,
                                color=ft.colors.BLACK),
                    ])
                )
            ])
        )
    )


def create_cards_from_file(file_path):
    cards = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:

            product_dict = json.loads(line.strip())
            cards.append(create_product_card(product_dict))
    return cards


file_path = "./assets/BD/checkoutBD.txt"


def selected_products():
    return ft.ListView(
        auto_scroll=True,
        spacing=10,
        padding=20,
        expand=1,
        controls=create_cards_from_file("./assets/BD/checkoutBD.txt")
    )
