"""Card components for Clientnest."""
import reflex as rx
from datetime import datetime


def project_card(project: dict, on_click: str) -> rx.Component:
    """Create a project card component.
    
    Args:
        project: The project data.
        on_click: The click handler.
        
    Returns:
        A project card component.
    """
    from .badges import status_badge
    
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading(project.get("title", "Untitled Project"), size="5"),
                rx.spacer(),
                status_badge(project.get("status", "not_started")),
                align_items="center",
                width="100%",
            ),
            rx.text(
                project.get("description", "No description"),
                color="gray",
                size="1",
                no_of_lines=2,
            ),
            rx.spacer(),
            rx.hstack(
                rx.text(
                    f"Due: {format_date(project.get('due_date'))}",
                    size="1",
                    color="gray",
                ),
                rx.spacer(),
                rx.text(
                    f"Updated: {format_date(project.get('updated_at'))}",
                    size="1",
                    color="gray",
                ),
                align_items="center",
                width="100%",
            ),
            spacing="2",
            align_items="stretch",
        ),
        on_click=on_click,
        cursor="pointer",
        _hover={"background": "gray.2"},
        transition="all 0.2s",
    )


def client_card(client: dict, on_click: str) -> rx.Component:
    """Create a client card component.
    
    Args:
        client: The client data.
        on_click: The click handler.
        
    Returns:
        A client card component.
    """
    from .badges import role_badge
    
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.avatar(
                    name=client.get("name", "Unknown"),
                    src=client.get("avatar_url"),
                    size="md",
                ),
                rx.vstack(
                    rx.heading(client.get("name", "Unknown"), size="5"),
                    rx.text(
                        client.get("email", ""),
                        size="1",
                        color="gray",
                    ),
                    spacing="0",
                    align_items="start",
                ),
                rx.spacer(),
                role_badge(client.get("role", "client")),
                align_items="center",
                width="100%",
            ),
            rx.spacer(),
            rx.hstack(
                rx.text(
                    f"Projects: {client.get('project_count', 0)}",
                    size="1",
                    color="gray",
                ),
                rx.spacer(),
                rx.text(
                    f"Last active: {format_date(client.get('last_login'))}",
                    size="1",
                    color="gray",
                ),
                align_items="center",
                width="100%",
            ),
            spacing="2",
            align_items="stretch",
        ),
        on_click=on_click,
        cursor="pointer",
        _hover={"background": "gray.2"},
        transition="all 0.2s",
    )


def invoice_card(invoice: dict, on_click: str) -> rx.Component:
    """Create an invoice card component.
    
    Args:
        invoice: The invoice data.
        on_click: The click handler.
        
    Returns:
        An invoice card component.
    """
    from .badges import invoice_status_badge
    
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading(f"Invoice #{invoice.get('id', '')}", size="5"),
                rx.spacer(),
                invoice_status_badge(invoice.get("status", "unpaid")),
                align_items="center",
                width="100%",
            ),
            rx.hstack(
                rx.text(
                    f"Amount: {format_currency(invoice.get('amount', 0), invoice.get('currency', 'USD'))}",
                    size="2",
                    weight="bold",
                ),
                rx.spacer(),
                rx.text(
                    f"Due: {format_date(invoice.get('due_date'))}",
                    size="1",
                    color="gray",
                ),
                align_items="center",
                width="100%",
            ),
            rx.spacer(),
            rx.text(
                invoice.get("notes", "No notes"),
                size="1",
                color="gray",
                no_of_lines=2,
            ),
            spacing="2",
            align_items="stretch",
        ),
        on_click=on_click,
        cursor="pointer",
        _hover={"background": "gray.2"},
        transition="all 0.2s",
    )


