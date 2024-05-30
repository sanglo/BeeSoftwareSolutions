from proj.templates import template
import reflex as rx

@template(route="/raporty/pracownicy", title="Raport Pracownicy")
def raport_pracownicy() -> rx.Component:
    """The other page.

    Returns:
        The UI for the other page.
    """
    return rx.vstack(
        rx.heading("Raport dotyczący pracowników", size="8"),
        rx.text("This is the other page."),
    )