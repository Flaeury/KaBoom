import flet as ft
import assets.components.paymentOptions as pay


def checkout():
    mensage, options = pay.paymentOptions()
    return mensage, options
