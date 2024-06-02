from proj.templates import template
import reflex as rx
from proj.state import RekrutacjeState

@template(route="/rekrutacja", title="Rekrutacja")
def rekrutacja() -> rx.Component:
    print('6')
    return rx.vstack(
        rx.heading("Rekrutacja", size="8", on_click=RekrutacjeState.get_jobs),
        rx.foreach(
            RekrutacjeState.jobs,
            lambda job: rx.vstack(
                rx.heading("Ogłoszenie", size="6"),
                rx.text(f"Tytuł stanowiska: {job['title']}"),
                rx.text(f"Opis obowiązków: {job['description']}"),
                rx.text(f"Wymagania kwalifikacyjne: {job['qualifications']}"),
                rx.text(f"Lokalizacja: {job['location']}"),
                rx.text(f"Wynagrodzenie: {job['salary']}"),
                style={"margin-bottom": "10px"}
            )
        ),
        rx.button("Dodaj nowe ogłoszenie", on_click=RekrutacjeState.toggle_form),
        rx.cond(
            RekrutacjeState.show_form,
            rx.vstack(
                rx.input(
                    placeholder="Tytuł stanowiska", 
                    on_change=lambda e: RekrutacjeState.handle_change('title', e), 
                    style={"width": "40vw"}
                ),
                rx.cond(RekrutacjeState.errors.contains('title'), rx.text(RekrutacjeState.errors['title'])),
                rx.input(
                    placeholder="Opis obowiązków", 
                    on_change=lambda e: RekrutacjeState.handle_change('description', e), 
                    textarea=True, 
                    style={"width": "40vw", "min-height": "50px", "resize": "vertical"}
                ),
                rx.cond(RekrutacjeState.errors.contains('description'), rx.text(RekrutacjeState.errors['description'])),
                rx.input(
                    placeholder="Wymagania kwalifikacyjne", 
                    on_change=lambda e: RekrutacjeState.handle_change('qualifications', e), 
                    textarea=True, 
                    style={"width": "40vw", "min-height": "50px", "resize": "vertical"}
                ),
                rx.cond(RekrutacjeState.errors.contains('qualifications'), rx.text(RekrutacjeState.errors['qualifications'])),
                rx.input(
                    placeholder="Lokalizacja", 
                    on_change=lambda e: RekrutacjeState.handle_change('location', e), 
                    style={"width": "40vw"}
                ),
                rx.cond(RekrutacjeState.errors.contains('location'), rx.text(RekrutacjeState.errors['location'])),
                rx.input(
                    placeholder="Wynagrodzenie", 
                    on_change=lambda e: RekrutacjeState.handle_change('salary', e), 
                    style={"width": "40vw"}
                ),
                rx.cond(RekrutacjeState.errors.contains('salary'), rx.text(RekrutacjeState.errors['salary'])),
                rx.button("Opublikuj", on_click=RekrutacjeState.submit_form),
            )
        )
    )