import flet as ft
import dashboard
# Card de informação dos produtos

components = {
    'list': ft.Ref[ft.ListView](),
    # add todos os compontens da tela aqui
}


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
                                color=ft.colors.BLACK,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"R$ {product['price']}",
                                size=17,
                                color=ft.colors.BLACK, weight="bold"),
                        ft.Text(f"Estoque: {product['estoque']}",
                                size=17,
                                color=ft.colors.BLACK),
                        ft.Text("spacing", size=5, color="#f5f5f5"),
                        ft.ElevatedButton(
                            text="Remover",
                            icon="delete",
                            width=180,
                            height=40,
                            icon_color="white",
                            bgcolor="#ff6b00",
                            color="white",
                            on_click=removeBtn,
                            key=product,
                        ),
                    ])
                ),

                ft.Container(
                    padding=50,
                    content=ft.Column([

                    ])
                )
            ])
        )
    )

# Remover produto

def removeBtn(e):
    if type(e.control.key) is dict:
        name = e.control.key['name']
        price = e.control.key['price']
        image = e.control.key['image']
        stock = e.control.key['estoque']

        for idx, row in enumerate(dashboard.table.rows):
            if row[1] == name and row[2] == price and row[0] == image and row[3] == stock:
                dashboard.table.rows.pop(idx)
                break
    components['list'].current.controls = create_cards_from_table(dashboard.table)
    dashboard.page.update()


# Exibir produtos em lista na interface grafica

def create_cards_from_table(table):
    cards = []
    for row in table.rows:
        product_dict = {
            "image": row[0],
            "name": row[1],
            "price": row[2],
            "estoque": row[3]
        }
        cards.append(create_product_card(product_dict))
    return cards


# Lista os cards criados

def selected_products(table):
    return ft.ListView(
        # auto_scroll=True,
        spacing=10,
        padding=20,
        expand=1,
        ref=components['list'],
        controls=create_cards_from_table(table)
    )


# Botão para tela de pagamento

def change_screen(page):
    return ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.SHOPPING_CART_CHECKOUT), ft.Text("PAGAR")], alignment="center", spacing=5),
        bgcolor="#0c4b85",

        shape=ft.RoundedRectangleBorder(radius=5),
        width=190,
        on_click=lambda _: page.go("/payment")
    )
