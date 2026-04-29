"""
Enhanced Badge Components - Glassmorphism Design
=================================================

Premium badge components with glassmorphism effects for the Clientnest dashboard.
All badges use the new lusion.co-inspired design system with blur effects and smooth animations.
"""

import reflex as rx
from ..styles import (
    Colors,
    Typography,
    Spacing,
    BorderRadius,
    Transitions,
)


def status_badge(status: str) -> rx.Component:
    """
    Enhanced status badge with glassmorphism design.
    
    Args:
        status: The status value.
        
    Returns:
        A glassmorphism status badge component.
    """
    status_colors = {
        "not_started": {
            "background": "rgba(148, 163, 184, 0.1)",
            "color": Colors.TEXT_TERTIARY,
            "border": "rgba(148, 163, 184, 0.2)",
        },
        "in_progress": {
            "background": "rgba(99, 102, 241, 0.1)",
            "color": Colors.NEST_ACCENT,
            "border": "rgba(99, 102, 241, 0.2)",
        },
        "review": {
            "background": "rgba(245, 158, 11, 0.1)",
            "color": Colors.WARNING,
            "border": "rgba(245, 158, 11, 0.2)",
        },
        "completed": {
            "background": "rgba(16, 185, 129, 0.1)",
            "color": Colors.SUCCESS,
            "border": "rgba(16, 185, 129, 0.2)",
        },
        "on_hold": {
            "background": "rgba(239, 68, 68, 0.1)",
            "color": Colors.ERROR,
            "border": "rgba(239, 68, 68, 0.2)",
        },
    }
    
    status_labels = {
        "not_started": "Not Started",
        "in_progress": "In Progress",
        "review": "In Review",
        "completed": "Completed",
        "on_hold": "On Hold",
    }
    
    color_config = status_colors.get(status, status_colors["not_started"])
    label = status_labels.get(status, status.title())
    
    return rx.badge(
        rx.text(
            label,
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_MEDIUM,
            font_family=Typography.MONO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        padding=f"{"1"} {"3"}",
        background=color_config["background"],
        color=color_config["color"],
        border=f"1px solid {color_config['border']}",
        border_radius=BorderRadius.RADIUS_FULL,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": color_config["background"].replace("0.1", "0.15"),
        },
    )


def plan_badge(plan: str) -> rx.Component:
    """
    Enhanced plan badge with glassmorphism design.
    
    Args:
        plan: The plan value.
        
    Returns:
        A glassmorphism plan badge component.
    """
    plan_colors = {
        "free": {
            "background": "rgba(148, 163, 184, 0.1)",
            "color": Colors.TEXT_TERTIARY,
            "border": "rgba(148, 163, 184, 0.2)",
        },
        "solo": {
            "background": "rgba(99, 102, 241, 0.1)",
            "color": Colors.NEST_ACCENT,
            "border": "rgba(99, 102, 241, 0.2)",
        },
        "agency": {
            "background": "rgba(139, 92, 246, 0.1)",
            "color": Colors.NEST_GLOW,
            "border": "rgba(139, 92, 246, 0.2)",
        },
        "studio": {
            "background": "rgba(249, 115, 22, 0.1)",
            "color": "#f97316",
            "border": "rgba(249, 115, 22, 0.2)",
        },
    }
    
    plan_labels = {
        "free": "Free",
        "solo": "Solo",
        "agency": "Agency",
        "studio": "Studio",
    }
    
    color_config = plan_colors.get(plan, plan_colors["free"])
    label = plan_labels.get(plan, plan.title())
    
    return rx.badge(
        rx.text(
            label,
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_MEDIUM,
            font_family=Typography.MONO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        padding=f"{"1"} {"3"}",
        background=color_config["background"],
        color=color_config["color"],
        border=f"1px solid {color_config['border']}",
        border_radius=BorderRadius.RADIUS_FULL,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": color_config["background"].replace("0.1", "0.15"),
        },
    )


def role_badge(role: str) -> rx.Component:
    """
    Enhanced role badge with glassmorphism design.
    
    Args:
        role: The role value.
        
    Returns:
        A glassmorphism role badge component.
    """
    role_colors = {
        "owner": {
            "background": "rgba(16, 185, 129, 0.1)",
            "color": Colors.SUCCESS,
            "border": "rgba(16, 185, 129, 0.2)",
        },
        "member": {
            "background": "rgba(99, 102, 241, 0.1)",
            "color": Colors.NEST_ACCENT,
            "border": "rgba(99, 102, 241, 0.2)",
        },
        "client": {
            "background": "rgba(139, 92, 246, 0.1)",
            "color": Colors.NEST_GLOW,
            "border": "rgba(139, 92, 246, 0.2)",
        },
    }
    
    role_labels = {
        "owner": "Owner",
        "member": "Member",
        "client": "Client",
    }
    
    color_config = role_colors.get(role, role_colors["client"])
    label = role_labels.get(role, role.title())
    
    return rx.badge(
        rx.text(
            label,
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_MEDIUM,
            font_family=Typography.MONO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        padding=f"{"1"} {"3"}",
        background=color_config["background"],
        color=color_config["color"],
        border=f"1px solid {color_config['border']}",
        border_radius=BorderRadius.RADIUS_FULL,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": color_config["background"].replace("0.1", "0.15"),
        },
    )


