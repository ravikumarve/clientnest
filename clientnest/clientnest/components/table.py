"""
Enhanced Table Components - Glassmorphism Design
=================================================

Premium table components with glassmorphism effects for the Clientnest dashboard.
All tables use the new lusion.co-inspired design system with blur effects and smooth animations.
"""

import reflex as rx
from .glass import glass_button
from .badges import status_badge, role_badge, invoice_status_badge
from ..styles import (
    Colors,
    Typography,
    Spacing,
    BorderRadius,
    Shadows,
    Transitions,
)


def data_table(
    columns: list[dict],
    rows: list[dict],
    on_row_click: str = None,
) -> rx.Component:
    """
    Enhanced data table with glassmorphism design.
    
    Args:
        columns: List of column definitions with 'key', 'label', and optional 'width'.
        rows: List of row data dictionaries.
        on_row_click: Optional click handler for rows.
        
    Returns:
        A glassmorphism data table component.
    """
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    *[
                        rx.table.column_header_cell(
                            rx.text(
                                col["label"],
                                font_size=Typography.TEXT_SM,
                                font_weight=Typography.FONT_SEMIBOLD,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.MONO,
                                text_transform="uppercase",
                                letter_spacing="0.05em",
                            ),
                            width=col.get("width", "auto"),
                            padding="4",
                        )
                        for col in columns
                    ],
                    background="rgba(255, 255, 255, 0.02)",
                    border_bottom=f"1px solid {Colors.BORDER_DARK}",
                ),
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        *[
                            rx.table.cell(
                                rx.text(
                                    row.get(col["key"], ""),
                                    font_size=Typography.TEXT_BASE,
                                    color=Colors.TEXT_PRIMARY,
                                    font_family=Typography.SANS,
                                ),
                                width=col.get("width", "auto"),
                                padding="4",
                            )
                            for col in columns
                        ],
                        on_click=on_row_click,
                        cursor="pointer" if on_row_click else "default",
                        transition=Transitions.TRANSITION_FAST,
                        _hover={
                            "background": Colors.BG_HOVER,
                        } if on_row_click else {},
                        border_bottom=f"1px solid {Colors.BORDER_DARK}",
                    )
                    for row in rows
                ],
            ),
            variant="simple",
        ),
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_radius=BorderRadius.RADIUS_2XL,
        overflow="hidden",
        box_shadow=Shadows.SHADOW_LG,
    )


def project_table(projects: list[dict]) -> rx.Component:
    """
    Enhanced project table with glassmorphism design.
    
    Args:
        projects: List of project data dictionaries.
        
    Returns:
        A glassmorphism project table component.
    """
    columns = [
        {"key": "title", "label": "Project", "width": "30%"},
        {"key": "client_name", "label": "Client", "width": "20%"},
        {"key": "status", "label": "Status", "width": "15%"},
        {"key": "due_date", "label": "Due Date", "width": "15%"},
        {"key": "updated_at", "label": "Last Updated", "width": "20%"},
    ]
    
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    *[
                        rx.table.column_header_cell(
                            rx.text(
                                col["label"],
                                font_size=Typography.TEXT_SM,
                                font_weight=Typography.FONT_SEMIBOLD,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.MONO,
                                text_transform="uppercase",
                                letter_spacing="0.05em",
                            ),
                            width=col["width"],
                            padding="4",
                        )
                        for col in columns
                    ],
                    background="rgba(255, 255, 255, 0.02)",
                    border_bottom=f"1px solid {Colors.BORDER_DARK}",
                ),
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.cell(
                            rx.text(
                                project.get("title", "Untitled"),
                                font_size=Typography.TEXT_BASE,
                                font_weight=Typography.FONT_MEDIUM,
                                color=Colors.TEXT_PRIMARY,
                                font_family=Typography.SANS,
                            ),
                            width="30%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                project.get("client_name", "Unknown"),
                                font_size=Typography.TEXT_BASE,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.SANS,
                            ),
                            width="20%",
                            padding="4",
                        ),
                        rx.table.cell(
                            status_badge(project.get("status", "not_started")),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                format_date(project.get("due_date")),
                                font_size=Typography.TEXT_SM,
                                color=Colors.TEXT_TERTIARY,
                                font_family=Typography.MONO,
                            ),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                format_date(project.get("updated_at")),
                                font_size=Typography.TEXT_SM,
                                color=Colors.TEXT_TERTIARY,
                                font_family=Typography.MONO,
                            ),
                            width="20%",
                            padding="4",
                        ),
                        cursor="pointer",
                        transition=Transitions.TRANSITION_FAST,
                        _hover={
                            "background": Colors.BG_HOVER,
                        },
                        border_bottom=f"1px solid {Colors.BORDER_DARK}",
                    )
                    for project in projects
                ],
            ),
            variant="simple",
        ),
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_radius=BorderRadius.RADIUS_2XL,
        overflow="hidden",
        box_shadow=Shadows.SHADOW_LG,
    )


