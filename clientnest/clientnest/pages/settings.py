import reflex as rx
from ..state.agency import AgencyState
from ..state.auth import AuthState


def settings() -> rx.Component:
    """Main settings page."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Settings", size="8"),
            rx.text("Manage your agency settings", size="4"),
            rx.grid(
                rx.card(
                    rx.heading("Profile", size="6"),
                    rx.text("Update agency information and branding"),
                    rx.button(
                        "Edit Profile", on_click=rx.redirect("/settings/profile")
                    ),
                ),
                rx.card(
                    rx.heading("Billing", size="6"),
                    rx.text("Manage subscription and payment methods"),
                    rx.button(
                        "View Billing", on_click=rx.redirect("/settings/billing")
                    ),
                ),
                rx.card(
                    rx.heading("Team", size="6"),
                    rx.text("Manage team members and permissions"),
                    rx.button("Manage Team", on_click=rx.redirect("/settings/team")),
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="5",
            width="100%",
            max_width="1000px",
        ),
    )


def billing() -> rx.Component:
    """Billing and subscription management page."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Billing & Subscription", size="8"),
            rx.card(
                rx.vstack(
                    rx.heading("Current Plan", size="6"),
                    rx.text(AgencyState.plan, size="4", weight="bold"),
                    rx.text("Subscription status will show here", color="gray"),
                    spacing="3",
                ),
                width="100%",
            ),
            rx.grid(
                rx.card(
                    rx.vstack(
                        rx.heading("Solo Plan", size="5"),
                        rx.text("$19/month", size="4", weight="bold"),
                        rx.vstack(
                            rx.text("✓ Unlimited clients"),
                            rx.text("✓ Unlimited projects"),
                            rx.text("✓ 5GB storage"),
                            rx.text("✓ White-label branding"),
                            rx.text("✓ Basic invoicing"),
                            spacing="2",
                        ),
                        rx.button(
                            "Upgrade to Solo",
                            on_click=rx.redirect("/checkout/solo"),
                            variant="solid",
                        ),
                        spacing="4",
                    ),
                ),
                rx.card(
                    rx.vstack(
                        rx.heading("Agency Plan", size="5"),
                        rx.text("$39/month", size="4", weight="bold"),
                        rx.vstack(
                            rx.text("✓ Unlimited clients"),
                            rx.text("✓ Unlimited projects"),
                            rx.text("✓ 20GB storage"),
                            rx.text("✓ White-label + custom domain"),
                            rx.text("✓ Advanced invoicing"),
                            rx.text("✓ 5 team members"),
                            spacing="2",
                        ),
                        rx.button(
                            "Upgrade to Agency",
                            on_click=rx.redirect("/checkout/agency"),
                            variant="solid",
                        ),
                        spacing="4",
                    ),
                ),
                columns="2",
                spacing="4",
                width="100%",
            ),
            spacing="5",
            width="100%",
            max_width="1000px",
        ),
    )
