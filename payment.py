import flet as ft
import assets.components.paymentOptions as pay

#Definindo checkout e pagamento

def checkout():
    mensage, options = pay.paymentOptions()
    return mensage, options
