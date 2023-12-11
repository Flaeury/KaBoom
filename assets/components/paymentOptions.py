from flet import *
import flet as ft

#Definir opções de pagamento

def paymentOptions():

    def radiogroup_changed(e):
        # Se escolher PIX
        if e.control.value == 'PIX':
            mensage.controls.clear()
            mensageQrCOde = ft.TextField(
                width=610,
                label='CLIQUE EM "FINALIZAR A COMPRA" PARA GERAR O QR CODE DO PAGAMENTO',
                disabled=True
            )
            mensage.controls.append(mensageQrCOde)
            mensage.update()

        # Se escolher cartão
        if e.control.value == "Cartão de crédito":
            mensage.controls.clear()
            # dadosCartao = ft.Text(value=f'\nDADOS DO CARTÃO')

            name = ft.TextField(
                width=415,  # Ajuste da largura
                label='Nome do Titular',
                border=ft.InputBorder.NONE,
                color="#5B5B5B",
                filled=True,
                height=70,
                bgcolor="#FFFFFF",
                border_color="TRANSPARENT",
                capitalization=ft.TextCapitalization.CHARACTERS,
                # helper_text='Insira o nome do titular como está grafado no cartão.'
            )

            cardNumber = ft.TextField(
                width=415,  # Ajuste da largura
                label='Número do Cartão',
                border=ft.InputBorder.NONE,
                filled=True,
                height=70,
                color="#5B5B5B",
                keyboard_type=ft.KeyboardType.NUMBER,
                max_length=16,
                bgcolor="#FFFFFF",
                border_color="TRANSPARENT",
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                # helper_text='Insira o número do cartão sem espaços.',
            )
            cvv = ft.TextField(
                width=185,  # Ajuste da largura
                label='CVV',
                height=70,
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
                # helper_text='Insira o código de segurança.'
            )
            valDate = ft.TextField(
                width=180,  # Ajuste da largura
                label='Data de Validade',
                height=70,
                border_color="TRANSPARENT",
                max_length=4,
                color="#5B5B5B",
                border=ft.InputBorder.NONE,
                filled=True,
                bgcolor="#FFFFFF",
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                # helper_text='Insira a data de validade do cartão sem a barra.',
            )

            mensage.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=padding.only(45, 25, 45, 20),
                        width="auto",

                        alignment=ft.alignment.center,
                        bgcolor="#828282",
                        height="auto",
                        border_radius=ft.border_radius.only(
                            top_left=10, top_right=10, bottom_left=10, bottom_right=10,
                        ),
                        content=ft.Container(

                            ft.Column(
                                [
                                    # dadosCartao,
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
            )
            mensage.update()

    pix = ft.Radio(value="PIX", label="PIX (5% DE DESCONTO)")
    creditCard = ft.Radio(value="Cartão de crédito", label="Cartão de crédito")
    options = ft.RadioGroup(
        content=ft.Column([
            pix,
            creditCard
        ]),
        on_change=radiogroup_changed
    )
    mensage = ft.ListView(width=470)

    return mensage, options
