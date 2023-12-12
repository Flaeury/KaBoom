import json
import flet as ft

itemselectedimage = ft.Image(width=100, height=50)
itemselectedname = ft.Text()
itemselectedprice = ft.Text()
itemselectednamestock = ft.Text()

table = ft.DataTable(
    columns=['image', 'name', 'price', 'estoque'],
    rows=[]
)

#Definir instância da pagina

def init(p):
    global page
    page = p

#Adicionar produtos ao carrinho

def addToCartBtn(e):
    userOrder = []
    quantidade = 1

    if type(e.control.key) is dict:
        itemselectedname.value = e.control.key['name']
        itemselectedprice.value = e.control.key['price']
        itemselectedimage.src = e.control.key['image']
        itemselectednamestock.value = e.control.key['estoque']

        product_details = {
            "image": itemselectedimage.src,
            "name": itemselectedname.value,
            "price": itemselectedprice.value,
            "estoque": itemselectednamestock.value
        }

        # Adiciona a linha na tabela de dados
        table.rows.append([product_details['image'], product_details['name'], product_details['price'], product_details['estoque']])


        dlg = ft.AlertDialog(
            title=ft.Text("SUCESSO!"),
            content=ft.Text("Produto adicionado ao carrinho."),
            shape=ft.BeveledRectangleBorder(radius=4))
        page.dialog = dlg
        dlg.open = True
        page.update()

    else:
        print("Error: Missing data in the control.")

#Criar card do produto no carrinho

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
                                on_click=addToCartBtn
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

#Criar grade de produtos

def create_product_grid(file_path):
    gridView = ft.GridView(
        child_aspect_ratio=1.0,
        expand=1,
        runs_count=5,
        max_extent=330,
        spacing=100,
        padding=30,
        run_spacing=60,
    )

    with open(file_path, 'r', encoding="utf-8") as f:
        # Lê todo o conteúdo do arquivo
        content = f.read()

        # Converte o conteúdo para uma lista de dicionários
        products = [json.loads(line.strip())
                    for line in content.split('\n') if line.strip()]

        for product in products:
            gridView.controls.append(create_product_card(product))

    correcaoTela = ft.Container(bgcolor='gray', height=1)
    correcaoTela2 = ft.Container(bgcolor='gray', height=1)
    gridView.controls.append(correcaoTela)
    gridView.controls.append(correcaoTela2)

    return gridView


file_path = "./assets/BD/products.txt"
product_grid = create_product_grid(file_path)
