"""
Clientnest Components
====================

Reusable UI components for the Clientnest application.
Includes glassmorphism components, cards, badges, navigation, tables, and interactive elements.
"""

from .glass import (
    glass_panel,
    glass_card,
    glass_button,
    glass_input,
    glass_textarea,
    glass_badge,
    glass_divider,
    glass_stat_card,
    glass_modal,
)

from .interactive import (
    custom_cursor,
    ambient_background,
    interactive_wrapper,
)

from .badges import (
    status_badge,
    plan_badge,
    role_badge,
    invoice_status_badge,
    subscription_status_badge,
    notification_badge,
    priority_badge,
)

from .cards import (
    project_card,
    client_card,
    invoice_card,
    file_card,
    message_card,
    task_card,
)

from .navbar import (
    navbar,
    sidebar,
    mobile_navbar,
    nav_link,
    sidebar_link,
    user_menu,
    breadcrumb,
    search_bar,
    notification_dropdown,
)

from .table import (
    data_table,
    project_table,
    client_table,
    invoice_table,
    empty_table,
    loading_table,
)

__all__ = [
    # Glass components
    "glass_panel",
    "glass_card",
    "glass_button",
    "glass_input",
    "glass_textarea",
    "glass_badge",
    "glass_divider",
    "glass_stat_card",
    "glass_modal",
    # Interactive components
    "custom_cursor",
    "ambient_background",
    "interactive_wrapper",
    # Badges
    "status_badge",
    "plan_badge",
    "role_badge",
    "invoice_status_badge",
    "subscription_status_badge",
    "notification_badge",
    "priority_badge",
    # Cards
    "project_card",
    "client_card",
    "invoice_card",
    "file_card",
    "message_card",
    "task_card",
    # Navigation
    "navbar",
    "sidebar",
    "mobile_navbar",
    "nav_link",
    "sidebar_link",
    "user_menu",
    "breadcrumb",
    "search_bar",
    "notification_dropdown",
    # Tables
    "data_table",
    "project_table",
    "client_table",
    "invoice_table",
    "empty_table",
    "loading_table",
]