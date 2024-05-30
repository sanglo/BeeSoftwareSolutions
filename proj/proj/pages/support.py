from proj.templates import template
import reflex as rx


@template(route="/support", title="Support")
def support() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Support", size="8"),
        rx.text("Support page!"),
        rx.text(
            # You can add more text here if needed
        ),
    )
