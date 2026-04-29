import reflex as rx
from ..state.dashboard import DashboardState
from ..state.project import ProjectState


def dashboard() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Dashboard", size="8"),
            rx.hstack(
                rx.button(
                    "Create Project",
                    on_click=ProjectState.toggle_create_form,
                    color_scheme="blue",
                ),
                rx.button(
                    "View All Projects",
                    href="/projects",
                    color_scheme="gray",
                ),
                spacing="4",
            ),
            rx.cond(
                ProjectState.show_create_form,
                create_project_form_dashboard(),
                rx.box(),
            ),
            rx.hstack(
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.text("Projects", size="3"),
                            rx.text(ProjectState.projects.length(), size="5"),
                            rx.icon("folder", size=20, color_scheme="blue"),
                            spacing="2",
                            align="center",
                        ),
                        size="3",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.text("Clients", size="3"),
                            rx.text("0", size="5"),
                            rx.icon("users", size=20, color_scheme="green"),
                            spacing="2",
                            align="center",
                        ),
                        size="3",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.text("Invoices", size="3"),
                            rx.text("0", size="5"),
                            rx.icon("dollar-sign", size=20, color_scheme="purple"),
                            spacing="2",
                            align="center",
                        ),
                        size="3",
                    ),
                    template_columns="repeat(3, 1fr)",
                    gap="4",
                    width="100%",
                ),
                spacing="6",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def create_project_form_dashboard() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Create New Project", size="6"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Project Title",
                        name="title",
                        required=True,
                        value=ProjectState.project_title,
                        on_change=ProjectState.set_project_title,
                    ),
                    rx.text_area(
                        placeholder="Description",
                        name="description",
                        value=ProjectState.project_description,
                        on_change=ProjectState.set_project_description,
                    ),
                    rx.input(
                        placeholder="Due Date (optional)",
                        type="date",
                        name="due_date",
                        value=ProjectState.project_due_date,
                        on_change=ProjectState.set_project_due_date,
                    ),
                    rx.hstack(
                        rx.button(
                            "Cancel",
                            on_click=ProjectState.toggle_create_form,
                            variant="soft",
                        ),
                        rx.button(
                            "Create Project",
                            type="submit",
                            color_scheme="blue",
                        ),
                        spacing="3",
                    ),
                ),
                on_submit=ProjectState.create_project,
                reset_on_submit=True,
            ),
            border="1px solid",
            border_color="gray.300",
            border_radius="lg",
            padding="4",
            width="100%",
            max_width="500px",
        ),
        position="fixed",
        top="20%",
        right="5%",
        z_index="1000",
        background_color="white",
    )
