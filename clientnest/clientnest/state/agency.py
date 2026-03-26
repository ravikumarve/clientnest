import reflex as rx
from ..models.agency import Agency
from ..models.user import User
from ..models.project import Project
from ..email import EmailService
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import List


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

    # Logo upload state
    is_logo_uploading: bool = False

    # Explicit setters — required in Reflex 0.8.9+
    def set_search_term(self, value: str):
        self.search_term = value

    def set_invite_name(self, value: str):
        self.invite_name = value

    def set_invite_email(self, value: str):
        self.invite_email = value

    def set_is_logo_uploading(self, value: bool):
        self.is_logo_uploading = value

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
            c
            for c in self.clients
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

            clients = (
                session.query(User)
                .filter(
                    User.agency_id == agency_id,
                    User.role == "client",
                )
                .all()
            )

            self.clients = [
                {
                    "id": c.id,
                    "name": c.name,
                    "email": c.email,
                    "projects_count": 0,
                    "last_active": c.last_login.strftime("%b %d, %Y")
                    if c.last_login
                    else "Never",
                }
                for c in clients
            ]

    @rx.event
    def update_brand_color(self, color: str):
        """Update agency brand color."""
        self.brand_color = color
        # In a real implementation, save to database
        return rx.toast.success("Brand color updated")

    @rx.event
    def update_logo(self, logo_url: str):
        """Update agency logo."""
        self.logo_url = logo_url
        # In a real implementation, save to database
        return rx.toast.success("Logo updated")

    @rx.event
    def handle_logo_upload(self, files: List[rx.UploadFile]):
        """Handle logo file upload."""
        if not files:
            return

        self.is_logo_uploading = True

        try:
            file = files[0]  # Only handle first file

            # Check if file is an image
            if not file.content_type.startswith("image/"):
                return rx.toast.error("Please upload an image file")

            # Check file size (max 2MB)
            content = file.read()
            if len(content) > 2 * 1024 * 1024:
                return rx.toast.error("Logo must be less than 2MB")

            # Create uploads directory
            uploads_dir = Path("uploads/agency-logos")
            uploads_dir.mkdir(exist_ok=True, parents=True)

            # Generate unique filename
            unique_id = str(uuid.uuid4())
            file_extension = Path(file.filename).suffix
            stored_filename = f"{unique_id}{file_extension}"
            file_path = uploads_dir / stored_filename

            # Write file
            with open(file_path, "wb") as f:
                f.write(content)

            # Update logo URL
            self.logo_url = f"/uploads/agency-logos/{stored_filename}"

            # In a real implementation, save to database
            return rx.toast.success("Logo uploaded successfully")

        finally:
            self.is_logo_uploading = False

    @rx.event
    def serve_logo(self, logo_path: str):
        """Serve logo file."""
        if logo_path.startswith("/uploads/agency-logos/"):
            file_path = Path(".") / logo_path[1:]  # Remove leading slash
            if file_path.exists():
                return rx.file(file_path)
        return rx.window_alert("Logo not found")

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

        # Generate invite token
        invite_token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + timedelta(days=7)

        # Store token in database (in a real implementation)
        # For now, we'll just store it in memory for the demo
        self.invite_token = invite_token
        self.invite_expires_at = expires_at.isoformat()

        # Send invitation email
        email_sent = EmailService.send_invite_email(
            to_email=self.invite_email,
            agency_name=self.agency.get("name", "Your Agency"),
            invite_token=invite_token,
            inviter_name=self.get_state(rx.State).current_user.get(
                "name", "A team member"
            ),
        )

        email = self.invite_email
        self.clear_invite_form()

        if email_sent:
            return rx.toast.success(f"Invitation sent to {email}")
        else:
            return rx.toast.warning(
                f"Invitation created for {email} but email failed to send"
            )
