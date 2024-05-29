from proj.templates import template
import reflex as rx
from proj.state import UczniowieState

@template(route="/uczniowie", title="Uczniowie")
def uczniowie() -> rx.Component:

    return rx.vstack(
        rx.heading("Uczniowie", size="8"),
        rx.button("Dodaj ucznia", on_click=UczniowieState.toggle_form),
        rx.cond(
            UczniowieState.show_form,
            rx.vstack(
                rx.input(placeholder="Imię", on_change=UczniowieState.handle_first_name_change),
                rx.input(placeholder="Nazwisko", on_change=UczniowieState.handle_last_name_change),
                rx.input(placeholder="Klasa", on_change=UczniowieState.handle_class_name_change),
                rx.button("Submit", on_click=UczniowieState.submit_form),
            )
        )
    )