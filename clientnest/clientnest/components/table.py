"""Table components for Clientnest."""
import reflex as rx


def data_table(
    columns: list[dict],
    rows: list[dict],
    on_row_click: str = None,
) -> rx.Component:
    """Create a data table component.
    
    Args:
        columns: List of column definitions with 'key', 'label', and optional 'width'.
        rows: List of row data dictionaries.
        on_row_click: Optional click handler for rows.
        
    Returns:
        A data table component.
    """
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[
                    rx.table.column_header_cell(
                        rx.text(col["label"]),
                        width=col.get("width", "auto"),
                    )
                    for col in columns
                ],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    *[
                        rx.table.cell(
                            rx.text(row.get(col["key"], "")),
                            width=col.get("width", "auto"),
                        )
                        for col in columns
                    ],
                    on_click=on_row_click,
                    cursor="pointer" if on_row_click else "default",
                    _hover={"background": "gray.1"} if on_row_click else {},
                )
                for row in rows
            ],
        ),
        variant="simple",
    )


def sortable_table(
    columns: list[dict],
    rows: list[dict],
    sort_field: str = None,
    sort_direction: str = "asc",
    on_sort: str = None,
    on_row_click: str = None,
) -> rx.Component:
    """Create a sortable data table component.
    
    Args:
        columns: List of column definitions with 'key', 'label', and optional 'width'.
        rows: List of row data dictionaries.
        sort_field: The current sort field.
        sort_direction: The current sort direction ('asc' or 'desc').
        on_sort: Optional sort handler.
        on_row_click: Optional click handler for rows.
        
    Returns:
        A sortable data table component.
    """
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[
                    rx.table.column_header_cell(
                        rx.hstack(
                            rx.text(col["label"]),
                            rx.cond(
                                sort_field == col["key"],
                                rx.icon(
                                    "arrow-up" if sort_direction == "asc" else "arrow-down",
                                    size=3,
                                ),
                            ),
                            align_items="center",
                            spacing="1",
                            cursor="pointer" if on_sort else "default",
                            on_click=on_sort if on_sort else None,
                        ),
                        width=col.get("width", "auto"),
                    )
                    for col in columns
                ],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    *[
                        rx.table.cell(
                            rx.text(row.get(col["key"], "")),
                            width=col.get("width", "auto"),
                        )
                        for col in columns
                    ],
                    on_click=on_row_click,
                    cursor="pointer" if on_row_click else "default",
                    _hover={"background": "gray.1"} if on_row_click else {},
                )
                for row in rows
            ],
        ),
        variant="simple",
    )


def project_table(projects: list[dict]) -> rx.Component:
    """Create a project table component.
    
    Args:
        projects: List of project data dictionaries.
        
    Returns:
        A project table component.
    """
    from .badges import status_badge
    
    columns = [
        {"key": "title", "label": "Project", "width": "30%"},
        {"key": "client_name", "label": "Client", "width": "20%"},
        {"key": "status", "label": "Status", "width": "15%"},
        {"key": "due_date", "label": "Due Date", "width": "15%"},
        {"key": "updated_at", "label": "Last Updated", "width": "20%"},
    ]
    
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[
                    rx.table.column_header_cell(
                        rx.text(col["label"]),
                        width=col["width"],
                    )
                    for col in columns
                ],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(
                        rx.text(project.get("title", "Untitled")),
                        width="30%",
                    ),
                    rx.table.cell(
                        rx.text(project.get("client_name", "Unknown")),
                        width="20%",
                    ),
                    rx.table.cell(
                        status_badge(project.get("status", "not_started")),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(format_date(project.get("due_date"))),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(format_date(project.get("updated_at"))),
                        width="20%",
                    ),
                    cursor="pointer",
                    _hover={"background": "gray.1"},
                )
                for project in projects
            ],
        ),
        variant="simple",
    )


def client_table(clients: list[dict]) -> rx.Component:
    """Create a client table component.
    
    Args:
        clients: List of client data dictionaries.
        
    Returns:
        A client table component.
    """
    from .badges import role_badge
    
    columns = [
        {"key": "name", "label": "Name", "width": "25%"},
        {"key": "email", "label": "Email", "width": "30%"},
        {"key": "role", "label": "Role", "width": "15%"},
        {"key": "project_count", "label": "Projects", "width": "15%"},
        {"key": "last_login", "label": "Last Active", "width": "15%"},
    ]
    
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[
                    rx.table.column_header_cell(
                        rx.text(col["label"]),
                        width=col["width"],
                    )
                    for col in columns
                ],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(
                        rx.hstack(
                            rx.avatar(
                                name=client.get("name", "Unknown"),
                                src=client.get("avatar_url"),
                                size="sm",
                            ),
                            rx.text(client.get("name", "Unknown")),
                            align_items="center",
                            spacing="2",
                        ),
                        width="25%",
                    ),
                    rx.table.cell(
                        rx.text(client.get("email", "")),
                        width="30%",
                    ),
                    rx.table.cell(
                        role_badge(client.get("role", "client")),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(str(client.get("project_count", 0))),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(format_date(client.get("last_login"))),
                        width="15%",
                    ),
                    cursor="pointer",
                    _hover={"background": "gray.1"},
                )
                for client in clients
            ],
        ),
        variant="simple",
    )