def client_table(clients: list[dict]) -> rx.Component:
    """
    Enhanced client table with glassmorphism design.
    
    Args:
        clients: List of client data dictionaries.
        
    Returns:
        A glassmorphism client table component.
    """
    columns = [
        {"key": "name", "label": "Name", "width": "25%"},
        {"key": "email", "label": "Email", "width": "30%"},
        {"key": "role", "label": "Role", "width": "15%"},
        {"key": "project_count", "label": "Projects", "width": "15%"},
        {"key": "last_login", "label": "Last Active", "width": "15%"},
    ]
    
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    *[
                        rx.table.column_header_cell(
                            rx.text(
                                col["label"],
                                font_size=Typography.TEXT_SM,
                                font_weight=Typography.FONT_SEMIBOLD,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.MONO,
                                text_transform="uppercase",
                                letter_spacing="0.05em",
                            ),
                            width=col["width"],
                            padding="4",
                        )
                        for col in columns
                    ],
                    background="rgba(255, 255, 255, 0.02)",
                    border_bottom=f"1px solid {Colors.BORDER_DARK}",
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
                                rx.text(
                                    client.get("name", "Unknown"),
                                    font_size=Typography.TEXT_BASE,
                                    font_weight=Typography.FONT_MEDIUM,
                                    color=Colors.TEXT_PRIMARY,
                                    font_family=Typography.SANS,
                                ),
                                align_items="center",
                                spacing="3",
                            ),
                            width="25%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                client.get("email", ""),
                                font_size=Typography.TEXT_BASE,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.SANS,
                            ),
                            width="30%",
                            padding="4",
                        ),
                        rx.table.cell(
                            role_badge(client.get("role", "client")),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                str(client.get("project_count", 0)),
                                font_size=Typography.TEXT_BASE,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.SANS,
                            ),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                format_date(client.get("last_login")),
                                font_size=Typography.TEXT_SM,
                                color=Colors.TEXT_TERTIARY,
                                font_family=Typography.MONO,
                            ),
                            width="15%",
                            padding="4",
                        ),
                        cursor="pointer",
                        transition=Transitions.TRANSITION_FAST,
                        _hover={
                            "background": Colors.BG_HOVER,
                        },
                        border_bottom=f"1px solid {Colors.BORDER_DARK}",
                    )
                    for client in clients
                ],
            ),
            variant="simple",
        ),
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_radius=BorderRadius.RADIUS_2XL,
        overflow="hidden",
        box_shadow=Shadows.SHADOW_LG,
    )


