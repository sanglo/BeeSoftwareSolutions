from proj.templates import template
import reflex as rx

@template(route="/raporty/dostepnosc_sal", title="Raport Dostępność Sal")
def raport_dostepnosc_sal() -> rx.Component:
    """The other page.

    Returns:
        The UI for the other page.
    """
    return rx.vstack(
        rx.heading("Raport dotyczący dostępności sal", size="8"),
        rx.text("This is the other page."),
    )