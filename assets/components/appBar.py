import flet as ft

#Criar barra superior da pagina inicial

def create_app_bar_dashboard(page):
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

#Criar barra superior da pagina do carrinho

def create_app_bar_cart(page):
    return ft.AppBar(
        bgcolor='#0C4B85',
        toolbar_height=65,

        title=ft.Text("Carrinho", color='#FF7E20',
                      font_family='BungeeSpice'),
    )

#Criar barra superior da pagina de pagamento

def create_app_bar_payment(page):
    return ft.AppBar(
        bgcolor='#0C4B85',
        toolbar_height=65,
        title=ft.Text("Pagamento", color='#FF7E20',
                      font_family='BungeeSpice'),

    )

#Criar barra superior do checkout

def create_app_bar_finalcheckout(page):
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
                    ft.icons.HOME,
                    tooltip='Voltar para a página inicial',
                    icon_color='#FFFFFF',
                    icon_size=30,
                    on_click=lambda _: page.go("/")
                )
        ]
    )