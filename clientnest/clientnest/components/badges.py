"""Badge components for Clientnest."""
import reflex as rx


def status_badge(status: str) -> rx.Component:
    """Create a status badge component.
    
    Args:
        status: The status value.
        
    Returns:
        A badge component with appropriate styling.
    """
    status_colors = {
        "not_started": "gray",
        "in_progress": "blue",
        "review": "amber",
        "completed": "green",
        "on_hold": "red",
    }
    
    status_labels = {
        "not_started": "Not Started",
        "in_progress": "In Progress",
        "review": "In Review",
        "completed": "Completed",
        "on_hold": "On Hold",
    }
    
    color = status_colors.get(status, "gray")
    label = status_labels.get(status, status.title())
    
    return rx.badge(
        rx.text(label, size="1"),
        color_scheme=color,
        variant="soft",
        radius="full",
    )


def plan_badge(plan: str) -> rx.Component:
    """Create a plan badge component.
    
    Args:
        plan: The plan value.
        
    Returns:
        A badge component with appropriate styling.
    """
    plan_colors = {
        "free": "gray",
        "solo": "blue",
        "agency": "purple",
        "studio": "orange",
    }
    
    plan_labels = {
        "free": "Free",
        "solo": "Solo",
        "agency": "Agency",
        "studio": "Studio",
    }
    
    color = plan_colors.get(plan, "gray")
    label = plan_labels.get(plan, plan.title())
    
    return rx.badge(
        rx.text(label, size="1"),
        color_scheme=color,
        variant="soft",
        radius="full",
    )


def role_badge(role: str) -> rx.Component:
    """Create a role badge component.
    
    Args:
        role: The role value.
        
    Returns:
        A badge component with appropriate styling.
    """
    role_colors = {
        "owner": "green",
        "member": "blue",
        "client": "purple",
    }
    
    role_labels = {
        "owner": "Owner",
        "member": "Member",
        "client": "Client",
    }
    
    color = role_colors.get(role, "gray")
    label = role_labels.get(role, role.title())
    
    return rx.badge(
        rx.text(label, size="1"),
        color_scheme=color,
        variant="soft",
        radius="full",
    )


def invoice_status_badge(status: str) -> rx.Component:
    """Create an invoice status badge component.
    
    Args:
        status: The invoice status value.
        
    Returns:
        A badge component with appropriate styling.
    """
    status_colors = {
        "unpaid": "gray",
        "paid": "green",
        "overdue": "red",
        "cancelled": "orange",
    }
    
    status_labels = {
        "unpaid": "Unpaid",
        "paid": "Paid",
        "overdue": "Overdue",
        "cancelled": "Cancelled",
    }
    
    color = status_colors.get(status, "gray")
    label = status_labels.get(status, status.title())
    
    return rx.badge(
        rx.text(label, size="1"),
        color_scheme=color,
        variant="soft",
        radius="full",
    )


def subscription_status_badge(status: str) -> rx.Component:
    """Create a subscription status badge component.
    
    Args:
        status: The subscription status value.
        
    Returns:
        A badge component with appropriate styling.
    """
    status_colors = {
        "active": "green",
        "inactive": "gray",
        "cancelled": "red",
        "past_due": "orange",
    }
    
    status_labels = {
        "active": "Active",
        "inactive": "Inactive",
        "cancelled": "Cancelled",
        "past_due": "Past Due",
    }
    
    color = status_colors.get(status, "gray")
    label = status_labels.get(status, status.title())
    
    return rx.badge(
        rx.text(label, size="1"),
        color_scheme=color,
        variant="soft",
        radius="full",
    )


def notification_badge(count: int) -> rx.Component:
    """Create a notification badge component.
    
    Args:
        count: The notification count.
        
    Returns:
        A badge component showing the count.
    """
    if count == 0:
        return rx.fragment()
    
    return rx.badge(
        rx.text(str(count), size="1"),
        color_scheme="red",
        variant="solid",
        radius="full",
        class_name="notification-badge",
    )


def priority_badge(priority: str) -> rx.Component:
    """Create a priority badge component.
    
    Args:
        priority: The priority value.
        
    Returns:
        A badge component with appropriate styling.
    """
    priority_colors = {
        "low": "gray",
        "medium": "blue",
        "high": "orange",
        "urgent": "red",
    }
    
    priority_labels = {
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "urgent": "Urgent",
    }
    
    color = priority_colors.get(priority, "gray")
    label = priority_labels.get(priority, priority.title())
    
    return rx.badge(
        rx.text(label, size="1"),
        color_scheme=color,
        variant="soft",
        radius="full",
    )
