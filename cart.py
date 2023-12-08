import flet as ft
from flet import *
import os
from dash import create_selected_product_item, addToCartBtn


def selected_products():
    return ft.ListView(
        controls=[create_selected_product_item(
            x) for x in addToCartBtn.userOrder]
    )
