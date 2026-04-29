"""
Enhanced Card Components - Glassmorphism Design
================================================

Premium card components with glassmorphism effects for the Clientnest dashboard.
All cards use the new lusion.co-inspired design system with blur effects and smooth animations.
"""

import reflex as rx
from datetime import datetime
from .glass import glass_card, glass_button
from .badges import status_badge, role_badge, invoice_status_badge
from ..styles import (
    Colors,
    Typography,
    Spacing,
    BorderRadius,
    Shadows,
    Transitions,
)


def project_card(project: dict, on_click: str) -> rx.Component:
    """
    Enhanced project card with glassmorphism design.
    
    Args:
        project: The project data.
        on_click: The click handler.
        
    Returns:
        A glassmorphism project card component.
    """
    return glass_card(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    project.get("title", "Untitled Project"),
                    size="5",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                ),
                status_badge(project.get("status", "not_started")),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            rx.text(
                project.get("description", "No description"),
                font_size=Typography.TEXT_BASE,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
                no_of_lines=2,
            ),
            rx.box(height="4"),
            rx.hstack(
                rx.text(
                    f"Due: {format_date(project.get('due_date'))}",
                    font_size=Typography.TEXT_SM,
                    color=Colors.TEXT_TERTIARY,
                    font_family=Typography.MONO,
                ),
                rx.text(
                    f"Updated: {format_date(project.get('updated_at'))}",
                    font_size=Typography.TEXT_SM,
                    color=Colors.TEXT_TERTIARY,
                    font_family=Typography.MONO,
                ),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            spacing="3",
            align_items="stretch",
        ),
        cursor="pointer",
        on_click=on_click,
        padding="6",
    )


def client_card(client: dict, on_click: str) -> rx.Component:
    """
    Enhanced client card with glassmorphism design.
    
    Args:
        client: The client data.
        on_click: The click handler.
        
    Returns:
        A glassmorphism client card component.
    """
    return glass_card(
        rx.vstack(
            rx.hstack(
                rx.avatar(
                    name=client.get("name", "Unknown"),
                    src=client.get("avatar_url"),
                    size="md",
                ),
                rx.vstack(
                    rx.heading(
                        client.get("name", "Unknown"),
                        size="5",
                        font_family=Typography.DISPLAY,
                        font_weight=Typography.FONT_BOLD,
                        color=Colors.TEXT_PRIMARY,
                    ),
                    rx.text(
                        client.get("email", ""),
                        font_size=Typography.TEXT_SM,
                        color=Colors.TEXT_TERTIARY,
                        font_family=Typography.SANS,
                    ),
                    spacing="1",
                    align_items="start",
                ),
                role_badge(client.get("role", "client")),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            rx.box(height="4"),
            rx.hstack(
                rx.text(
                    f"Projects: {client.get('project_count', 0)}",
                    font_size=Typography.TEXT_SM,
                    color=Colors.TEXT_TERTIARY,
                    font_family=Typography.MONO,
                ),
                rx.text(
                    f"Last active: {format_date(client.get('last_login'))}",
                    font_size=Typography.TEXT_SM,
                    color=Colors.TEXT_TERTIARY,
                    font_family=Typography.MONO,
                ),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            spacing="3",
            align_items="stretch",
        ),
        cursor="pointer",
        on_click=on_click,
        padding="6",
    )


def invoice_card(invoice: dict, on_click: str) -> rx.Component:
    """
    Enhanced invoice card with glassmorphism design.
    
    Args:
        invoice: The invoice data.
        on_click: The click handler.
        
    Returns:
        A glassmorphism invoice card component.
    """
    return glass_card(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    f"Invoice #{invoice.get('id', '')}",
                    size="5",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                ),
                invoice_status_badge(invoice.get("status", "unpaid")),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            rx.hstack(
                rx.text(
                    f"Amount: {format_currency(invoice.get('amount', 0), invoice.get('currency', 'USD'))}",
                    font_size=Typography.TEXT_2XL,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.NEST_ACCENT,
                    font_family=Typography.DISPLAY,
                ),
                rx.text(
                    f"Due: {format_date(invoice.get('due_date'))}",
                    font_size=Typography.TEXT_SM,
                    color=Colors.TEXT_TERTIARY,
                    font_family=Typography.MONO,
                ),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            rx.box(height="4"),
            rx.text(
                invoice.get("notes", "No notes"),
                font_size=Typography.TEXT_BASE,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
                no_of_lines=2,
            ),
            spacing="3",
            align_items="stretch",
        ),
        cursor="pointer",
        on_click=on_click,
        padding="6",
    )


def file_card(file: dict, on_download: str, on_delete: str) -> rx.Component:
    """
    Enhanced file card with glassmorphism design.
    
    Args:
        file: The file data.
        on_download: The download handler.
        on_delete: The delete handler.
        
    Returns:
        A glassmorphism file card component.
    """
    return glass_card(
        rx.vstack(
            rx.hstack(
                rx.icon("file", size=4, color=Colors.NEST_ACCENT),
                rx.vstack(
                    rx.heading(
                        file.get("filename", "Unknown"),
                        size="5",
                        font_family=Typography.DISPLAY,
                        font_weight=Typography.FONT_BOLD,
                        color=Colors.TEXT_PRIMARY,
                    ),
                    rx.text(
                        f"{format_file_size(file.get('file_size', 0))} • {format_date(file.get('created_at'))}",
                        font_size=Typography.TEXT_SM,
                        color=Colors.TEXT_TERTIARY,
                        font_family=Typography.MONO,
                    ),
                    spacing="1",
                    align_items="start",
                ),
                rx.hstack(
                    glass_button(
                        "Download",
                        variant="secondary",
                        size="sm",
                        on_click=on_download,
                    ),
                    glass_button(
                        "Delete",
                        variant="ghost",
                        size="sm",
                        on_click=on_delete,
                    ),
                    spacing="2",
                ),
                align_items="center",
                justify="space-between",
                width="100%",
            ),
            rx.box(height="4"),
            rx.text(
                f"Uploaded by: {file.get('uploader_name', 'Unknown')}",
                font_size=Typography.TEXT_SM,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
            ),
            spacing="3",
            align_items="stretch",
        ),
        padding="6",
    )


def message_card(message: dict, is_own: bool = False) -> rx.Component:
    """
    Enhanced message card with glassmorphism design.
    
    Args:
        message: The message data.
        is_own: Whether the message is from the current user.
        
    Returns:
        A glassmorphism message card component.
    """
    background = "rgba(99, 102, 241, 0.1)" if is_own else "rgba(255, 255, 255, 0.05)"
    border_color = "rgba(99, 102, 241, 0.3)" if is_own else "rgba(255, 255, 255, 0.1)"
    
    return rx.box(
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
                        font_size=Typography.TEXT_BASE,
                        font_weight=Typography.FONT_MEDIUM,
                        color=Colors.TEXT_PRIMARY,
                        font_family=Typography.SANS,
                    ),
                    rx.text(
                        format_time(message.get("created_at")),
                        font_size=Typography.TEXT_XS,
                        color=Colors.TEXT_TERTIARY,
                        font_family=Typography.MONO,
                    ),
                    spacing="1",
                    align_items="start",
                ),
                align_items="center",
                spacing="3",
            ),
            rx.text(
                message.get("body", ""),
                font_size=Typography.TEXT_BASE,
                color=Colors.TEXT_PRIMARY,
                font_family=Typography.SANS,
            ),
            spacing="3",
            align_items="start",
        ),
        padding="4",
        background=background,
        border=f"1px solid {border_color}",
        border_radius=BorderRadius.RADIUS_LG,
        backdrop_filter="blur(8px)",
        webkit_backdrop_filter="blur(8px)",
        align_self="start" if not is_own else "end",
        max_width="70%",
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "border_color": "rgba(99, 102, 241, 0.5)" if is_own else "rgba(255, 255, 255, 0.2)",
        },
    )


