from flet import *
import flet as ft
import dashboard

# Definir opções de pagamento


def paymentOptions(page):  # Pass the page object as an argument

    def radiogroup_changed(e):
        # Se escolher PIX
        if e.control.value == 'PIX':
            mensage.controls.clear()
            mensageQrCOde = ft.TextField(
                width="auto",
                label='CLIQUE NO BOTÃO PARA GERAR O QR CODE DO PAGAMENTO',
                disabled=True
            )
            endButton = ft.Row([
                ft.Container(bgcolor='gray'),
                change_screen_pix(page)  # Pass the page object
            ])

            mensage.controls.append(mensageQrCOde)
            mensage.controls.append(endButton)
            mensage.update()

        # Se escolher cartão
        if e.control.value == "CARTÃO DE CRÉDITO":  # Fix the label to match the radio value
            mensage.controls.clear()

            endButton = ft.Column([
                ft.Container(bgcolor='gray'),
                change_screen_creditCard(page)  # Pass the page object
            ])

            mensage.controls.append(create_creditCard())
            mensage.controls.append(endButton)
            mensage.update()

    options = ft.RadioGroup(
        content=ft.Column([
            ft.Container(
                padding=12,
                bgcolor="#7D7D7D",
                border_radius=ft.border_radius.only(
                    top_left=7, top_right=7, bottom_left=7, bottom_right=7,
                ),
                height=55,
                content=ft.Column([
                    # opção PIX
                    ft.Radio(value="PIX",  label="PIX (5% DE DESCONTO)",
                             fill_color=ft.colors.WHITE),

                ]),
            ),
            ft.Container(
                padding=15,
                bgcolor="#7D7D7D",
                border_radius=ft.border_radius.only(
                    top_left=7, top_right=7, bottom_left=7, bottom_right=7,
                ),
                height=55,
                content=ft.Column([
                    # opção CARTÃO
                    ft.Radio(value="CARTÃO DE CRÉDITO",
                             label="CARTÃO DE CRÉDITO", fill_color=ft.colors.WHITE)

                ]),
            ),
        ]),
        on_change=radiogroup_changed
    )
    mensage = ft.Column(width=470)

    return mensage, options


def create_creditCard():
    name = ft.TextField(
        width=410,  # Ajuste da largura
        label='Nome do Titular',
        border=ft.InputBorder.NONE,
        color="#5B5B5B",
        filled=True,
        height=65,
        bgcolor="#FFFFFF",
        border_color="TRANSPARENT",
        capitalization=ft.TextCapitalization.CHARACTERS,
    )

    cardNumber = ft.TextField(
        width=415,  # Ajuste da largura
        label='Número do Cartão',
        border=ft.InputBorder.NONE,
        filled=True,
        height=65,
        color="#5B5B5B",
        max_length=16,
        bgcolor="#FFFFFF",
        border_color="TRANSPARENT",
        input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
    )
    cvv = ft.TextField(
        width=185,  # Ajuste da largura
        label='CVV',
        height=65,
        color="#5B5B5B",
        max_length=3,
        password=True,
        border_color="TRANSPARENT",
        border=ft.InputBorder.NONE,
        filled=True,

        can_reveal_password=True,
        bgcolor="#FFFFFF",
        input_filter=ft.InputFilter(
                    allow=True,  regex_string="[0-9]"),
    )
    valDate = ft.TextField(
        width=180,  # Ajuste da largura
        label='Data de Validade',
        height=65,
        border_color="TRANSPARENT",
        max_length=4,
        color="#5B5B5B",
        border=ft.InputBorder.NONE,
        filled=True,
        bgcolor="#FFFFFF",
        input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
    )
    return ft.Card(
        content=ft.Container(
            padding=padding.only(43, 30, 43, 18),
            width="auto",
            alignment=ft.alignment.center,
            bgcolor="#464646",
            height="auto",
            border_radius=ft.border_radius.only(
                top_left=7, top_right=7, bottom_left=7, bottom_right=7,),
            content=ft.Container(
                ft.Column(
                    [  # dadosCartao,
                        cardNumber,
                        name,
                        ft.Row([
                            cvv,
                            valDate
                        ], alignment='left')
                    ])
            )
        )
    )


def change_screen_pix(page):
    return ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.CHECK), ft.Text("GERAR CHAVE ALEATÓRIA")], alignment="center", spacing=5),
        bgcolor="#0c4b85",

        shape=ft.RoundedRectangleBorder(radius=5),
        width=260,
        on_click=lambda _: page.go("/")
    )


def change_screen_creditCard(page):
    return ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.CHECK), ft.Text("UTILIZAR CARTÃO CADASTRADO")], alignment="center", spacing=5),
        bgcolor="#0c4b85",

        shape=ft.RoundedRectangleBorder(radius=5),
        width=280,
        on_click=lambda _: page.go("/")
    )
