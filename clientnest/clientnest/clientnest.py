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
)
from .state.message import MessageState
from .state.invoice import InvoiceState
from .state.agency import AgencyState
from .state.project import ProjectState


class State(rx.State):
    """The base app state."""

    pass


app = rx.App()
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
