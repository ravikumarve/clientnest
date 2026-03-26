import reflex as rx
from ..models.project import Project, Task
from ..models.user import User
from ..models.agency import Agency
from typing import List, Dict, Any
import uuid


class ProjectState(rx.State):
    """State for project management."""

    # Project data
    projects: list[dict] = []
    current_project: dict = {}
    tasks: list[dict] = []
    project_filter: str = "all"  # all | active | review | completed

    # Form data for creating/editing
    project_title: str = ""
    project_description: str = ""
    project_due_date: str = ""
    selected_client_id: int = None

    # Task form data
    task_title: str = ""

    # Setter methods for form fields
    def set_project_title(self, value: str):
        self.project_title = value

    def set_project_description(self, value: str):
        self.project_description = value

    def set_project_due_date(self, value: str):
        self.project_due_date = value

    def set_task_title(self, value: str):
        self.task_title = value

    # UI state
    show_create_form: bool = False

    @rx.event
    def load_projects(self):
        """Load projects for the current agency."""
        with rx.session() as session:
            # Get agency_id from AuthState
            agency_id = (
                self.get_state(rx.State).agency_id
                if hasattr(self.get_state(rx.State), "agency_id")
                else 1
            )

            # Query projects for this agency
            projects_query = session.query(Project).filter(
                Project.agency_id == agency_id
            )

            # Apply filter
            if self.project_filter == "active":
                projects_query = projects_query.filter(
                    Project.status.in_(["not_started", "in_progress", "review"])
                )
            elif self.project_filter == "review":
                projects_query = projects_query.filter(Project.status == "review")
            elif self.project_filter == "completed":
                projects_query = projects_query.filter(Project.status == "completed")

            projects = projects_query.all()

            # Convert to list of dicts
            self.projects = [
                {
                    "id": p.id,
                    "title": p.title,
                    "description": p.description,
                    "status": p.status,
                    "due_date": p.due_date.isoformat() if p.due_date else None,
                    "created_at": p.created_at.isoformat() if p.created_at else None,
                    "updated_at": p.updated_at.isoformat() if p.updated_at else None,
                    "client_id": p.client_id,
                    "agency_id": p.agency_id,
                }
                for p in projects
            ]

    @rx.event
    def load_project(self, project_id: int):
        """Load a specific project and its tasks."""
        with rx.session() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if project:
                # Get client name
                client = (
                    session.query(User).filter(User.id == project.client_id).first()
                )
                client_name = client.name if client else "Unknown"

                # Get agency name
                agency = (
                    session.query(Agency).filter(Agency.id == project.agency_id).first()
                )
                agency_name = agency.name if agency else "Unknown"

                # Get tasks
                tasks = (
                    session.query(Task)
                    .filter(Task.project_id == project_id)
                    .order_by(Task.sort_order)
                    .all()
                )

                self.current_project = {
                    "id": project.id,
                    "title": project.title,
                    "description": project.description,
                    "status": project.status,
                    "due_date": project.due_date.isoformat()
                    if project.due_date
                    else None,
                    "created_at": project.created_at.isoformat()
                    if project.created_at
                    else None,
                    "updated_at": project.updated_at.isoformat()
                    if project.updated_at
                    else None,
                    "client_id": project.client_id,
                    "client_name": client_name,
                    "agency_id": project.agency_id,
                    "agency_name": agency_name,
                }

                self.tasks = [
                    {
                        "id": t.id,
                        "title": t.title,
                        "is_done": t.is_done,
                        "sort_order": t.sort_order,
                        "created_at": t.created_at.isoformat()
                        if t.created_at
                        else None,
                    }
                    for t in tasks
                ]

    @rx.event
    def create_project(self, form_data: dict):
        """Create a new project."""
        with rx.session() as session:
            # Get agency_id from AuthState
            agency_id = (
                self.get_state(rx.State).agency_id
                if hasattr(self.get_state(rx.State), "agency_id")
                else 1
            )

            project = Project(
                agency_id=agency_id,
                client_id=form_data.get("client_id"),
                title=form_data.get("title"),
                description=form_data.get("description"),
                due_date=form_data.get("due_date")
                if form_data.get("due_date")
                else None,
                status="not_started",
            )
            session.add(project)
            session.commit()

            # Clear form
            self.project_title = ""
            self.project_description = ""
            self.project_due_date = ""
            self.selected_client_id = None

            # Reload projects
            self.load_projects()

            return rx.toast.success("Project created successfully!")

    @rx.event
    def update_project_status(self, project_id: int, status: str):
        """Update project status."""
        with rx.session() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if project:
                project.status = status
                session.commit()

                # Reload current project if it's the one being updated
                if self.current_project.get("id") == project_id:
                    self.load_project(project_id)

                # Reload projects list
                self.load_projects()

                return rx.toast.success(f"Project status updated to {status}")

    @rx.event
    def add_task(self):
        """Add a new task to the current project."""
        if not self.task_title.strip():
            return rx.toast.error("Task title cannot be empty")

        if not self.current_project.get("id"):
            return rx.toast.error("No project selected")

        with rx.session() as session:
            # Get max sort order
            max_sort_order = (
                session.query(Task)
                .filter(Task.project_id == self.current_project["id"])
                .order_by(Task.sort_order.desc())
                .first()
            )
            next_sort_order = (max_sort_order.sort_order + 1) if max_sort_order else 0

            task = Task(
                project_id=self.current_project["id"],
                title=self.task_title,
                sort_order=next_sort_order,
            )
            session.add(task)
            session.commit()

            # Clear form
            self.task_title = ""

            # Reload tasks
            self.load_project(self.current_project["id"])

            return rx.toast.success("Task added successfully!")

    @rx.event
    def toggle_task(self, task_id: int):
        """Toggle task completion status."""
        with rx.session() as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                task.is_done = not task.is_done
                session.commit()

                # Reload tasks
                self.load_project(self.current_project["id"])

                return rx.toast.success("Task updated")

    @rx.event
    def delete_task(self, task_id: int):
        """Delete a task."""
        with rx.session() as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                session.delete(task)
                session.commit()

                # Reload tasks
                self.load_project(self.current_project["id"])

                return rx.toast.success("Task deleted")

    @rx.event
    def delete_project(self, project_id: int):
        """Delete a project."""
        with rx.session() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if project:
                session.delete(project)
                session.commit()

                # Clear current project if it was deleted
                if self.current_project.get("id") == project_id:
                    self.current_project = {}
                    self.tasks = []

                # Reload projects
                self.load_projects()

                return rx.toast.success("Project deleted")

    @rx.event
    def set_project_filter(self, filter_value: str):
        """Set the project filter."""
        self.project_filter = filter_value
        self.load_projects()

    @rx.event
    def clear_project_form(self):
        """Clear the project form."""
        self.project_title = ""
        self.project_description = ""
        self.project_due_date = ""
        self.selected_client_id = None

    @rx.var
    def filtered_projects(self) -> List[Dict[str, Any]]:
        """Get projects based on current filter."""
        return self.projects

    @rx.var
    def project_status_color(self) -> str:
        """Get color for current project status."""
        status = self.current_project.get("status", "not_started")
        status_colors = {
            "not_started": "gray",
            "in_progress": "blue",
            "review": "amber",
            "completed": "green",
            "on_hold": "red",
        }
        return status_colors.get(status, "gray")

    @rx.var
    def task_completion_percentage(self) -> int:
        """Calculate percentage of completed tasks."""
        if not self.tasks:
            return 0
        completed_count = sum(1 for t in self.tasks if t["is_done"])
        return int((completed_count / len(self.tasks)) * 100)

    @rx.event
    def toggle_create_form(self):
        """Toggle the create project form visibility."""
        self.show_create_form = not self.show_create_form
