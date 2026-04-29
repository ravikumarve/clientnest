import reflex as rx
from ..state.project import ProjectState
from ..state.auth import AuthState


def client_portal() -> rx.Component:
    """Client portal view - only shows client's own projects."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Client Portal", size="8"),
            rx.text("Welcome to your client dashboard", size="4"),
            # Client's projects
            rx.heading("Your Projects", size="6"),
            rx.cond(
                ProjectState.projects,
                rx.grid(
                    rx.foreach(
                        ProjectState.projects,
                        lambda project: rx.card(
                            rx.vstack(
                                rx.heading(project["title"], size="4"),
                                rx.text(f"Status: {project['status']}"),
                                rx.cond(
                                    project["due_date"],
                                    rx.text(f"Due: {project['due_date']}"),
                                    rx.text("No due date"),
                                ),
                                rx.button(
                                    "View Project",
                                    on_click=rx.redirect(f"/projects/{project['id']}"),
                                ),
                                spacing="3",
                            ),
                        ),
                    ),
                    columns="2",
                    spacing="4",
                    width="100%",
                ),
                rx.text("No projects assigned yet", size="4"),
            ),
            # Quick actions
            rx.heading("Quick Actions", size="6"),
            rx.hstack(
                rx.button(
                    "View Messages",
                    on_click=rx.redirect("/projects/messages"),
                ),
                rx.button(
                    "View Files",
                    on_click=rx.redirect("/projects/files"),
                ),
                rx.button(
                    "View Invoices",
                    on_click=rx.redirect("/invoices"),
                ),
                spacing="4",
            ),
            spacing="6",
            width="100%",
            max_width="1000px",
        ),
    )