def task_card(task: dict, on_toggle: str, on_delete: str) -> rx.Component:
    """
    Enhanced task card with glassmorphism design.
    
    Args:
        task: The task data.
        on_toggle: The toggle handler.
        on_delete: The delete handler.
        
    Returns:
        A glassmorphism task card component.
    """
    return rx.box(
        rx.hstack(
            rx.checkbox(
                checked=task.get("is_done", False),
                on_change=on_toggle,
                color_scheme="indigo",
            ),
            rx.vstack(
                rx.text(
                    task.get("title", "Untitled"),
                    font_size=Typography.TEXT_BASE,
                    decoration="line-through" if task.get("is_done", False) else "none",
                    color=Colors.TEXT_MUTED if task.get("is_done", False) else Colors.TEXT_PRIMARY,
                    font_family=Typography.SANS,
                ),
                rx.text(
                    format_date(task.get("created_at")),
                    font_size=Typography.TEXT_XS,
                    color=Colors.TEXT_TERTIARY,
                    font_family=Typography.MONO,
                ),
                spacing="1",
                align_items="start",
            ),
            rx.box(flex="1"),
            glass_button(
                "",
                variant="ghost",
                size="sm",
                on_click=on_delete,
            ),
            align_items="center",
            spacing="3",
            width="100%",
        ),
        padding="3",
        background="rgba(255, 255, 255, 0.02)",
        border=f"1px solid {Colors.BORDER_DARK}",
        border_radius=BorderRadius.RADIUS_MD,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": Colors.BG_HOVER,
            "border_color": Colors.BORDER_MEDIUM,
        },
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


__all__ = [
    "project_card",
    "client_card",
    "invoice_card",
    "file_card",
    "message_card",
    "task_card",
]