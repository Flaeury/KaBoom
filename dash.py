import flet as ft
import os
from pathlib import Path
import random
from flet import *

itemselectedimage = Image(width=100, height=50)
itemselectedname = Text()
itemselectedprice = Text()



def addToCartBtn(e):
    userOrder = []
    quantidade = 1

    print(e.control.key)

    if type(e.control.key) is dict:
        itemselectedname.value = e.control.key['name']
        itemselectedprice.value = e.control.key['price']
        itemselectedimage.src = e.control.key['image']

        userOrder.append([quantidade, itemselectedimage.src,
                         itemselectedname.value, itemselectedprice.value])

        order_string = str(userOrder)

        with open('checkoutBD.txt', 'a', encoding="utf-8") as f:
            conteudo = f.write(f"{order_string}\n")

    else:
        print("Error: Missing data in the control.")



def create_product_card(product):
    return ft.Card(
        elevation=10,
        content=ft.Container(
            bgcolor="white",
            width=210,
            height=80,
            content=ft.Column([
                ft.Image(src=product["image"],
                         width=210,
                         height=135),
                ft.Container(
                    padding=10,
                    width="auto",
                    height=190,
                    bgcolor="#a0a0a0",
                    border_radius=ft.border_radius.only(
                        top_left=10, top_right=10, bottom_left=5, bottom_right=5,
                    ),
                    content=ft.Column([
                        ft.Row([
                            ft.ElevatedButton(
                                text="Comprar",
                                bgcolor="#ff6b00",
                                color="white",
                                width=180,
                                height=45,
                                key=product,
                                on_click=addToCartBtn  # CHAMADA DA FUNÇÃO COM ERRO
                            ),
                        ], alignment="center"),
                        ft.Text(product["name"],
                                size=17,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"R$ {product['price']}",
                                size=16, weight="bold"),
                        ft.Text(f"Estoque: {product['estoque']}",
                                size=15),
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
        spacing=100,
        padding=30,
        run_spacing=60,
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
                    "price": random.randint(2300, 6990),
                }

                gridView.controls.append(create_product_card(product))
    correcaoTela = ft.Container(bgcolor='dark', height=1)
    gridView.controls.append(correcaoTela)

    return gridView
