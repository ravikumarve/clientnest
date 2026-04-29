import reflex as rx
from ..models.invoice import Invoice
from ..models.user import User
from ..models.project import Project
from ..state.auth import AuthState
from typing import List, Dict


class InvoiceState(rx.State):
    """State for invoice management."""

    invoices: List[Dict] = []  # type: ignore
    current_invoice: Dict = {}
    creating: bool = False

    # Form fields
    client_id: int = 0
    project_id: int = 0
    amount: float = 0.0
    currency: str = "USD"
    due_date: str = ""
    notes: str = ""

    @rx.event
    def load_invoices(self):
        """Load all invoices for the agency."""
        with rx.session() as session:
            invoices = (
                session.query(Invoice)
                .filter(Invoice.agency_id == AuthState.agency_id)
                .order_by(Invoice.created_at.desc())
                .all()
            )

            result = []
            for inv in invoices:
                client = session.query(User).filter(User.id == inv.client_id).first()
                client_name = client.name if client else "Unknown Client"

                project_name = ""
                if inv.project_id:
                    project = (
                        session.query(Project)
                        .filter(Project.id == inv.project_id)
                        .first()
                    )
                    project_name = project.title if project else ""

                result.append(
                    {
                        "id": inv.id,
                        "client_id": inv.client_id,
                        "client_name": client_name,
                        "project_id": inv.project_id,
                        "project_name": project_name,
                        "amount": inv.amount,
                        "currency": inv.currency,
                        "status": inv.status,
                        "due_date": inv.due_date.strftime("%Y-%m-%d")
                        if inv.due_date
                        else "",
                        "paid_at": inv.paid_at.strftime("%Y-%m-%d")
                        if inv.paid_at
                        else "",
                        "created_at": inv.created_at.strftime("%Y-%m-%d")
                        if inv.created_at
                        else "",
                        "notes": inv.notes or "",
                    }
                )

            self.invoices = result

    @rx.event
    def create_invoice(self, form_data: Dict):
        """Create a new invoice."""
        self.creating = True

        try:
            with rx.session() as session:
                invoice = Invoice(
                    agency_id=AuthState.agency_id,
                    client_id=int(form_data.get("client_id", 0)),
                    project_id=int(form_data.get("project_id", 0)) or None,
                    amount=float(form_data.get("amount", 0)),
                    currency=form_data.get("currency", "USD"),
                    due_date=form_data.get("due_date"),
                    notes=form_data.get("notes", ""),
                )
                session.add(invoice)
                session.commit()
                session.refresh(invoice)

                # Generate LemonSqueezy checkout URL (placeholder)
                # This would be implemented with actual LemonSqueezy integration
                checkout_url = f"https://app.lemonsqueezy.com/checkout/buy/{invoice.id}"

                invoice.lemonsqueezy_checkout_url = checkout_url
                session.commit()

                self.creating = False
                yield rx.redirect("/invoices")

        except Exception as e:
            print(f"Error creating invoice: {e}")
            self.creating = False

    @rx.event
    def set_client_id(self, value: str):
        self.client_id = int(value) if value else 0

    @rx.event
    def set_project_id(self, value: str):
        self.project_id = int(value) if value else 0

    @rx.event
    def set_amount(self, value: str):
        self.amount = float(value) if value else 0.0

    @rx.event
    def set_currency(self, value: str):
        self.currency = value

    @rx.event
    def set_due_date(self, value: str):
        self.due_date = value

    @rx.event
    def set_notes(self, value: str):
        self.notes = value
