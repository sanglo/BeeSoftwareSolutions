from proj import styles
from proj.templates import template

import reflex as rx

@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    
    return rx.hstack(
        rx.vstack(
            rx.heading("Witaj w systemie zarządzania twoją placówką", size="6"),
            rx.text("News & Updates"),
            rx.text("Nowe aplikacje"),
            rx.text("Ustawienia"),
            align="center",
            padding_x="5em",
            padding_y="0em"
        ),
        rx.vstack(
            rx.heading("OSTATNIO UŻYWANE", size="5"),
            rx.hstack(rx.box(border="1px solid black", width="150px", height="100px"), rx.box(border="1px solid black", width="150px", height="100px")),
            rx.hstack(rx.box(border="1px solid black", width="150px", height="100px"), rx.box(border="1px solid black", width="150px", height="100px")),
            align="center",
            background_color="lightblue",
            padding="1em"
        )
    )

