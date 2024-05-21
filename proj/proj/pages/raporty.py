"""The dashboard page."""

from proj.templates import template

import reflex as rx


@template(route="/raporty", title="Raporty")
def raporty() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Raporty", size="8"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/raporty.py"),
        ),
    )