def stat_card(title: str, value: str, icon: str, color: str = "blue") -> rx.Component:
    """Create a stat card component.
    
    Args:
        title: The stat title.
        value: The stat value.
        icon: The icon name.
        color: The color scheme.
        
    Returns:
        A stat card component.
    """
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.icon(icon, size=4),
                rx.spacer(),
                rx.text(title, size="1", color="gray"),
                align_items="center",
                width="100%",
            ),
            rx.heading(value, size="4"),
            spacing="2",
            align_items="start",
        ),
        padding="4",
        background=f"{color}.1",
        border=f"2px solid {color}.3",
    )


def file_card(file: dict, on_download: str, on_delete: str) -> rx.Component:
    """Create a file card component.
    
    Args:
        file: The file data.
        on_download: The download handler.
        on_delete: The delete handler.
        
    Returns:
        A file card component.
    """
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.icon("file", size=4),
                rx.vstack(
                    rx.heading(file.get("filename", "Unknown"), size="5"),
                    rx.text(
                        f"{format_file_size(file.get('file_size', 0))} • {format_date(file.get('created_at'))}",
                        size="1",
                        color="gray",
                    ),
                    spacing="0",
                    align_items="start",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.button(
                        rx.icon("download", size=3),
                        on_click=on_download,
                        color_scheme="blue",
                        variant="soft",
                    ),
                    rx.button(
                        rx.icon("trash", size=3),
                        on_click=on_delete,
                        color_scheme="red",
                        variant="soft",
                    ),
                    spacing="2",
                ),
                align_items="center",
                width="100%",
            ),
            rx.text(
                f"Uploaded by: {file.get('uploader_name', 'Unknown')}",
                size="1",
                color="gray",
            ),
            spacing="2",
            align_items="stretch",
        ),
        padding="3",
    )


def message_card(message: dict, is_own: bool = False) -> rx.Component:
    """Create a message card component.
    
    Args:
        message: The message data.
        is_own: Whether the message is from the current user.
        
    Returns:
        A message card component.
    """
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.avatar(
                    name=message.get("sender_name", "Unknown"),
                    src=message.get("sender_avatar"),
                    size="sm",
                ),
                rx.vstack(
                    rx.text(
                        message.get("sender_name", "Unknown"),
                        size="1",
                        weight="bold",
                    ),
                    rx.text(
                        format_time(message.get("created_at")),
                        size="1",
                        color="gray",
                    ),
                    spacing="0",
                    align_items="start",
                ),
                align_items="center",
                spacing="2",
            ),
            rx.text(
                message.get("body", ""),
                size="2",
            ),
            spacing="2",
            align_items="start",
        ),
        padding="3",
        background="blue.1" if is_own else "gray.1",
        align_self="start" if not is_own else "end",
        max_width="70%",
    )


def task_card(task: dict, on_toggle: str, on_delete: str) -> rx.Component:
    """Create a task card component.
    
    Args:
        task: The task data.
        on_toggle: The toggle handler.
        on_delete: The delete handler.
        
    Returns:
        A task card component.
    """
    return rx.card(
        rx.hstack(
            rx.checkbox(
                checked=task.get("is_done", False),
                on_change=on_toggle,
            ),
            rx.vstack(
                rx.text(
                    task.get("title", "Untitled"),
                    size="2",
                    decoration="line-through" if task.get("is_done", False) else "none",
                    color="gray" if task.get("is_done", False) else "inherit",
                ),
                rx.text(
                    format_date(task.get("created_at")),
                    size="1",
                    color="gray",
                ),
                spacing="0",
                align_items="start",
            ),
            rx.spacer(),
            rx.button(
                rx.icon("trash", size=3),
                on_click=on_delete,
                color_scheme="red",
                variant="ghost",
                size="1",
            ),
            align_items="center",
            spacing="3",
            width="100%",
        ),
        padding="2",
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
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return date.strftime("%b %d, %Y")
    except Exception:
        return "Invalid date"


def format_time(date_str: str) -> str:
    """Format a time string.
    
    Args:
        date_str: The date string to format.
        
    Returns:
        The formatted time string.
    """
    if not date_str:
        return "N/A"
    
    try:
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return date.strftime("%I:%M %p")
    except Exception:
        return "Invalid time"


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
