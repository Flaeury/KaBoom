import flet as ft



def popUp(page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor='#FF7E20',
        leading=ft.Icon(ft.icons.CHECK, color='#29B207', size=40),
        content=ft.Text(
            value="SUA COMPRA FOI FINALIZADA. OBRIGADO POR ESCOLHER NOSSA LOJA! VOLTE SEMPRE!",
            weight='Bold',
            color='#FFFFFF'
        ),
        actions=[ft.TextButton(text="FECHAR", on_click=close_banner)],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    b = ft.ElevatedButton("FINALIZAR COMPRA", on_click=show_banner_click)
    return b
