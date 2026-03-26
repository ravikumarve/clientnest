import reflex as rx
from ..state.agency import AgencyState
from ..state.auth import AuthState


def white_label() -> rx.Component:
    """White-label settings page."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("White-label Settings", size="8"),
            rx.cond(
                AgencyState.has_white_label,
                rx.vstack(
                    rx.card(
                        rx.vstack(
                            rx.heading("Brand Color", size="5"),
                            rx.color_picker(
                                value=AgencyState.brand_color,
                                on_change=AgencyState.update_brand_color,
                            ),
                            rx.text("Current color: "),
                            rx.box(
                                width="50px",
                                height="50px",
                                background_color=AgencyState.brand_color,
                                border="1px solid gray",
                                border_radius="md",
                            ),
                            spacing="3",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Logo", size="5"),
                            rx.cond(
                                AgencyState.logo_url,
                                rx.image(
                                    src=AgencyState.logo_url,
                                    height="100px",
                                    border_radius="md",
                                ),
                                rx.text("No logo uploaded"),
                            ),
                            rx.upload(
                                rx.button(
                                    "Upload Logo",
                                    variant="outline",
                                ),
                                border="1px dashed",
                                padding="4",
                                border_radius="md",
                            ),
                            spacing="3",
                        ),
                    ),
                    spacing="4",
                    width="100%",
                ),
                rx.card(
                    rx.vstack(
                        rx.heading("Upgrade Required", size="5"),
                        rx.text("White-label features require Solo plan or higher"),
                        rx.button(
                            "View Plans",
                            on_click=rx.redirect("/settings/billing"),
                        ),
                        spacing="3",
                    ),
                ),
            ),
            spacing="5",
            width="100%",
            max_width="600px",
        ),
    )
