import reflex as rx
import bcrypt
from datetime import datetime
from ..models.user import User
from ..models.agency import Agency


class AuthState(rx.State):
    """Authentication state."""

    user_id: int = None
    agency_id: int = None
    role: str = None
    is_logged_in: bool = False
    current_user: dict = {}

    @rx.event
    def login(self, form_data: dict):
        """Handle user login."""
        email = form_data.get("email")
        password = form_data.get("password")

        with rx.session() as session:
            user = session.query(User).filter(User.email == email).first()
            if user and bcrypt.checkpw(
                password.encode("utf-8"), user.password_hash.encode("utf-8")
            ):
                # Set session variables
                self.user_id = user.id
                self.agency_id = user.agency_id
                self.role = user.role
                self.is_logged_in = True
                self.current_user = {
                    "id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "role": user.role,
                    "agency_id": user.agency_id,
                }
                # Update last login
                user.last_login = datetime.utcnow()
                session.commit()

                # Redirect based on role
                if self.role == "client":
                    return rx.redirect("/portal")
                else:
                    return rx.redirect("/dashboard")
            else:
                # Return error message (will be handled in component)
                return rx.window_alert("Invalid email or password")

    @rx.event
    def logout(self):
        """Handle user logout."""
        self.user_id = None
        self.agency_id = None
        self.role = None
        self.is_logged_in = False
        self.current_user = {}
        return rx.redirect("/")

    @rx.event
    def register(self, form_data: dict):
        """Handle user registration."""
        agency_name = form_data.get("agency_name")
        your_name = form_data.get("your_name")
        email = form_data.get("email")
        password = form_data.get("password")

        with rx.session() as session:
            # Check if email already exists
            existing_user = session.query(User).filter(User.email == email).first()
            if existing_user:
                return rx.window_alert("Email already registered")

            # Create agency with auto-generated slug
            slug = agency_name.lower().replace(" ", "-")
            # Ensure slug is unique
            counter = 1
            original_slug = slug
            while session.query(Agency).filter(Agency.slug == slug).first():
                slug = f"{original_slug}-{counter}"
                counter += 1

            agency = Agency(name=agency_name, slug=slug)
            session.add(agency)
            session.flush()  # Get agency ID

            # Create user
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            user = User(
                agency_id=agency.id,
                email=email,
                password_hash=hashed_password,
                role="owner",
                name=your_name,
            )
            session.add(user)
            session.commit()

            # Set session variables
            self.user_id = user.id
            self.agency_id = agency.id
            self.role = user.role
            self.is_logged_in = True
            self.current_user = {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role,
                "agency_id": user.agency_id,
            }

            return rx.redirect("/dashboard")

    @rx.event
    def accept_invite(self, form_data: dict):
        """Handle client invitation acceptance."""
        token = self.router.page.params.get("token")
        name = form_data.get("name")
        password = form_data.get("password")

        if not all([token, name, password]):
            return rx.toast.error("Please fill in all fields")

        # TODO: Validate token against database
        # For now, we'll assume token is valid and create the user

        with rx.session() as session:
            # Check if email already exists
            existing_user = session.query(User).filter(User.email == token).first()
            if existing_user:
                return rx.toast.error("User already exists with this email")

            # Create user with client role
            # In a real implementation, we'd lookup the agency from the token
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")

            # For demo purposes, create user with a default agency
            user = User(
                agency_id=1,  # Default agency for demo
                email=token,  # Using token as email for demo
                password_hash=hashed_password,
                role="client",
                name=name,
            )
            session.add(user)
            session.commit()

            # Set session
            self.user_id = user.id
            self.agency_id = user.agency_id
            self.role = user.role
            self.is_logged_in = True
            self.current_user = {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role,
                "agency_id": user.agency_id,
            }

            return rx.redirect("/portal")
