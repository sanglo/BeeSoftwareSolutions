"""Sidebar component for the app."""

from proj import styles

import reflex as rx


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.color_mode_cond(
            rx.image(src="/reflex_black.svg", height="2em"),
            rx.image(src="/reflex_white.svg", height="2em"),
        ),
        rx.spacer(),
        rx.link(
            rx.button(
                rx.icon("github"),
                color_scheme="gray",
                variant="soft",
            ),
            href="https://github.com/reflex-dev/reflex",
        ),
        align="center",
        padding_x="1em",
        padding_y="1em",
    )




def sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.box(
            rx.text(
                text,
            ),
            bg=rx.cond(
                active,
                rx.color("accent", 2),
                "transparent",
            ),
            border=rx.cond(
                active,
                f"1px solid {rx.color('accent', 6)}",
                f"1px solid {rx.color('gray', 6)}",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            border_radius=styles.border_radius,
            padding_x="1em",
            padding_y="0.5em",
        ),
        href=url,
        align_self="center",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            rx.hstack(
                sidebar_header(),
                rx.hstack(
                    *[
                        sidebar_item(
                            text=page.get("title", page["route"].strip("/").capitalize()),
                            url=page["route"],
                        )
                        for page in get_decorated_pages()
                    ],
                    align_items="center",
                    overflow_x="auto",
                    padding_x="1em",
                ),
                rx.spacer(),
                width="100%",
                height="auto",
            ),
            display=["block"],
            height="auto",
            width="100%",
            position="sticky",
            top="0px",
            border_bottom=styles.border,
        ),
        width="100%",
        height="auto",
    )


def main_content() -> rx.Component:
    """Main content.

    Returns:
        The main content component.
    """
    # Placeholder for the actual main content
    return rx.box(
        rx.text("Main Content Goes Here"),
        width="100%",
        padding="2em",
    )


def layout() -> rx.Component:
    """Complete layout with sidebar and main content.

    Returns:
        The complete layout component.
    """
    return rx.hstack(
        sidebar(),
        main_content(),
        width="100%",
        align_items="stretch",
    )