def invoice_table(invoices: list[dict]) -> rx.Component:
    """
    Enhanced invoice table with glassmorphism design.
    
    Args:
        invoices: List of invoice data dictionaries.
        
    Returns:
        A glassmorphism invoice table component.
    """
    columns = [
        {"key": "id", "label": "Invoice #", "width": "15%"},
        {"key": "client_name", "label": "Client", "width": "25%"},
        {"key": "amount", "label": "Amount", "width": "15%"},
        {"key": "status", "label": "Status", "width": "15%"},
        {"key": "due_date", "label": "Due Date", "width": "15%"},
        {"key": "actions", "label": "Actions", "width": "15%"},
    ]
    
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    *[
                        rx.table.column_header_cell(
                            rx.text(
                                col["label"],
                                font_size=Typography.TEXT_SM,
                                font_weight=Typography.FONT_SEMIBOLD,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.MONO,
                                text_transform="uppercase",
                                letter_spacing="0.05em",
                            ),
                            width=col["width"],
                            padding="4",
                        )
                        for col in columns
                    ],
                    background="rgba(255, 255, 255, 0.02)",
                    border_bottom=f"1px solid {Colors.BORDER_DARK}",
                ),
            ),
            rx.table.body(
                *[
                    rx.table.row(
                        rx.table.cell(
                            rx.text(
                                f"#{invoice.get('id', '')}",
                                font_size=Typography.TEXT_BASE,
                                font_weight=Typography.FONT_MEDIUM,
                                color=Colors.TEXT_PRIMARY,
                                font_family=Typography.MONO,
                            ),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                invoice.get("client_name", "Unknown"),
                                font_size=Typography.TEXT_BASE,
                                color=Colors.TEXT_SECONDARY,
                                font_family=Typography.SANS,
                            ),
                            width="25%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                format_currency(invoice.get("amount", 0), invoice.get("currency", "USD")),
                                font_size=Typography.TEXT_BASE,
                                font_weight=Typography.FONT_BOLD,
                                color=Colors.NEST_ACCENT,
                                font_family=Typography.DISPLAY,
                            ),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            invoice_status_badge(invoice.get("status", "unpaid")),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.text(
                                format_date(invoice.get("due_date")),
                                font_size=Typography.TEXT_SM,
                                color=Colors.TEXT_TERTIARY,
                                font_family=Typography.MONO,
                            ),
                            width="15%",
                            padding="4",
                        ),
                        rx.table.cell(
                            rx.hstack(
                                glass_button(
                                    "",
                                    variant="secondary",
                                    size="sm",
                                ),
                                glass_button(
                                    "",
                                    variant="ghost",
                                    size="sm",
                                ),
                                spacing="2",
                            ),
                            width="15%",
                            padding="4",
                        ),
                        cursor="pointer",
                        transition=Transitions.TRANSITION_FAST,
                        _hover={
                            "background": Colors.BG_HOVER,
                        },
                        border_bottom=f"1px solid {Colors.BORDER_DARK}",
                    )
                    for invoice in invoices
                ],
            ),
            variant="simple",
        ),
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_radius=BorderRadius.RADIUS_2XL,
        overflow="hidden",
        box_shadow=Shadows.SHADOW_LG,
    )


def empty_table(message: str = "No data available") -> rx.Component:
    """
    Enhanced empty table with glassmorphism design.
    
    Args:
        message: The message to display.
        
    Returns:
        A glassmorphism empty table component.
    """
    return rx.box(
        rx.vstack(
            rx.icon("inbox", size=8, color=Colors.TEXT_TERTIARY),
            rx.text(
                message,
                font_size=Typography.TEXT_BASE,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
            ),
            spacing="4",
            align_items="center",
        ),
        padding="9",
        text_align="center",
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_radius=BorderRadius.RADIUS_2XL,
    )


def loading_table() -> rx.Component:
    """
    Enhanced loading table with glassmorphism design.
    
    Returns:
        A glassmorphism loading table component.
    """
    return rx.box(
        rx.vstack(
            rx.spinner(size="6", color=Colors.NEST_ACCENT),
            rx.text(
                "Loading...",
                font_size=Typography.TEXT_BASE,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
            ),
            spacing="4",
            align_items="center",
        ),
        padding="9",
        text_align="center",
        background=Colors.BG_CARD,
        backdrop_filter="blur(16px)",
        webkit_backdrop_filter="blur(16px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_radius=BorderRadius.RADIUS_2XL,
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


__all__ = [
    "data_table",
    "project_table",
    "client_table",
    "invoice_table",
    "empty_table",
    "loading_table",
]