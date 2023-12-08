from flet import *
import flet as ft
import os
import random


def main(page: ft.Page):
    # Lista de diretórios
    folder_paths = ["assets/img/xbox/",
                    "assets/img/notebooks/", "assets/img/playstation/"]

    def orderBtn():
        pass

    # Criar um GridView
    gridView = ft.GridView(
        expand=1,
        runs_count=3,
        max_extent=240,
        child_aspect_ratio=1.0,
        spacing=20,
        run_spacing=20,
        on_scroll=None,
    )

    # Iterar sobre os diretórios
    for folder_path in folder_paths:
        for _ in range(4):  # Criar quatro cards em cada linha
            files = os.listdir(folder_path)
            file_name = random.choice(files)
            if os.path.isfile(os.path.join(folder_path, file_name)):
                product_name, ext = os.path.splitext(file_name)
                product = {
                    "name": product_name,
                    "image": os.path.join(folder_path, file_name),
                    "estoque": random.randint(1, 10),
                    "price": random.randint(2455, 5990),
                    # "rating": round(random.uniform(2, 5), 1)
                }

                # Adicionar um Card ao GridView
                gridView.controls.append(
                    ft.Card(
                        elevation=30,
                        content=ft.Container(
                            bgcolor="white",
                            width=240,
                            height=280,
                            content=ft.Column([
                                ft.Image(src=product["image"],
                                         width=160,
                                         height=140),
                                ft.Container(
                                    padding=10,
                                    width=240,
                                    height=180,
                                    bgcolor="#a0a0a0",
                                    border_radius=ft.border_radius.only(
                                        top_left=10, top_right=10
                                    ),
                                    content=ft.Column([
                                        ft.Text(product["name"],
                                                size=16,
                                                weight=ft.FontWeight.BOLD),
                                        ft.Text(f"R$ {product['price']}",
                                                size=14),
                                        ft.Text(f"Estoque: {product['estoque']}",
                                                size=14),
                                        ft.ElevatedButton(
                                            text="Comprar",
                                            bgcolor="#4CAF50",
                                            color="white",
                                            on_click=orderBtn
                                        )
                                    ])
                                )
                            ])
                        )
                    )
                )

    # Adicionar o GridView à página
    page.add(gridView)


# Iniciar o aplicativo
ft.app(target=main)


# import flet as ft
# from assets.components.appBar import create_app_bar
# from assets.components.navigationRail import create_navigation_rail


# def main(page: ft.Page):
#     # AppBar
#     app_bar = create_app_bar()

#     # NavigationRail
#     # navigation_rail = create_navigation_rail()

#     # Responsive Cards
#     cards = ft.Row(
#         [
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable without Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         bgcolor=ft.colors.GREEN_200,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         on_click=lambda e: print(
#                             "Clickable without Ink clicked!"),
#                     ),
#                 ]
#             ),
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable with Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         bgcolor=ft.colors.CYAN_200,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         ink=True,
#                         on_click=lambda e: print(
#                             "Clickable with Ink clicked!"),
#                     ),
#                 ]
#             ),
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable transparent with Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         ink=True,
#                         on_click=lambda e: print(
#                             "Clickable transparent with Ink clicked!"),
#                     ),
#                 ]
#             ),
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable with Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         bgcolor=ft.colors.CYAN_200,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         ink=True,
#                         on_click=lambda e: print(
#                             "Clickable with Ink clicked!"),
#                     ),
#                 ]
#             ),
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable transparent with Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         ink=True,
#                         on_click=lambda e: print(
#                             "Clickable transparent with Ink clicked!"),
#                     ),
#                 ]
#             ),
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable without Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         bgcolor=ft.colors.GREEN_200,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         on_click=lambda e: print(
#                             "Clickable without Ink clicked!"),
#                     ),
#                 ]
#             ),
#             ft.Column(
#                 [
#                     ft.Container(
#                         content=ft.Text("Clickable with Ink"),
#                         margin=10,
#                         padding=10,
#                         alignment=ft.alignment.center,
#                         bgcolor=ft.colors.CYAN_200,
#                         width=190,
#                         height=245,
#                         border_radius=10,
#                         ink=True,
#                         on_click=lambda e: print(
#                             "Clickable with Ink clicked!"),
#                     ),
#                 ]
#             ),


#         ],
#         alignment=ft.MainAxisAlignment.CENTER,
#         spacing=10,
#     )

#     page.add(
#         app_bar,
#         ft.Row(
#             [
#                 # navigation_rail,
#                 cards],
#             expand=False,
#         )
#     )


# # Inicializar o aplicativo
# ft.app(target=main)