def invoice_status_badge(status: str) -> rx.Component:
    """
    Enhanced invoice status badge with glassmorphism design.
    
    Args:
        status: The invoice status value.
        
    Returns:
        A glassmorphism invoice status badge component.
    """
    status_colors = {
        "unpaid": {
            "background": "rgba(148, 163, 184, 0.1)",
            "color": Colors.TEXT_TERTIARY,
            "border": "rgba(148, 163, 184, 0.2)",
        },
        "paid": {
            "background": "rgba(16, 185, 129, 0.1)",
            "color": Colors.SUCCESS,
            "border": "rgba(16, 185, 129, 0.2)",
        },
        "overdue": {
            "background": "rgba(239, 68, 68, 0.1)",
            "color": Colors.ERROR,
            "border": "rgba(239, 68, 68, 0.2)",
        },
        "cancelled": {
            "background": "rgba(249, 115, 22, 0.1)",
            "color": "#f97316",
            "border": "rgba(249, 115, 22, 0.2)",
        },
    }
    
    status_labels = {
        "unpaid": "Unpaid",
        "paid": "Paid",
        "overdue": "Overdue",
        "cancelled": "Cancelled",
    }
    
    color_config = status_colors.get(status, status_colors["unpaid"])
    label = status_labels.get(status, status.title())
    
    return rx.badge(
        rx.text(
            label,
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_MEDIUM,
            font_family=Typography.MONO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        padding=f"{"1"} {"3"}",
        background=color_config["background"],
        color=color_config["color"],
        border=f"1px solid {color_config['border']}",
        border_radius=BorderRadius.RADIUS_FULL,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": color_config["background"].replace("0.1", "0.15"),
        },
    )


def subscription_status_badge(status: str) -> rx.Component:
    """
    Enhanced subscription status badge with glassmorphism design.
    
    Args:
        status: The subscription status value.
        
    Returns:
        A glassmorphism subscription status badge component.
    """
    status_colors = {
        "active": {
            "background": "rgba(16, 185, 129, 0.1)",
            "color": Colors.SUCCESS,
            "border": "rgba(16, 185, 129, 0.2)",
        },
        "inactive": {
            "background": "rgba(148, 163, 184, 0.1)",
            "color": Colors.TEXT_TERTIARY,
            "border": "rgba(148, 163, 184, 0.2)",
        },
        "cancelled": {
            "background": "rgba(239, 68, 68, 0.1)",
            "color": Colors.ERROR,
            "border": "rgba(239, 68, 68, 0.2)",
        },
        "past_due": {
            "background": "rgba(249, 115, 22, 0.1)",
            "color": "#f97316",
            "border": "rgba(249, 115, 22, 0.2)",
        },
    }
    
    status_labels = {
        "active": "Active",
        "inactive": "Inactive",
        "cancelled": "Cancelled",
        "past_due": "Past Due",
    }
    
    color_config = status_colors.get(status, status_colors["inactive"])
    label = status_labels.get(status, status.title())
    
    return rx.badge(
        rx.text(
            label,
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_MEDIUM,
            font_family=Typography.MONO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        padding=f"{"1"} {"3"}",
        background=color_config["background"],
        color=color_config["color"],
        border=f"1px solid {color_config['border']}",
        border_radius=BorderRadius.RADIUS_FULL,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": color_config["background"].replace("0.1", "0.15"),
        },
    )


def notification_badge(count: int) -> rx.Component:
    """
    Enhanced notification badge with glassmorphism design.
    
    Args:
        count: The notification count.
        
    Returns:
        A glassmorphism notification badge component.
    """
    if count == 0:
        return rx.fragment()
    
    return rx.badge(
        rx.text(
            str(count),
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_BOLD,
            font_family=Typography.MONO,
        ),
        padding=f"{"1"} {"2"}",
        background=Colors.ERROR,
        color=Colors.TEXT_PRIMARY,
        border_radius=BorderRadius.RADIUS_FULL,
        box_shadow=Shadows.GLOW_ERROR,
    )


def priority_badge(priority: str) -> rx.Component:
    """
    Enhanced priority badge with glassmorphism design.
    
    Args:
        priority: The priority value.
        
    Returns:
        A glassmorphism priority badge component.
    """
    priority_colors = {
        "low": {
            "background": "rgba(148, 163, 184, 0.1)",
            "color": Colors.TEXT_TERTIARY,
            "border": "rgba(148, 163, 184, 0.2)",
        },
        "medium": {
            "background": "rgba(99, 102, 241, 0.1)",
            "color": Colors.NEST_ACCENT,
            "border": "rgba(99, 102, 241, 0.2)",
        },
        "high": {
            "background": "rgba(249, 115, 22, 0.1)",
            "color": "#f97316",
            "border": "rgba(249, 115, 22, 0.2)",
        },
        "urgent": {
            "background": "rgba(239, 68, 68, 0.1)",
            "color": Colors.ERROR,
            "border": "rgba(239, 68, 68, 0.2)",
        },
    }
    
    priority_labels = {
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "urgent": "Urgent",
    }
    
    color_config = priority_colors.get(priority, priority_colors["low"])
    label = priority_labels.get(priority, priority.title())
    
    return rx.badge(
        rx.text(
            label,
            font_size=Typography.TEXT_XS,
            font_weight=Typography.FONT_MEDIUM,
            font_family=Typography.MONO,
            text_transform="uppercase",
            letter_spacing="0.05em",
        ),
        padding=f"{"1"} {"3"}",
        background=color_config["background"],
        color=color_config["color"],
        border=f"1px solid {color_config['border']}",
        border_radius=BorderRadius.RADIUS_FULL,
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": color_config["background"].replace("0.1", "0.15"),
        },
    )


__all__ = [
    "status_badge",
    "plan_badge",
    "role_badge",
    "invoice_status_badge",
    "subscription_status_badge",
    "notification_badge",
    "priority_badge",
]