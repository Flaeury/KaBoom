import flet as ft
import os
from pathlib import Path
import random
from flet import *


def create_product_card(product):
    return ft.Card(
        elevation=10,
        content=ft.Container(
            bgcolor="white",
            width=220,
            height=280,
            content=ft.Column([
                ft.Image(src=product["image"],
                         width="auto",
                         height=165),
                ft.Container(
                    padding=10,
                    width="auto",
                    height=185,
                    bgcolor="#a0a0a0",
                    border_radius=ft.border_radius.only(
                        top_left=10, top_right=10, bottom_left=5, bottom_right=5,
                    ),
                    content=ft.Column([
                        ft.Text(product["name"],
                                size=16,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"R$ {product['price']}",
                                size=15, weight="bold"),
                        ft.Text(f"Estoque: {product['estoque']}",
                                size=14),

                        ft.Row([
                            ft.ElevatedButton(
                                text="Comprar",
                                bgcolor="#ff6b00",
                                color="white",
                                width=180,
                                height=45,
                                # on_click=orderBtn
                            ),
                        ], alignment="center"),
                    ])
                )
            ])
        )
    )


def create_product_grid(folder_paths):
    gridView = ft.GridView(
        child_aspect_ratio=1.0,
        expand=1,
        runs_count=5,
        max_extent=330,
        spacing=110,
        padding=80,
        run_spacing=80,
    )

    for folder_path in folder_paths:
        files = sorted(os.listdir(folder_path))

        for file_name in files:
            if os.path.isfile(os.path.join(folder_path, file_name)):
                product_name, ext = os.path.splitext(file_name)
                product = {
                    "name": product_name,
                    "image": os.path.join(folder_path, file_name),
                    "estoque": random.randint(1, 10),
                    "price": random.randint(2400, 5990),
                }

                gridView.controls.append(create_product_card(product))

    return gridView
