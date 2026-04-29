import reflex as rx
from ..state.invoice import InvoiceState
from ..state.auth import AuthState


def invoices() -> rx.Component:
    """Invoice list page."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.hstack(
                rx.heading("Invoices", size="8"),
                rx.spacer(),
                rx.button(
                    "Create Invoice",
                    on_click=rx.redirect("/invoices/new"),
                    size="3",
                ),
                width="100%",
                align="center",
            ),
            rx.cond(
                InvoiceState.invoices,
                rx.data_table(
                    data=InvoiceState.invoices,
                    columns=[
                        {"title": "ID", "accessor": "id"},
                        {"title": "Client", "accessor": "client_name"},
                        {"title": "Amount", "accessor": "amount", "format": "currency"},
                        {"title": "Currency", "accessor": "currency"},
                        {"title": "Status", "accessor": "status"},
                        {"title": "Due Date", "accessor": "due_date"},
                        {"title": "Actions", "accessor": "actions"},
                    ],
                    search=True,
                    pagination=True,
                    sort=True,
                ),
                rx.text("No invoices found", size="4"),
            ),
            spacing="5",
            width="100%",
        ),
    )


def new_invoice() -> rx.Component:
    """Create new invoice page."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Create New Invoice", size="8"),
            rx.form(
                rx.vstack(
                    rx.select(
                        "Select Client",
                        name="client_id",
                        on_change=InvoiceState.set_client_id,
                        placeholder="Choose a client",
                    ),
                    rx.select(
                        "Select Project (Optional)",
                        name="project_id",
                        on_change=InvoiceState.set_project_id,
                        placeholder="Choose a project",
                    ),
                    rx.input(
                        type="number",
                        name="amount",
                        placeholder="Amount",
                        step="0.01",
                        on_change=InvoiceState.set_amount,
                    ),
                    rx.select(
                        "Currency",
                        name="currency",
                        on_change=InvoiceState.set_currency,
                        default_value="USD",
                        options=["USD", "INR"],
                    ),
                    rx.input(
                        type="date",
                        name="due_date",
                        placeholder="Due Date",
                        on_change=InvoiceState.set_due_date,
                    ),
                    rx.text_area(
                        name="notes",
                        placeholder="Notes (optional)",
                        on_change=InvoiceState.set_notes,
                    ),
                    rx.button(
                        "Create Invoice",
                        type="submit",
                        loading=InvoiceState.creating,
                    ),
                    spacing="4",
                ),
                on_submit=InvoiceState.create_invoice,
            ),
            spacing="5",
            width="100%",
            max_width="600px",
        ),
    )
