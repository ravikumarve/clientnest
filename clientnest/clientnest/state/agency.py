import reflex as rx
from ..models.agency import Agency
from ..models.user import User
from ..models.project import Project
import uuid
from datetime import datetime, timedelta


class AgencyState(rx.State):
    """Agency state."""

    # Agency data
    agency: dict = {}
    brand_color: str = "#2563EB"
    logo_url: str = ""
    plan: str = "free"
    is_subscribed: bool = False

    # Client data
    clients: list[dict] = []
    search_term: str = ""

    # Client invite data
    invite_name: str = ""
    invite_email: str = ""
    invite_token: str = ""
    invite_expires_at: str = ""
    show_invite_form: bool = False

    # Explicit setters — required in Reflex 0.8.9+
    def set_search_term(self, value: str):
        self.search_term = value

    def set_invite_name(self, value: str):
        self.invite_name = value

    def set_invite_email(self, value: str):
        self.invite_email = value

    @rx.var
    def can_invite_client(self) -> bool:
        if self.plan == "free":
            return len(self.clients) < 2
        return True

    @rx.var
    def has_white_label(self) -> bool:
        return self.plan in ["solo", "agency", "studio"]

    @rx.var
    def filtered_clients(self) -> list[dict]:
        if not self.search_term:
            return self.clients
        term = self.search_term.lower()
        return [
            c for c in self.clients
            if term in c["name"].lower() or term in c["email"].lower()
        ]

    @rx.event
    def load_agency(self):
        pass

    @rx.event
    def load_clients(self):
        with rx.session() as session:
            auth = self.get_state(rx.State)
            agency_id = getattr(auth, "agency_id", 1)

            clients = session.query(User).filter(
                User.agency_id == agency_id,
                User.role == "client",
            ).all()

            self.clients = [
                {
                    "id": c.id,
                    "name": c.name,
                    "email": c.email,
                    "projects_count": 0,
                    "last_active": c.last_login.strftime("%b %d, %Y") if c.last_login else "Never",
                }
                for c in clients
            ]

    @rx.event
    def toggle_invite_form(self):
        self.show_invite_form = not self.show_invite_form
        if not self.show_invite_form:
            self.invite_name = ""
            self.invite_email = ""
            self.invite_token = ""

    @rx.event
    def clear_invite_form(self):
        self.invite_name = ""
        self.invite_email = ""
        self.invite_token = ""
        self.invite_expires_at = ""
        self.show_invite_form = False

    @rx.event
    def invite_client(self):
        if not self.invite_email:
            return rx.toast.error("Please enter an email address")

        self.invite_token = str(uuid.uuid4())
        self.invite_expires_at = (datetime.utcnow() + timedelta(days=7)).isoformat()

        # TODO: store token in DB and send email with link
        email = self.invite_email
        self.clear_invite_form()
        return rx.toast.success(f"Invitation sent to {email}")
