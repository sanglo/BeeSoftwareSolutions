"""The home page of the app."""

from proj import styles
from proj.templates import template

import reflex as rx


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page :) .

    Returns:
        The UI for the home page.
    """
    
    return "Wybierz zakladke"
