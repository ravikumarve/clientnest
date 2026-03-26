import reflex as rx
from ..state.project import ProjectState


def status_color(status: str) -> str:
    return rx.cond(
        ProjectState.current_project["status"] == "completed",
        "green",
        rx.cond(
            ProjectState.current_project["status"] == "in_progress",
            "blue",
            rx.cond(
                ProjectState.current_project["status"] == "review",
                "amber",
                rx.cond(
                    ProjectState.current_project["status"] == "on_hold",
                    "red",
                    "gray",
                ),
            ),
        ),
    )


def task_list() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            ProjectState.tasks,
            lambda task: rx.hstack(
                rx.checkbox(
                    checked=task["is_done"],
                    on_change=lambda checked: ProjectState.toggle_task(task["id"]),
                ),
                rx.text(
                    task["title"],
                    text_decoration=rx.cond(task["is_done"], "line-through", "none"),
                    color=rx.cond(task["is_done"], "gray", "black"),
                    flex="1",
                ),
                rx.button(
                    rx.icon("trash-2", size=16),
                    on_click=ProjectState.delete_task(task["id"]),
                    size="1",
                    variant="ghost",
                    color_scheme="red",
                ),
                align_items="center",
                spacing="3",
                width="100%",
                padding="2",
                border="1px solid",
                border_color="gray.100",
                border_radius="md",
            ),
        ),
        spacing="3",
        width="100%",
    )


def create_project_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Create New Project", size="6"),
            rx.vstack(
                rx.input(
                    placeholder="Project Title",
                    value=ProjectState.project_title,
                    on_change=ProjectState.set_project_title,
                ),
                rx.text_area(
                    placeholder="Description",
                    value=ProjectState.project_description,
                    on_change=ProjectState.set_project_description,
                ),
                rx.input(
                    placeholder="Due Date (optional)",
                    type="date",
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
                        on_click=ProjectState.create_project,
                        color_scheme="blue",
                    ),
                    spacing="3",
                ),
                spacing="3",
                width="100%",
            ),
            border="1px solid",
            border_color="gray.300",
            border_radius="lg",
            padding="4",
            width="100%",
            max_width="400px",
        ),
        position="fixed",
        top="20%",
        right="5%",
        z_index="1000",
        background_color="white",
    )


def projects_table() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            ProjectState.projects,
            lambda project: rx.card(
                rx.vstack(
                    rx.text(project["title"], size="5", weight="bold"),
                    rx.text(f"Status: {project['status']}", size="3"),
                    rx.text(project["client_name"], size="3", color="gray"),
                    rx.hstack(
                        rx.button(
                            "View Details",
                            on_click=ProjectState.load_project(project["id"]),
                            size="2",
                            color_scheme="blue",
                        ),
                        rx.button(
                            "Delete",
                            on_click=ProjectState.delete_project(project["id"]),
                            size="2",
                            color_scheme="red",
                        ),
                        spacing="3",
                    ),
                    spacing="3",
                ),
                size="4",
            ),
        ),
        spacing="4",
        width="100%",
    )


def projects() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Projects", size="8"),
            rx.hstack(
                rx.button(
                    "Create Project",
                    on_click=ProjectState.toggle_create_form,
                    color_scheme="blue",
                ),
                rx.spacer(),
                rx.select(
                    ["All", "Active", "Review", "Completed"],
                    value=ProjectState.project_filter,
                    on_change=ProjectState.set_project_filter,
                    placeholder="Filter by status",
                ),
                align_items="center",
                width="100%",
            ),
            rx.cond(
                ProjectState.projects.length() > 0,
                projects_table(),
                rx.text(
                    "No projects found. Create your first project!",
                    size="4",
                    color_scheme="gray",
                ),
            ),
            rx.cond(
                ProjectState.show_create_form,
                create_project_form(),
                rx.box(),
            ),
            spacing="5",
            width="100%",
            min_height="85vh",
        ),
    )


def project_detail() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.hstack(
                rx.button(
                    rx.icon("arrow-left"),
                    on_click=rx.redirect("/projects"),
                    size="2",
                    variant="ghost",
                ),
                rx.heading(ProjectState.current_project["title"], size="7"),
                rx.spacer(),
                rx.badge(
                    ProjectState.current_project["status"],
                    color_scheme=status_color(ProjectState.current_project["status"]),
                ),
                align_items="center",
                width="100%",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Description:", font_weight="bold"),
                    rx.text(ProjectState.current_project["description"]),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Client: ", font_weight="bold"),
                        rx.text(ProjectState.current_project["client_name"]),
                        rx.spacer(),
                        rx.text("Due Date: ", font_weight="bold"),
                        rx.text(ProjectState.current_project["due_date"]),
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Progress: ", font_weight="bold"),
                        rx.progress(
                            value=ProjectState.task_completion_percentage,
                            max=100,
                            height="8px",
                            flex="1",
                        ),
                        rx.text(
                            ProjectState.task_completion_percentage.to(str),
                            margin_left="3",
                        ),
                        width="100%",
                        align_items="center",
                    ),
                    rx.divider(),
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Tasks", size="6"),
                            rx.spacer(),
                            rx.input(
                                placeholder="Add a new task...",
                                value=ProjectState.task_title,
                                on_change=ProjectState.set_task_title,
                                flex="1",
                            ),
                            rx.button(
                                "Add Task",
                                on_click=ProjectState.add_task,
                                color_scheme="blue",
                                size="2",
                            ),
                            align_items="center",
                            width="100%",
                        ),
                        rx.cond(
                            ProjectState.tasks.length() > 0,
                            task_list(),
                            rx.text(
                                "No tasks yet. Add your first task above!",
                                size="4",
                                color_scheme="gray",
                            ),
                        ),
                        spacing="3",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                ),
                padding="6",
                border="1px solid",
                border_color="gray.200",
                border_radius="lg",
                margin_top="4",
            ),
            spacing="5",
            width="100%",
            min_height="85vh",
        ),
    )
