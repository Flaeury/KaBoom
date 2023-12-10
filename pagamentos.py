import flet as ft
import os
from pathlib import Path

#Função que faz a mudança das opções entre pix e cartão
def optionsPayment():

    def radiogroup_changed(e):
        # se escolher PIX
        if e.control.value == 'PIX':
            mensage.controls.clear()
            mensageQrCOde = ft.TextField(
                width= 800,
                label='CLIQUE EM "FINALIZAR A COMPRA" PARA GERAR O QR CODE DO PAGAMENTO',
                disabled=True
                )
            mensage.controls.append(mensageQrCOde)
            mensage.update()
            
        # se escolher cartão
        if e.control.value == "Cartão de crédito":
            mensage.controls.clear()
            name = ft.TextField(
                width= 800,
                label='Nome do Titular',
                capitalization=ft.TextCapitalization.CHARACTERS,
                helper_text='Insira o nome do titular como está grafado no cartão.'
            )

            cardNumber = ft.TextField(
                width= 800,
                label='Número do Cartão',
                keyboard_type=ft.KeyboardType.NUMBER,
                max_length=16,
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                helper_text='Insira o número do cartão sem espaços.',
            )
            cvv = ft.TextField(
                width= 800,
                label='CVV',
                max_length=3,
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                helper_text='Insira o código de segurança.'
            )
            valDate = ft.TextField(
                width= 800,
                label='Data de Validade',
                max_length=4,
                input_filter=ft.InputFilter(allow=True, regex_string="[0-9]"),
                helper_text='Insira a data de validade do cartão sem a barra.',
            )
            dadosCartao = ft.Text(value='DADOS DO CARTÃO')
              
            mensage.controls.append(ft.Column([dadosCartao, name, cardNumber, cvv, valDate]))
            mensage.update()

    pix = ft.Radio(value="PIX", label="PIX")
    creditCard = ft.Radio(value="Cartão de crédito", label="Cartão de crédito")
    mensage = ft.ListView()
    options = ft.RadioGroup(content=ft.Column([
                    pix,
                    creditCard]),
                    on_change=radiogroup_changed)
    return mensage, options

def main(page: ft.Page):
    mensage, option = optionsPayment()
                
    page.add(ft.Text('Selecione seu método de pagamento'), option, mensage)

ft.app(target=main, assets_dir='assets')