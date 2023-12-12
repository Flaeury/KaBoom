import flet as ft
import random
import string
import qrcode
import dashboard
import cart

# Gerador de chave PIX aleatória


def generate_random_key(length):
    """Gera uma chave aleatória PIX."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Gerador de QR Code aleatório


def generate_qr_code(data, file_path):
    """Gera um QR Code a partir dos dados fornecidos."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)


# Exemplo de uso:
# Ajuste o comprimento conforme necessário
random_pix_key = generate_random_key(25)
qr_code_file_path = "qr_code.png"

generate_qr_code(random_pix_key, qr_code_file_path)

# Página final 1


def checkoutCreditCard():
    cleanCart()
    return ft.Card(
        elevation=10,
        content=ft.Container(  # Container maior
            bgcolor="#C9C9CA",
            width=600,
            height=200,
            border_radius=ft.border_radius.only(
                    top_left=7, top_right=7, bottom_left=7, bottom_right=7,
            ),
            content=ft.Row([
                ft.Container(  # Container menor para ajudar a alinar tudo
                    padding=10,
                    width=450,
                    height=190,
                    bgcolor="#C9C9CA",
                    content=ft.Row([
                            # Insere o icone de check
                            ft.Icon(ft.icons.CHECK_CIRCLE,
                                    color='#29B207', size=40),
                            # Insere a mensagem
                            ft.Text(value="SUA COMPRA FOI FINALIZADA.\nFICAMOS MUITO FELIZES EM TER VOCÊ AQUI!\nVOLTE SEMPRE!",
                                    size=18,
                                    color=ft.colors.BLACK,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.START)
                    ])
                ),
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
    )

# Página final 2


def checkoutPix():
    cleanCart()
    return ft.Card(
        elevation=10,
        content=ft.Container(  # Container maior
            bgcolor="#f5f5f5",
            width=600,
            height=400,
            border_radius=ft.border_radius.only(
                top_left=7, top_right=7, bottom_left=7, bottom_right=7,
            ),
            content=ft.Column([
                ft.Row([
                    # Insere o icone de check
                    ft.Icon(ft.icons.CHECK_CIRCLE, color='#C6920E', size=40),
                    # Insere a mensagem
                    ft.Text(value='SUA COMPRA FOI RESERVADA.\nEFETUE O PAGEMENTO PARA GARANTÍ-LA!',
                            size=18,
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.START),
                ],
                    alignment=ft.MainAxisAlignment.CENTER),

                ft.Container(  # Container menor para ajudar a alinar tudo
                    padding=10,
                    width=450,
                    height=190,
                    bgcolor="#f5f5f5",

                    content=ft.Column([
                        ft.Image(src='qr_code.png',  # Insere o QR Code do pix
                                 width=150,
                                 height=150),
                        ft.Text(value=random_pix_key,  # Insere a chave pix
                                size=18,
                                color=ft.colors.BLACK,
                                weight=ft.FontWeight.BOLD)
                    ], alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )


def cleanCart():
    dashboard.table.rows.clear()
    cart.components['list'].current.controls = cart.create_cards_from_table(
        dashboard.table)
    dashboard.page.update()
