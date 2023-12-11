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
