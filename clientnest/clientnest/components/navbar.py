"""
Enhanced Navigation Components - Glassmorphism Design
====================================================

Premium navigation components with glassmorphism effects for the Clientnest dashboard.
All navigation elements use the new lusion.co-inspired design system with blur effects.
"""

import reflex as rx
from .glass import glass_button
from ..styles import (
    Colors,
    Typography,
    Spacing,
    BorderRadius,
    Shadows,
    Transitions,
)


def navbar() -> rx.Component:
    """
    Enhanced main navigation bar with glassmorphism design.
    
    Returns:
        A glassmorphism navigation bar component.
    """
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.box(
                    rx.text(
                        "C",
                        font_size=Typography.TEXT_XL,
                        font_weight=Typography.FONT_BOLD,
                        color=Colors.TEXT_PRIMARY,
                    ),
                    width="32px",
                    height="32px",
                    border=f"1px solid {Colors.BORDER_MEDIUM}",
                    border_radius=BorderRadius.RADIUS_FULL,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.heading(
                    "Clientnest",
                    size="6",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                    letter_spacing="-0.025em",
                ),
                align_items="center",
                spacing="3",
            ),
            rx.box(flex="1"),
            # Navigation items
            rx.hstack(
                nav_link("Dashboard", "/dashboard"),
                nav_link("Projects", "/projects"),
                nav_link("Clients", "/clients"),
                nav_link("Invoices", "/invoices"),
                nav_link("Settings", "/settings"),
                spacing="6",
            ),
            # User menu
            user_menu(),
            align_items="center",
            spacing="6",
        ),
        padding="6",
        background=Colors.NEST_SURFACE,
        backdrop_filter="blur(24px)",
        webkit_backdrop_filter="blur(24px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_bottom=f"1px solid {Colors.BORDER_DARK}",
        position="sticky",
        top="0",
        z_index="1000",
    )


def sidebar() -> rx.Component:
    """
    Enhanced sidebar navigation with glassmorphism design.
    
    Returns:
        A glassmorphism sidebar component.
    """
    return rx.box(
        rx.vstack(
            # Logo
            rx.hstack(
                rx.box(
                    rx.text(
                        "C",
                        font_size=Typography.TEXT_LG,
                        font_weight=Typography.FONT_BOLD,
                        color=Colors.TEXT_PRIMARY,
                    ),
                    width="28px",
                    height="28px",
                    border=f"1px solid {Colors.BORDER_MEDIUM}",
                    border_radius=BorderRadius.RADIUS_FULL,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.heading(
                    "Clientnest",
                    size="5",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                    letter_spacing="-0.025em",
                ),
                align_items="center",
                spacing="3",
            ),
            rx.box(
                height="1px",
                width="100%",
                background=f"linear-gradient(90deg, transparent, {Colors.BORDER_MEDIUM}, transparent)",
            ),
            # Navigation items
            rx.vstack(
                sidebar_link("Dashboard", "/dashboard", "layout-dashboard"),
                sidebar_link("Projects", "/projects", "folder"),
                sidebar_link("Clients", "/clients", "users"),
                sidebar_link("Invoices", "/invoices", "file-text"),
                sidebar_link("Settings", "/settings", "settings"),
                spacing="2",
                align_items="stretch",
                width="100%",
            ),
            rx.box(flex="1"),
            # User info
            rx.box(
                rx.hstack(
                    rx.avatar(size="sm"),
                    rx.vstack(
                        rx.text(
                            "User Name",
                            font_size=Typography.TEXT_SM,
                            font_weight=Typography.FONT_MEDIUM,
                            color=Colors.TEXT_PRIMARY,
                            font_family=Typography.SANS,
                        ),
                        rx.text(
                            "user@example.com",
                            font_size=Typography.TEXT_XS,
                            color=Colors.TEXT_TERTIARY,
                            font_family=Typography.SANS,
                        ),
                        spacing="1",
                        align_items="start",
                    ),
                    align_items="center",
                    spacing="3",
                ),
                padding="3",
                background="rgba(255, 255, 255, 0.02)",
                border=f"1px solid {Colors.BORDER_DARK}",
                border_radius=BorderRadius.RADIUS_LG,
            ),
            spacing="6",
            align_items="stretch",
            width="100%",
        ),
        width="250px",
        height="100vh",
        background=Colors.NEST_SURFACE,
        backdrop_filter="blur(24px)",
        webkit_backdrop_filter="blur(24px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_right=f"1px solid {Colors.BORDER_DARK}",
        position="fixed",
        left="0",
        top="0",
        padding="6",
        display=["none", "none", "flex"],
        z_index="999",
    )


def mobile_navbar() -> rx.Component:
    """
    Enhanced mobile navigation bar with glassmorphism design.
    
    Returns:
        A glassmorphism mobile navigation bar component.
    """
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.box(
                    rx.text(
                        "C",
                        font_size=Typography.TEXT_LG,
                        font_weight=Typography.FONT_BOLD,
                        color=Colors.TEXT_PRIMARY,
                    ),
                    width="28px",
                    height="28px",
                    border=f"1px solid {Colors.BORDER_MEDIUM}",
                    border_radius=BorderRadius.RADIUS_FULL,
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.heading(
                    "Clientnest",
                    size="5",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                    letter_spacing="-0.025em",
                ),
                align_items="center",
                spacing="3",
            ),
            rx.box(flex="1"),
            # Mobile menu button
            glass_button(
                "",
                variant="ghost",
                size="sm",
                on_click=lambda: rx.toggle_sidebar(),
            ),
            align_items="center",
            spacing="4",
        ),
        padding="4",
        background=Colors.NEST_SURFACE,
        backdrop_filter="blur(24px)",
        webkit_backdrop_filter="blur(24px)",
        border=f"1px solid {Colors.BORDER_LIGHT}",
        border_bottom=f"1px solid {Colors.BORDER_DARK}",
        display=["flex", "flex", "none"],
        position="sticky",
        top="0",
        z_index="1000",
    )


