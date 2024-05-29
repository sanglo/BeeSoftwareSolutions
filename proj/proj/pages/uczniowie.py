from proj.templates import template
import reflex as rx
from proj.state import UczniowieState

@template(route="/uczniowie", title="Uczniowie")
def uczniowie() -> rx.Component:
    print('5')
    return rx.vstack(
        rx.heading("Uczniowie", size="8",on_click=UczniowieState.get_students),
        rx.foreach(
            UczniowieState.students,
            lambda student: rx.text(f"{student['first_name']} {student['last_name']} - Klasa: {student['class_name']}")
        ),
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