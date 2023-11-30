import flet as ft
from pages.index import index

def main(page: ft.Page):        
    page.title = "TechTemple"             
    page.theme_mode = "dark"
    
    # Chame a função ou crie uma instância da classe do arquivo index.py
    index(page)

ft.app(target=main)
