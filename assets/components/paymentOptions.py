import flet as ft
import os

#Função que faz a mudança das opções entre pix e cartão
def paymentOptions():

    def radiogroup_changed(e):
        # se escolher PIX
        if e.control.value == 'PIX':
            mensage.controls.clear()
            mensageQrCOde = ft.TextField(
                width=610,
                label='CLIQUE EM "FINALIZAR A COMPRA" PARA GERAR O QR CODE DO PAGAMENTO',
                disabled=True
                )
            mensage.controls.append(mensageQrCOde)
            mensage.update()
            
        # se escolher cartão
        if e.control.value == "Cartão de crédito":
            mensage.controls.clear()
            dadosCartao = ft.Text(value=f'\nDADOS DO CARTÃO')

            name = ft.TextField(
                width= 610,
                label='Nome do Titular',
                capitalization=ft.TextCapitalization.CHARACTERS,
                helper_text='Insira o nome do titular como está grafado no cartão.'
            )

            cardNumber = ft.TextField(
                width= 610,
                label='Número do Cartão',
                keyboard_type=ft.KeyboardType.NUMBER,
                max_length=16,
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                helper_text='Insira o número do cartão sem espaços.',
            )
            cvv = ft.TextField(
                width= 300,
                label='CVV',
                max_length=3,
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                helper_text='Insira o código de segurança.'
            )
            valDate = ft.TextField(
                width= 300,
                label='Data de Validade',
                max_length=4,
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                helper_text='Insira a data de validade do cartão sem a barra.',
            )
              
            mensage.controls.append(ft.Column([
                                        dadosCartao,
                                        cardNumber,
                                        name,
                                        ft.Row([
                                            cvv,
                                            valDate
                                        ], alignment='left')
                                    ])
                                )
            mensage.update()

    pix = ft.Radio(value="PIX", label="PIX (5% DE DESCONTO)")
    creditCard = ft.Radio(value="Cartão de crédito", label="Cartão de crédito")
    mensage = ft.ListView()
    options = ft.RadioGroup(content=ft.Column([
                    pix,
                    creditCard]),
                    on_change=radiogroup_changed)
    return mensage, options