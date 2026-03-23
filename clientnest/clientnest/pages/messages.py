import reflex as rx


def project_messages() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Project Messages", size="8"),
            rx.text("Messages will appear here", size="4"),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )
