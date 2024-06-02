import reflex as rx
from proj.templates import template

class UserState(rx.State):
    is_logged_in: bool = False
    logout_message: str = 'Zostałeś wylogowany'

    def logout(self):
        self.is_logged_in = False
        print("Logout successful")
        rx.redirect("/logowanie")

@template(route="/wylogowanie", title="Wylogowywanie")
def wylogowywanie() -> rx.Component:
    UserState().logout()  # Wylogowanie użytkownika i ustawienie odpowiedniego stanu

    return rx.center(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Wylogowywanie",
                        size="4",
                        margin_top="0.5em",
                        color='black',
                        text_align="center",
                    ),
                    rx.text(
                        UserState.logout_message,
                        text_align="center",
                        margin_bottom="2em",
                        color='black',
                    ),
                    rx.button(
                        "Powrót do logowania",
                        on_click=lambda: rx.redirect("/logowanie"),
                        margin_bottom="1em",
                    ),
                ),
                margin_top="1em",
                padding="2em",
                border_radius="md",
                width="100%",
                max_width="400px",
                background="white",
                box_shadow="lg",
            ),
        ),
    )
