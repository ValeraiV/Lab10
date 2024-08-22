import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP 2024 - Lab 10"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Country Borders", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with controls
        self._txtAnno = ft.TextField(label="Anno")
        self._btnCalcola = ft.ElevatedButton(text="Calcola Confini", on_click=self._controller.handleCalcola)
        row1 = ft.Row([self._txtAnno, self._btnCalcola], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #2row
        self._ddStato = ft.Dropdown(label="Stato", disabled=True)
        self._btnRaggiungibili = ft.ElevatedButton(text="Stati Raggiungibili",
                                                   on_click=self._controller.handleRaggiungibili,
                                                   disabled=True, width=200)

        row2 = ft.Row([self._ddStato, self._btnRaggiungibili], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self._txt_result)
        self._page.update()



    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
