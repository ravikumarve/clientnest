import reflex as rx


def client_portal() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Client Portal", size="8"),
            rx.text("Welcome to your client portal", size="4"),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )
