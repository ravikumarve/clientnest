import reflex as rx
from ..state.auth import AuthState


def login() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Login to Clientnest", size="8"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Email",
                        type="email",
                        name="email",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Password",
                        type="password",
                        name="password",
                        required=True,
                        width="100%",
                    ),
                    rx.button(
                        "Login",
                        type="submit",
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                ),
                on_submit=AuthState.login,
                reset_on_submit=False,
            ),
            rx.text(
                "Don't have an account? ",
                rx.link("Sign up", href="/signup"),
                align="center",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def signup() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Create Your Account", size="8"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Agency Name",
                        name="agency_name",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Your Name",
                        name="your_name",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Email",
                        type="email",
                        name="email",
                        required=True,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Password",
                        type="password",
                        name="password",
                        required=True,
                        width="100%",
                    ),
                    rx.button(
                        "Sign Up",
                        type="submit",
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                ),
                on_submit=AuthState.register,
                reset_on_submit=False,
            ),
            rx.text(
                "Already have an account? ",
                rx.link("Login", href="/login"),
                align="center",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def accept_invite() -> rx.Component:
    """Accept invitation page for client signup."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Accept Invitation", size="8"),
            rx.text("Set up your client account", size="4"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Your Name",
                        name="name",
                        required=True,
                    ),
                    rx.input(
                        type="password",
                        placeholder="Password",
                        name="password",
                        required=True,
                    ),
                    rx.input(
                        type="password",
                        placeholder="Confirm Password",
                        name="confirm_password",
                        required=True,
                    ),
                    rx.button(
                        "Create Account",
                        type="submit",
                        width="100%",
                    ),
                    spacing="4",
                ),
                on_submit=AuthState.accept_invite,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
            max_width="400px",
        ),
    )
