import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Clientnest", size="9"),
            rx.text(
                "White-label client portal for freelancers and agencies",
                size="5",
            ),
            rx.link(
                rx.button("Get Started", color_scheme="blue"),
                href="/signup",
                width="100%",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
