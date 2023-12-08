import flet as ft
import os
from pathlib import Path
import random
from flet import *
from assets.components.appBar import create_app_bar


def main(page: Page):
    appBar = create_app_bar()
    page.scroll = "auto"
    # page.auto_scroll = "True"
    page.bgcolor = ft.colors.GREY_200
    page.padding = 50
    page.update()

    page.fonts = {
        'LuckiestGuy': 'fonts/LuckiestGuy-Regular.ttf',
    }

    folder_paths = ["assets/img/xbox/", "assets/img/placavideo/",
                    "assets/img/notebooks/", "assets/img/playstation/", "assets/img/processadores/", "assets/img/assistentesvirtuais/", "assets/img/tablets/"]

    mycounter = Text(1, size=12, weight="bold")
    precoSelecionado = Text(weight="bold")
    listOrder = Column(scroll="always")

    itemselectimage = Image(width=100, height=50)
    itemselectname = Text()
    itemselectprice = Text()

    yourOrder = []

    def decrementBtn(e):
        mycounter.value -= 1
        precoSelecionado.value = int(
            mycounter.value) * int(itemselectprice.value)
        if mycounter.value < 1:
            mycounter.value = 1
            precoSelecionado.value = int(
                mycounter.value) * int(itemselectprice.value)
        page.update()

    def incrementBtn(e):
        mycounter.value += 1
        precoSelecionado.value = int(
            mycounter.value) * int(itemselectprice.value)
        print(precoSelecionado)
        page.update()

    def orderBtn(e):
        mycounter.value += 1
        itemselectprice.value = e.control.data['price']
        itemselectname.value = e.control.data['name']
        itemselectimage.src = e.control.data['image']

        precoSelecionado.value = int(
            mycounter.value) * int(itemselectprice.value)
        page.update()

        page.update()

    gridView = ft.GridView(
        child_aspect_ratio=1.0,
        expand=1,
        runs_count=5,
        max_extent=260,

        auto_scroll=True,
        spacing=170,
        padding=20,
        run_spacing=100,
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
                    # "rating": round(random.uniform(2, 5), 1)
                }

                gridView.controls.append(
                    ft.Card(

                        elevation=10,
                        content=ft.Container(
                            bgcolor="white",
                            width=280,
                            height=300,
                            content=ft.Column([
                                ft.Image(src=product["image"],

                                         width=180,
                                         height=145),
                                ft.Container(
                                    padding=10,
                                    width=280,
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
                                                height=40,
                                                on_click=orderBtn
                                            ),


                                        ], alignment="center"),


                                    ])
                                )
                            ])
                        )
                    )
                )
                page.update()

    page.add(
        appBar,

        Column([

            gridView,
        ], scroll="always",),
    ),


ft.app(target=main, assets_dir="assets")
