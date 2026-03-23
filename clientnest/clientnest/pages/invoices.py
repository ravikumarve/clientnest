import reflex as rx


def invoices() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Invoices", size="8"),
            rx.text("Invoices will appear here", size="4"),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def new_invoice() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("New Invoice", size="8"),
            rx.text("Create a new invoice", size="4"),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )
