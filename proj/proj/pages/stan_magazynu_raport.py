from proj.templates import template
import reflex as rx

@template(route="/raporty/stan_magazynu", title="Raport Stan Magazynu")
def raport_stan_magazynu() -> rx.Component:
    """The other page.

    Returns:
        The UI for the other page.
    """
    return rx.vstack(
        rx.heading("Raport dotyczący stanu magazynu", size="8"),
        rx.text("This is the other page."),
    )