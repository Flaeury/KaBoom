import flet as ft
import dashboard
from flet import *
from assets.components.appBar import create_app_bar_cart, create_app_bar_dashboard, create_app_bar_payment, create_app_bar_finalcheckout
import os
import cart
import payment
from finalcheckout import checkoutCreditCard, checkoutPix

# Aspectos iniciais da pagina


def main(page: ft.Page):
    dashboard.init(page) # Para tornar o page usável em outras abas
    page.title = "KaBoom!"
    page.theme_mode = ft.ThemeMode.DARK
    page.fonts = {
        'BungeeSpice': 'fonts/BungeeSpice-Regular.ttf',
    }
    page.padding = 50
    
    # page.window_full_screen=True

# Alterar visualização da pagina com base na rota

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    create_app_bar_dashboard(page), # AppBar dashboard

                    dashboard.create_product_grid("./assets/BD/products.txt"), # Cria a dashboard com os produtos
                ],
            )

        )
        if page.route == "/cart":

            page.views.append(
                # Aqui é onde ela deve aparecer
                ft.View(
                    route="/cart",
                    controls=[   # AppBar do carrinho
                        create_app_bar_cart(page),
                        cart.selected_products(dashboard.table), # Gerar cards do carrinho
                        cart.change_screen(page), # Botão para ir para o pagamento
                    ],

                )
            )
        elif page.route == "/payment":
            mensage, options = payment.paymentOptions(page)
            page.views.append(
                ft.View(
                    route="/payment",
                    controls=[ # AppBar da aba de pagamentos
                        create_app_bar_payment(page),
                        options, # Opções de pagamento
                        mensage
                    ],

                )
            )
        elif page.route == "/finalcheckoutPIX":
            page.views.append(
                ft.View(
                    route="/finalcheckoutPIX",
                    controls=[ # AppBar da aba final
                        create_app_bar_finalcheckout(page),
                        checkoutPix() #Tela final opcao 1
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        elif page.route == "/finalcheckoutCREDITCARD":
            page.views.append(
                ft.View(
                    route="/finalcheckoutCREDITCARD",
                    controls=[ # AppBar da aba final
                        create_app_bar_finalcheckout(page),
                        checkoutCreditCard() #Tela final opcao 2
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        page.update()

# Navegar para a visualização no topo da pilha

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets")
