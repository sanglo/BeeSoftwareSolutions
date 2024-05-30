from proj.templates import template
import reflex as rx

@template(route="/raporty/uczniowie", title="Raport Uczniowie")
def raport_uczniowie() -> rx.Component:
    """The other page.

    Returns:
        The UI for the other page.
    """
    return rx.vstack(
        rx.heading("Raport dotyczący uczniów", size="8"),
        rx.text("This is the other page."),
    )