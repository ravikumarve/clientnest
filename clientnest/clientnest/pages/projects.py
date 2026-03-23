import reflex as rx
from ..state.project import ProjectState


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
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def projects_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Project Name"),
                rx.table.column_header_cell("Client"),
                rx.table.column_header_cell("Status"),
                rx.table.column_header_cell("Due Date"),
                rx.table.column_header_cell("Last Updated"),
                rx.table.column_header_cell("Actions"),
            )
        ),
        rx.table.body(
            rx.foreach(
                ProjectState.projects,
                lambda project: rx.table.row(
                    rx.table.cell(
                        rx.link(
                            project["title"],
                            href=f"/projects/{project['id']}",
                            underline="none",
                        )
                    ),
                    rx.table.cell(
                        rx.text("Client Name")  # Placeholder
                    ),
                    rx.table.cell(
                        rx.badge(
                            project["status"].replace("_", " ").title(),
                            color_scheme=rx.cond(
                                project["status"] == "completed",
                                "green",
                                rx.cond(
                                    project["status"] == "in_progress",
                                    "blue",
                                    rx.cond(
                                        project["status"] == "review",
                                        "amber",
                                        rx.cond(
                                            project["status"] == "on_hold",
                                            "red",
                                            "gray",
                                        ),
                                    ),
                                ),
                            ),
                        )
                    ),
                    rx.table.cell(project["due_date"] or "Not set"),
                    rx.table.cell(project["updated_at"] or project["created_at"]),
                    rx.table.cell(
                        rx.hstack(
                            rx.button(
                                rx.icon("eye"),
                                on_click=lambda: ProjectState.load_project(
                                    project["id"]
                                ),
                                size="1",
                                variant="ghost",
                            ),
                            rx.button(
                                rx.icon("trash-2"),
                                on_click=lambda: ProjectState.delete_project(
                                    project["id"]
                                ),
                                size="1",
                                variant="ghost",
                                color_scheme="red",
                            ),
                            spacing="2",
                        )
                    ),
                ),
            )
        ),
    )


def create_project_form() -> rx.Component:
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
            max_width="400px",
        ),
        position="fixed",
        top="20%",
        right="5%",
        z_index="1000",
        background_color="white",
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
                    ProjectState.current_project["status"].replace("_", " ").title(),
                    color_scheme=rx.cond(
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
                    ),
                ),
                align_items="center",
                width="100%",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Description:", font_weight="bold"),
                    rx.text(
                        ProjectState.current_project["description"]
                        or "No description provided"
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Client: ", font_weight="bold"),
                        rx.text(ProjectState.current_project["client_name"]),
                        rx.spacer(),
                        rx.text("Due Date: ", font_weight="bold"),
                        rx.text(ProjectState.current_project["due_date"] or "Not set"),
                        width="100%",
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Progress: ", font_weight="bold"),
                        rx.progress(
                            value=ProjectState.task_completion_percentage,
                            max=100,
                            height="8px",
                        ),
                        rx.text(
                            f"{ProjectState.task_completion_percentage}%",
                            margin_left="3",
                        ),
                        width="100%",
                    ),
                    rx.divider(),
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Tasks", size="6"),
                            rx.spacer(),
                            rx.input(
                                placeholder="Add a new task...",
                                value=ProjectState.task_title,
                                on_change=lambda e: setattr(
                                    ProjectState, "task_title", e.target.value
                                ),
                                on_key_down=lambda e: ProjectState.add_task()
                                if e.key == "Enter"
                                else None,
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
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def task_list() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            ProjectState.tasks,
            lambda task: rx.hstack(
                rx.checkbox(
                    is_checked=task["is_done"],
                    on_change=lambda: ProjectState.toggle_task(task["id"]),
                ),
                rx.text(
                    task["title"],
                    text_decoration=rx.cond(task["is_done"], "line-through", "none"),
                    color=rx.cond(task["is_done"], "gray", "black"),
                    flex="1",
                ),
                rx.button(
                    rx.icon("trash-2", size=16),
                    on_click=lambda: ProjectState.delete_task(task["id"]),
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
