import flet as ft
import random
import string
import qrcode

#Gerador de chave PIX aleatória

def generate_random_key(length):
    """Gera uma chave aleatória PIX."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

#Gerador de QR Code aleatório

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
random_pix_key = generate_random_key(20)  # Ajuste o comprimento conforme necessário
qr_code_file_path = "qr_code.png"

generate_qr_code(random_pix_key, qr_code_file_path)
print(f"Chave PIX Aleatória: {random_pix_key}")
print(f"QR Code salvo em: {qr_code_file_path}")

# Página final
def checkoutCreditCard():
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
                ft.Container(
                    padding=10,
                    width=450,

                    height=190,
                    bgcolor="#f5f5f5",

                    content=ft.Column([

                        ft.Text(
                                size=18,
                                color=ft.colors.BLACK,
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"R$ ",
                                size=17,
                                color=ft.colors.BLACK, weight="bold"),
                        ft.Text(f"Estoque: ",
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

def checkoutPix():
    return ft.ListView(
        spacing=10,
        padding=20,
        expand=1,
        controls=[
            ft.Card(

            ),
            ft.Text(
            value="SUA COMPRA FOI FINALIZADA.\nOBRIGADO POR ESCOLHER NOSSA LOJA!",
            weight='Bold',
            size=25,
            color='#FFFFFF',
            text_align=ft.TextAlign.CENTER)]
    )