def invoice_table(invoices: list[dict]) -> rx.Component:
    """Create an invoice table component.
    
    Args:
        invoices: List of invoice data dictionaries.
        
    Returns:
        An invoice table component.
    """
    from .badges import invoice_status_badge
    
    columns = [
        {"key": "id", "label": "Invoice #", "width": "15%"},
        {"key": "client_name", "label": "Client", "width": "25%"},
        {"key": "amount", "label": "Amount", "width": "15%"},
        {"key": "status", "label": "Status", "width": "15%"},
        {"key": "due_date", "label": "Due Date", "width": "15%"},
        {"key": "actions", "label": "Actions", "width": "15%"},
    ]
    
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[
                    rx.table.column_header_cell(
                        rx.text(col["label"]),
                        width=col["width"],
                    )
                    for col in columns
                ],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(
                        rx.text(f"#{invoice.get('id', '')}"),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(invoice.get("client_name", "Unknown")),
                        width="25%",
                    ),
                    rx.table.cell(
                        rx.text(
                            format_currency(invoice.get("amount", 0), invoice.get("currency", "USD"))
                        ),
                        width="15%",
                    ),
                    rx.table.cell(
                        invoice_status_badge(invoice.get("status", "unpaid")),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(format_date(invoice.get("due_date"))),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.hstack(
                            rx.button(
                                rx.icon("download", size=3),
                                variant="soft",
                                size="1",
                            ),
                            rx.button(
                                rx.icon("send", size=3),
                                variant="soft",
                                size="1",
                            ),
                            spacing="1",
                        ),
                        width="15%",
                    ),
                    cursor="pointer",
                    _hover={"background": "gray.1"},
                )
                for invoice in invoices
            ],
        ),
        variant="simple",
    )


def file_table(files: list[dict]) -> rx.Component:
    """Create a file table component.
    
    Args:
        files: List of file data dictionaries.
        
    Returns:
        A file table component.
    """
    columns = [
        {"key": "filename", "label": "File Name", "width": "30%"},
        {"key": "uploader_name", "label": "Uploaded By", "width": "20%"},
        {"key": "file_size", "label": "Size", "width": "15%"},
        {"key": "created_at", "label": "Upload Date", "width": "20%"},
        {"key": "actions", "label": "Actions", "width": "15%"},
    ]
    
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                *[
                    rx.table.column_header_cell(
                        rx.text(col["label"]),
                        width=col["width"],
                    )
                    for col in columns
                ],
            ),
        ),
        rx.table.body(
            *[
                rx.table.row(
                    rx.table.cell(
                        rx.hstack(
                            rx.icon("file", size=4),
                            rx.text(file.get("filename", "Unknown")),
                            align_items="center",
                            spacing="2",
                        ),
                        width="30%",
                    ),
                    rx.table.cell(
                        rx.text(file.get("uploader_name", "Unknown")),
                        width="20%",
                    ),
                    rx.table.cell(
                        rx.text(format_file_size(file.get("file_size", 0))),
                        width="15%",
                    ),
                    rx.table.cell(
                        rx.text(format_date(file.get("created_at"))),
                        width="20%",
                    ),
                    rx.table.cell(
                        rx.hstack(
                            rx.button(
                                rx.icon("download", size=3),
                                variant="soft",
                                size="1",
                            ),
                            rx.button(
                                rx.icon("trash", size=3),
                                variant="soft",
                                size="1",
                                color_scheme="red",
                            ),
                            spacing="1",
                        ),
                        width="15%",
                    ),
                    cursor="pointer",
                    _hover={"background": "gray.1"},
                )
                for file in files
            ],
        ),
        variant="simple",
    )


def empty_table(message: str = "No data available") -> rx.Component:
    """Create an empty table component.
    
    Args:
        message: The message to display.
        
    Returns:
        An empty table component.
    """
    return rx.box(
        rx.vstack(
            rx.icon("inbox", size=8, color="gray"),
            rx.text(message, size="2", color="gray"),
            spacing="4",
            align_items="center",
        ),
        padding="8",
        text_align="center",
    )


def loading_table() -> rx.Component:
    """Create a loading table component.
    
    Returns:
        A loading table component.
    """
    return rx.box(
        rx.vstack(
            rx.spinner(size="6"),
            rx.text("Loading...", size="2", color="gray"),
            spacing="4",
            align_items="center",
        ),
        padding="8",
        text_align="center",
    )


# Helper functions

def format_date(date_str: str) -> str:
    """Format a date string.
    
    Args:
        date_str: The date string to format.
        
    Returns:
        The formatted date string.
    """
    if not date_str:
        return "N/A"
    
    try:
        from datetime import datetime
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return date.strftime("%b %d, %Y")
    except Exception:
        return "Invalid date"


def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a currency amount.
    
    Args:
        amount: The amount to format.
        currency: The currency code.
        
    Returns:
        The formatted currency string.
    """
    symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "INR": "₹",
    }
    
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:.2f}"


def format_file_size(size: int) -> str:
    """Format a file size.
    
    Args:
        size: The file size in bytes.
        
    Returns:
        The formatted file size string.
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"
