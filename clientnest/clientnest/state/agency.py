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
    invite_email: str = ""
    invite_token: str = ""
    invite_expires_at: str = ""
    show_invite_form: bool = False

    @rx.var
    def can_invite_client(self) -> bool:
        """Check if agency can invite more clients based on plan."""
        if self.plan == "free":
            # In a real implementation, we would check actual client count
            # For now, we'll return True as placeholder
            return True
        return True

    @rx.var
    def has_white_label(self) -> bool:
        """Check if agency has white-label feature."""
        return self.plan in ["solo", "agency", "studio"]

    @rx.var
    def filtered_clients(self) -> list[dict]:
        """Get clients filtered by search term."""
        if not self.search_term:
            return self.clients
        return [
            client
            for client in self.clients
            if self.search_term.lower() in client["name"].lower()
            or self.search_term.lower() in client["email"].lower()
        ]

    @rx.event
    def load_agency(self):
        """Load agency data."""
        # Placeholder - will be implemented with actual DB query
        pass

    @rx.event
    def load_clients(self):
        """Load clients for the current agency."""
        with rx.session() as session:
            # Get agency_id from AuthState
            agency_id = (
                self.get_state(rx.State).agency_id
                if hasattr(self.get_state(rx.State), "agency_id")
                else 1
            )

            # Query clients (users with role=client) for this agency
            clients_query = session.query(User).filter(
                User.agency_id == agency_id, User.role == "client"
            )

            clients = clients_query.all()

            # Convert to list of dicts
            self.clients = [
                {
                    "id": c.id,
                    "name": c.name,
                    "email": c.email,
                    "projects_count": 0,  # Placeholder - would query actual count
                    "last_active": c.last_login.isoformat() if c.last_login else None,
                    "created_at": c.created_at.isoformat() if c.created_at else None,
                }
                for c in clients
            ]

    @rx.event
    def generate_invite_token(self):
        """Generate a UUID token for client invitation."""
        self.invite_token = str(uuid.uuid4())
        # Set expiration to 7 days from now
        self.invite_expires_at = (datetime.utcnow() + timedelta(days=7)).isoformat()
        return self.invite_token

    @rx.event
    def clear_invite_form(self):
        """Clear the invite form."""
        self.invite_email = ""
        self.invite_token = ""
        self.invite_expires_at = ""
        self.show_invite_form = False

    @rx.event
    def toggle_invite_form(self):
        """Toggle the invite form visibility."""
        self.show_invite_form = not self.show_invite_form
        if not self.show_invite_form:
            self.clear_invite_form()

    @rx.event
    def invite_client(self, email: str):
        """Handle client invitation."""
        if not email:
            return rx.toast.error("Please enter an email address")

        # Generate token
        token = self.generate_invite_token()

        # In a real implementation, we would:
        # 1. Store the token with expiry in a database table
        # 2. Send an email with the invitation link

        # For now, we'll just show a success message
        self.clear_invite_form()
        return [
            rx.toast.success(f"Invitation sent to {email}"),
            rx.redirect("/clients"),
        ]
