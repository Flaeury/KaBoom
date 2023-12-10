import flet as ft


def create_app_bar_dash(page):
    return ft.AppBar(

        title=ft.Text(
            value='KaBoom!',
            color='#FFFFFF',
            font_family='BungeeSpice',
            size=45,

            italic=True,
        ),
        leading=ft.Icon(
            name=ft.icons.GAMEPAD_ROUNDED,
            size=40,
            color='#FF7E20',
            scale=10
        ),
        bgcolor='#0C4B85',
        actions=[
                ft.IconButton(
                    ft.icons.SHOPPING_CART_ROUNDED,
                    tooltip='Ir para o carrinho',
                    icon_color='#FFFFFF',
                    icon_size=30,
                    on_click=lambda _: page.go("/cart")
                )
        ]
    )


def create_app_bar_cart(page):
    return ft.AppBar(
        bgcolor='#0C4B85',
        toolbar_height=65,

        title=ft.Text("Carrinho", color='#FF7E20',
                      font_family='BungeeSpice'),
        # actions=[
        #         ft.ElevatedButton(
        #             style=ft.ButtonStyle(padding=ft.padding.all(
        #                 1), shape=ft.RoundedRectangleBorder(radius=7),),

        #             # icon="money",
        #             # icon_color="green400",
        #             text="Finalizar",
        #             bgcolor="#ff6b00",
        #             color="white",
        #             width=150,
        #             height=45,
        #             on_click=lambda _: page.go("/payment")
        #         )
        # ]
    )


def create_app_bar_payment(page):
    return ft.AppBar(
        bgcolor='#0C4B85',
        toolbar_height=65,
        title=ft.Text("Pagamento", color='#FF7E20',
                      font_family='BungeeSpice'),

    )
