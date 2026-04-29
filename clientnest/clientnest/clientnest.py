import reflex as rx
from rxconfig import config
from .pages import (
    index,
    auth,
    dashboard,
    projects,
    messages,
    files,
    invoices,
    settings,
    portal,
    webhooks,
    clients,
    white_label,
)
from .state.message import MessageState
from .state.invoice import InvoiceState
from .state.agency import AgencyState
from .state.project import ProjectState


class State(rx.State):
    """The base app state."""

    def check_session_expiry(self):
        """Check if session should expire based on last activity."""
        # Session expires after 24 hours of inactivity
        # In a real implementation, this would check last activity timestamp
        # For now, this is a placeholder for session management
        pass


app = rx.App(
    style={
        "background_color": "#030305",
        "color": "#f8fafc",
    }
)

# Add custom CSS file
with open("clientnest/clientnest/styles/custom.css", "r") as f:
    custom_css = f.read()
    # Add custom CSS to the app
    app.style = {
        "background_color": "#030305",
        "color": "#f8fafc",
        "custom_css": custom_css,
    }

app.add_page(index.index, route="/")
app.add_page(auth.login, route="/login")
app.add_page(auth.signup, route="/signup")
app.add_page(
    dashboard.dashboard, route="/dashboard", on_load=dashboard.DashboardState.load_data
)
app.add_page(projects.projects, route="/projects")
app.add_page(projects.project_detail, route="/projects/[id]")
app.add_page(
    messages.project_messages,
    route="/projects/[id]/messages",
    on_load=MessageState.load_messages,
)
app.add_page(files.project_files, route="/projects/[id]/files")
app.add_page(invoices.invoices, route="/invoices", on_load=InvoiceState.load_invoices)
app.add_page(invoices.new_invoice, route="/invoices/new")
app.add_page(settings.settings, route="/settings")
app.add_page(
    settings.billing, route="/settings/billing", on_load=AgencyState.load_agency
)

app.add_page(
    portal.client_portal, route="/portal", on_load=ProjectState.load_client_projects
)
app.add_page(webhooks.webhook_ls, route="/webhooks/lemonsqueezy")
app.add_page(auth.accept_invite, route="/accept-invite/[token]")
app.add_page(clients.clients, route="/clients")
app.add_page(
    white_label.white_label,
    route="/settings/white-label",
    on_load=AgencyState.load_agency,
)
