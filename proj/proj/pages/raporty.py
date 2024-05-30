"""The dashboard page."""

from proj.templates import template

import reflex as rx


class RaportState(rx.State):
    selected_report: str = "None"
    def select_report(self,report_type: str):
        self.selected_report = report_type
        print(self.selected_report)

    def confirm_selection(self):
        if self.selected_report:
            return rx.redirect(f"raporty/{self.selected_report}")


@template(route="/raporty", title="Raporty",on_load=RaportState.select_report("None"))
def raporty() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    button_style = {
        "fontSize": "20px",  # Zwiększenie rozmiaru tekstu przycisku
        "width": "250px",  # Stała szerokość przycisku
        "height": "150px",  # Stała wysokość przycisku
        "textAlign": "center",  # Wyśrodkowanie tekstu
        "lineHeight": "60px",  # Wyśrodkowanie tekstu pionowo
        "margin": "10px",  # Dodanie odstępu między przyciskami
    }

    active_button_style = button_style.copy()
    active_button_style["backgroundColor"] = "#008CBA"

    return rx.vstack(
        rx.heading("Raporty", size="8"),
        rx.text("Wybierz rodzaj raportu do wygenerowania"),
        rx.hstack(
        rx.button(
            "Pracownicy",
            on_click=RaportState.select_report("pracownicy"),
            size="4",
            style={**button_style, "backgroundColor": rx.cond(
                RaportState.selected_report == "pracownicy","#c71d61","#e93d82")},
            _hover={
                "background_color": "#cf3673",
            },
        ),
        rx.button(
            "Uczniowie",
            on_click=RaportState.select_report("uczniowie"),
            size = "4",
            style={**button_style, "backgroundColor": rx.cond(
                RaportState.selected_report == "uczniowie","#c71d61","#e93d82")},
            _hover={
                "background_color": "#cf3673",
            },
        ),
        rx.button(
            "Dostępność Sal",
            on_click=RaportState.select_report("dostepnosc_sal"),
            size="4",
            style={**button_style, "backgroundColor": rx.cond(
                RaportState.selected_report == "dostepnosc_sal","#c71d61","#e93d82")},
            _hover={
                "background_color": "#cf3673",
            },
        ),
        rx.button(
            "Stan Magazynu",
            on_click=RaportState.select_report("stan_magazynu"),
            size="4",
            style={**button_style, "backgroundColor": rx.cond(
                RaportState.selected_report == "stan_magazynu","#c71d61","#e93d82")},
            _hover={
                "background_color": "#cf3673",
            },
        )
        ),
    rx.button(
        "Dalej",
        on_click=RaportState.confirm_selection,
        style={**button_style, "backgroundColor": rx.cond(
                RaportState.selected_report == "None","#CCCCCC","#008CBA"), "lineHeight": "normal", "height": "60px"},
        disabled=RaportState.selected_report == "None"
    ),
        rx.cond(
            RaportState.selected_report != "None",
            rx.text(""),
            rx.text("Nie wybrano rodzaju raportu", color="red", style={"margin-left":"10px"})
        ),
    )
