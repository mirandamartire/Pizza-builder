import flet as ft

def main(page: ft.Page):
    page.title = "Pizza Builder"

    base = ft.Image(src="assets/images/plainpizza.png")
    prosciutto = ft.Image(src="assets/images/prosciuttoslice.png", visible=False)
    rucula = ft.Image(src="assets/images/ruculatopping.png", visible=False)
    mozzarella = ft.Image(src="assets/images/mozzarella.png", width=300, height=300, visible=False)
    
    def toggle_prosciutto(e):
        prosciutto.visible = e.control.value
        page.update()

    def toggle_rucula(e):
        rucula.visible = e.control.value
        page.update()

    def toggle_mozzarella(e):
        mozzarella.visible = e.control.value
        page.update()

    pizza = ft.Stack(
        [
            base,
            mozzarella,
            prosciutto,
            rucula,
        ],
        width=300,
        height=300
    )

    switches = ft.Column([
        ft.Switch(label="Prosciutto", on_change=toggle_prosciutto),
        ft.Switch(label="Rúcula", on_change=toggle_rucula),
        ft.Switch(label="Mozzarella", on_change=toggle_mozzarella),
    ])

    page.add(
        ft.Row([
            pizza,
            switches
        ])
    )

ft.app(target=main)