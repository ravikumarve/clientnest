import reflex as rx


def project_files() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Project Files", size="8"),
            rx.text("Files will appear here", size="4"),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )
