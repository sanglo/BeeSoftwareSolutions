import reflex as rx
from proj.templates import template

class UserState(rx.State):
    username: str = ''
    password: str = ''
    is_logged_in: bool = False
    login_message: str = ''  

    def handle_username_change(self, value: str):
        self.username = value

    def handle_password_change(self, value: str):
        self.password = value

    def login(self):
        if self.username == "admin" and self.password == "admin":
            self.is_logged_in = True
            print("Login successful")
            self.login_message = "Logowanie udane"  # Ustawienie komunikatu
            rx.redirect("/magazyny")  # Replace "/" with the desired URL
        else:
            self.is_logged_in = False
            self.login_message = "Logowanie nieudane. Błędna nazwa użytkownika albo hasło"  # Ustawienie komunikatu
            print("Login failed")

    def logout(self):
        self.is_logged_in = False

@template(route="/logowanie", title="Logowanie")
def logowanie() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Logowanie do systemu",
                        size="4",
                        margin_top="0.5em",
                        color='black',
                        text_align="center",
                    ),
                    rx.text(
                        "Zaloguj się, aby mieć dostęp do funkcji zarządzania",
                        text_align="center",
                        margin_bottom="2em",
                        color='black',
                    ),
                    rx.text(UserState.login_message, color='red'),
                    rx.input(
                        placeholder="Nazwa użytkownika",
                        margin_bottom="1em",
                        color='#696969',
                        width="100%",
                        text_align="center",
                        class_name="placeholder-gray",
                        on_change=UserState.handle_username_change,
                    ),
                    rx.input(
                        type="password",
                        placeholder="Hasło",
                        margin_bottom="1em",
                        color='#696969',
                        width="100%",
                        text_align="center",
                        class_name="placeholder-gray",
                        on_change=UserState.handle_password_change,
                    ),
                    rx.hstack(
                        rx.button("Zaloguj", margin_right="1em", on_click=UserState.login),
                        rx.button("Zresetuj hasło", variant="outline"),
                    ),
                    rx.box(
                        rx.link(
                            "Masz problem z zalogowaniem? Skontaktuj się z Pomocą IT",
                            href="/support",
                            text_align="center",
                            background="white",
                            padding="0.5em",
                            border_radius="md",
                            box_shadow="md",
                            margin_top="1em",
                            display="block",
                        ),
                        width="100%",
                        text_align="center"
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
