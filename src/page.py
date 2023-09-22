from textual.app import App, ComposeResult
from textual.containers import (
        Container,
        VerticalScroll
)
from textual.widgets import (
        Header,
        Footer,
        Label
)

logo = r"""
   ▄████████     ███        ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████    ▄████████         ▄████████    ▄████████ ▀████    ▐████▀
  ███    ███ ▀█████████▄   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███   ███    ███        ███    ███   ███    ███   ███▌   ████▀ 
  ███    █▀     ▀███▀▀██   ███    ███ ███   ███ ███   ███   ███    █▀    ███    ███        ███    █▀    ███    ███    ███  ▐███    
  ███            ███   ▀   ███    ███ ███   ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀       ▄███▄▄▄       ███    ███    ▀███▄███▀    
▀███████████     ███     ▀███████████ ███   ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ▀▀███▀▀▀     ▀███████████    ████▀██▄     
         ███     ███       ███    ███ ███   ███ ███   ███   ███    █▄  ▀███████████        ███          ███    ███   ▐███  ▀███    
   ▄█    ███     ███       ███    ███ ███   ███ ███   ███   ███    ███   ███    ███        ███          ███    ███  ▄███     ███▄  
 ▄████████▀     ▄████▀     ███    █▀   ▀█   █▀   ▀█   █▀    ██████████   ███    ███        ███          ███    █▀  ████       ███▄ 
                                                                         ███    ███                                               
"""


class CeeFaxApp(App):
    TITLE = "STANNER FAX"
    SUB_TITLE = "based on CEEFAX"
    CSS_PATH = "./css/welcome.tcss"
    BINDINGS = [
            ("q", "quit_ceefax", "Quit"),
            ("d", "toggle_dark", "Toggle dark mode"),
            ("n", "next_page", "Navigate to next page"),
            ("p", "previous_page", "Navigate to previous page")]

    def __init__(self):
        self.current = 100
        super().__init__(None, None, False)

    def compose(self) -> ComposeResult:
        """Create child widgits for the app"""
        yield Header(show_clock=True, name="CEEFAX")
        yield Footer()
        yield VerticalScroll(
                Container(
                    Label(logo, id="title"),
                    Label("Welcome", id="welcome"),
                    Label(f"page: {self.current}", id="pagenum")
                )
            )

    def action_quit_ceefax(self) -> None:
        """Quits Ceefax"""
        self.exit()

    def action_next_page(self) -> None:
        self.current += 1
        # self.update_page()

    def action_previous_page(self) -> None:
        self.current -= 1
        # self.update_page()


if __name__ == "__main__":
    app = CeeFaxApp()
    app.run()