def nav_link(text: str, href: str) -> rx.Component:
    """
    Enhanced navigation link with glassmorphism design.
    
    Args:
        text: The link text.
        href: The link href.
        
    Returns:
        A glassmorphism navigation link component.
    """
    return rx.link(
        text,
        href=href,
        font_size=Typography.TEXT_SM,
        font_weight=Typography.FONT_MEDIUM,
        color=Colors.TEXT_SECONDARY,
        font_family=Typography.SANS,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "color": Colors.TEXT_PRIMARY,
        },
    )


def sidebar_link(text: str, href: str, icon: str) -> rx.Component:
    """
    Enhanced sidebar link with glassmorphism design.
    
    Args:
        text: The link text.
        href: The link href.
        icon: The icon name.
        
    Returns:
        A glassmorphism sidebar link component.
    """
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=4, color=Colors.TEXT_SECONDARY),
            rx.text(
                text,
                font_size=Typography.TEXT_BASE,
                font_weight=Typography.FONT_MEDIUM,
                color=Colors.TEXT_SECONDARY,
                font_family=Typography.SANS,
            ),
            align_items="center",
            spacing="3",
        ),
        href=href,
        padding="3",
        border_radius=BorderRadius.RADIUS_LG,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": Colors.BG_HOVER,
            "color": Colors.TEXT_PRIMARY,
        },
        width="100%",
    )


def user_menu() -> rx.Component:
    """
    Enhanced user menu with glassmorphism design.
    
    Returns:
        A glassmorphism user menu component.
    """
    return rx.menu.root(
        rx.menu.trigger(
            rx.hstack(
                rx.avatar(size="sm"),
                rx.icon("chevron-down", size=3, color=Colors.TEXT_SECONDARY),
                align_items="center",
                spacing="2",
                cursor="pointer",
            ),
        ),
        rx.menu.content(
            rx.menu.item("Profile"),
            rx.menu.item("Billing"),
            rx.menu.item("Settings"),
            rx.menu.separator(),
            rx.menu.item("Logout", color="red"),
        ),
    )


def breadcrumb(items: list[tuple[str, str]]) -> rx.Component:
    """
    Enhanced breadcrumb with glassmorphism design.
    
    Args:
        items: A list of (text, href) tuples.
        
    Returns:
        A glassmorphism breadcrumb component.
    """
    return rx.hstack(
        *[
            rx.fragment(
                rx.link(
                    text,
                    href=href,
                    font_size=Typography.TEXT_SM,
                    color=Colors.TEXT_SECONDARY,
                    font_family=Typography.SANS,
                    transition=Transitions.TRANSITION_FAST,
                    _hover={
                        "color": Colors.TEXT_PRIMARY,
                    },
                ),
                rx.icon(
                    "chevron-right",
                    size=3,
                    color=Colors.TEXT_TERTIARY,
                ) if i < len(items) - 1 else None,
            )
            for i, (text, href) in enumerate(items)
        ],
        spacing="2",
        align_items="center",
        padding="3",
    )


def search_bar(placeholder: str = "Search...") -> rx.Component:
    """
    Enhanced search bar with glassmorphism design.
    
    Args:
        placeholder: The placeholder text.
        
    Returns:
        A glassmorphism search bar component.
    """
    return rx.hstack(
        rx.icon("search", size=4, color=Colors.TEXT_TERTIARY),
        rx.input(
            placeholder=placeholder,
            background="transparent",
            border="none",
            color=Colors.TEXT_PRIMARY,
            font_family=Typography.SANS,
            font_size=Typography.TEXT_BASE,
            width="100%",
            _focus={
                "outline": "none",
            },
            _placeholder={
                "color": Colors.TEXT_TERTIARY,
            },
        ),
        align_items="center",
        spacing="3",
        padding="3",
        background="rgba(255, 255, 255, 0.02)",
        border=f"1px solid {Colors.BORDER_DARK}",
        border_radius=BorderRadius.RADIUS_LG,
        transition=Transitions.TRANSITION_FAST,
        _focus={
            "border_color": Colors.NEST_ACCENT,
            "box_shadow": Shadows.GLOW_ACCENT,
        },
    )


def notification_dropdown() -> rx.Component:
    """
    Enhanced notification dropdown with glassmorphism design.
    
    Returns:
        A glassmorphism notification dropdown component.
    """
    return rx.dropdown.root(
        rx.dropdown.trigger(
            rx.button(
                rx.icon("bell", size=4),
                rx.badge(
                    rx.text("3", size="1"),
                    color_scheme="red",
                    variant="solid",
                    radius="full",
                    position="absolute",
                    top="-1",
                    right="-1",
                ),
                variant="ghost",
                position="relative",
            ),
        ),
        rx.dropdown.content(
            rx.heading("Notifications", size="4"),
            rx.box(
                height="1px",
                width="100%",
                background=f"linear-gradient(90deg, transparent, {Colors.BORDER_MEDIUM}, transparent)",
                margin=f"{"4"} 0",
            ),
            rx.vstack(
                rx.text("New project assigned", size="2"),
                rx.text("Invoice overdue", size="2"),
                rx.text("Client message received", size="2"),
                spacing="3",
            ),
            width="300",
        ),
    )


__all__ = [
    "navbar",
    "sidebar",
    "mobile_navbar",
    "nav_link",
    "sidebar_link",
    "user_menu",
    "breadcrumb",
    "search_bar",
    "notification_dropdown",
]