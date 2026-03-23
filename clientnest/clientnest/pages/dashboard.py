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
                    rx.stat_card(
                        "Projects", ProjectState.projects.length(), "folder", "blue"
                    ),
                    rx.stat_card("Clients", "0", "users", "green"),
                    rx.stat_card("Invoices", "0", "dollar-sign", "purple"),
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
                        on_change=lambda e: setattr(
                            ProjectState, "project_title", e.target.value
                        ),
                    ),
                    rx.textarea(
                        placeholder="Description",
                        name="description",
                        value=ProjectState.project_description,
                        on_change=lambda e: setattr(
                            ProjectState, "project_description", e.target.value
                        ),
                    ),
                    rx.input(
                        placeholder="Due Date (optional)",
                        type="date",
                        name="due_date",
                        value=ProjectState.project_due_date,
                        on_change=lambda e: setattr(
                            ProjectState, "project_due_date", e.target.value
                        ),
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
