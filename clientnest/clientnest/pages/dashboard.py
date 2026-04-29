"""
Dashboard Page - Enhanced with Lusion.co Aesthetic
===================================================

Premium dashboard with glassmorphism, ambient effects, and smooth animations.
Features enhanced stats grid, activity sections, and modern UI components.
"""

import reflex as rx
from ..state.dashboard import DashboardState
from ..state.project import ProjectState
from ..components.glass import (
    glass_card,
    glass_button,
    glass_input,
    glass_textarea,
    glass_stat_card,
    glass_modal,
    glass_divider,
)
from ..components.interactive import (
    custom_cursor,
    ambient_background,
    interactive_wrapper,
)
from ..styles import (
    Colors,
    Typography,
    Spacing,
    BorderRadius,
    Shadows,
    Transitions,
)


def dashboard() -> rx.Component:
    """
    Enhanced dashboard with lusion.co-inspired design.
    
    Returns:
        Dashboard component with glassmorphism effects
    """
    return rx.box(
        # Custom cursor
        custom_cursor(),
        
        # Ambient background effects
        ambient_background(),
        
        # Main dashboard content
        rx.container(
            rx.vstack(
                # Header section
                dashboard_header(),
                
                # Stats grid
                stats_grid(),
                
                glass_divider(margin=f"{"8"} 0"),
                
                # Activity section
                activity_section(),
                
                # Quick actions
                quick_actions(),
                
                spacing="8",
                min_height="85vh",
                width="100%",
            ),
            max_width="1400px",
            padding_x="8",
            padding_y="8",
        ),
        
        # Create project modal
        create_project_modal(),
        
        # Custom styles
        style={
            "background_color": Colors.VOID,
            "color": Colors.TEXT_PRIMARY,
            "font_family": Typography.SANS,
            "min_height": "100vh",
        },
    )


def dashboard_header() -> rx.Component:
    """
    Dashboard header with title and actions.
    
    Returns:
        Header component
    """
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "Dashboard",
                size="8",
                font_family=Typography.DISPLAY,
                font_weight=Typography.FONT_BOLD,
                color=Colors.TEXT_PRIMARY,
                letter_spacing="-0.025em",
            ),
            rx.text(
                "Welcome back! Here's what's happening with your projects.",
                font_size=Typography.TEXT_BASE,
                color=Colors.TEXT_SECONDARY,
                font_family=Typography.SANS,
            ),
            spacing="2",
            align="start",
        ),
        rx.hstack(
            glass_button(
                "View All Projects",
                variant="secondary",
                on_click=lambda: rx.redirect("/projects"),
            ),
            glass_button(
                "Create Project",
                variant="primary",
                on_click=ProjectState.toggle_create_form,
            ),
            spacing="4",
        ),
        justify="between",
        align="center",
        width="100%",
    )


def stats_grid() -> rx.Component:
    """
    Enhanced statistics grid with glassmorphism cards.
    
    Returns:
        Stats grid component
    """
    return rx.grid(
        # Projects stat
        glass_stat_card(
            "Total Projects",
            ProjectState.projects.length(),
            "folder",
        ),

        # Active projects stat
        glass_stat_card(
            "Active Projects",
            ProjectState.active_count,
            "zap",
        ),

        # Clients stat
        glass_stat_card(
            "Total Clients",
            "0",  # Will be updated from state
            "users",
        ),

        # Invoices stat
        glass_stat_card(
            "Pending Invoices",
            "0",  # Will be updated from state
            "dollar-sign",
        ),
        
        template_columns="repeat(auto-fit, minmax(250px, 1fr))",
        gap="6",
        width="100%",
    )


def activity_section() -> rx.Component:
    """
    Activity section with recent projects and updates.
    
    Returns:
        Activity section component
    """
    return rx.hstack(
        # Recent projects
        glass_card(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Recent Projects",
                        size="5",
                        font_family=Typography.DISPLAY,
                        font_weight=Typography.FONT_BOLD,
                        color=Colors.TEXT_PRIMARY,
                    ),
                    glass_button(
                        "View All",
                        variant="ghost",
                        size="sm",
                        on_click=lambda: rx.redirect("/projects"),
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                
                rx.cond(
                    ProjectState.projects.length() > 0,
                    rx.vstack(
                        rx.foreach(
                            ProjectState.projects[:5],
                            project_list_item,
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    rx.box(
                        rx.text(
                            "No projects yet. Create your first project!",
                            color=Colors.TEXT_TERTIARY,
                            font_size=Typography.TEXT_SM,
                            text_align="center",
                            padding="8",
                        ),
                        width="100%",
                    ),
                ),
                
                spacing="6",
                width="100%",
            ),
            flex="2",
        ),
        
        # Quick stats and updates
        glass_card(
            rx.vstack(
                rx.heading(
                    "Quick Updates",
                    size="5",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                    margin_bottom="6",
                ),
                
                # Update items
                rx.vstack(
                    update_item(
                        "System Update",
                        "New features available",
                        "2 hours ago",
                        "info",
                    ),
                    update_item(
                        "Invoice Reminder",
                        "3 invoices due this week",
                        "1 day ago",
                        "warning",
                    ),
                    update_item(
                        "Project Completed",
                        "Website redesign finished",
                        "2 days ago",
                        "success",
                    ),
                    spacing="4",
                    width="100%",
                ),
                
                spacing="6",
                width="100%",
            ),
            flex="1",
        ),
        
        gap="6",
        width="100%",
    )


def project_list_item(project: dict) -> rx.Component:
    """
    Individual project list item.
    
    Args:
        project: Project data dictionary
    
    Returns:
        Project list item component
    """
    return rx.hstack(
        rx.box(
            rx.box(
                rx.text(
                    "📁",
                    font_size=Typography.TEXT_SM,
                ),
                width="40px",
                height="40px",
                background=f"rgba(99, 102, 241, 0.2)",
                border_radius=BorderRadius.RADIUS_LG,
                display="flex",
                align_items="center",
                justify_content="center",
            ),
        ),
        
        rx.vstack(
            rx.text(
                project.get("title", "Untitled Project"),
                font_size=Typography.TEXT_BASE,
                font_weight=Typography.FONT_MEDIUM,
                color=Colors.TEXT_PRIMARY,
                font_family=Typography.SANS,
            ),
            rx.text(
                rx.cond(
                    project.get("description") != "",
                    project.get("description", "No description"),
                    "No description"
                ),
                font_size=Typography.TEXT_SM,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
            ),
            spacing="1",
            align="start",
        ),
        
        rx.box(
            rx.badge(
                rx.cond(
                    project.get("status") == "not_started",
                    "Not Started",
                    rx.cond(
                        project.get("status") == "in_progress",
                        "In Progress",
                        rx.cond(
                            project.get("status") == "review",
                            "In Review",
                            rx.cond(
                                project.get("status") == "completed",
                                "Completed",
                                rx.cond(
                                    project.get("status") == "on_hold",
                                    "On Hold",
                                    "Unknown"
                                )
                            )
                        )
                    )
                ),
                background=f"rgba(99, 102, 241, 0.1)",
                color=Colors.NEST_ACCENT,
                padding=f"{"1"} {"3"}",
                border_radius=BorderRadius.RADIUS_FULL,
                font_size=Typography.TEXT_XS,
                font_family=Typography.MONO,
                font_weight=Typography.FONT_MEDIUM,
            ),
        ),
        
        justify="between",
        align="center",
        width="100%",
        padding="4",
        background=f"rgba(255, 255, 255, 0.02)",
        border_radius=BorderRadius.RADIUS_LG,
        border=f"1px solid {Colors.BORDER_DARK}",
        transition=Transitions.TRANSITION_FAST,
        _hover={
            "background": Colors.BG_HOVER,
            "border_color": Colors.BORDER_MEDIUM,
            "transform": "translateX(4px)",
        },
        cursor="pointer",
        on_click=lambda: rx.redirect(f"/projects/{project.get('id')}"),
    )


def update_item(
    title: str,
    description: str,
    time: str,
    variant: str = "info"
) -> rx.Component:
    """
    Individual update item.
    
    Args:
        title: Update title
        description: Update description
        time: Time ago
        variant: Update variant (info, warning, success)
    
    Returns:
        Update item component
    """
    variant_colors = {
        "info": Colors.NEST_ACCENT,
        "warning": Colors.WARNING,
        "success": Colors.SUCCESS,
    }
    
    color = variant_colors.get(variant, Colors.NEST_ACCENT)
    
    return rx.hstack(
        rx.box(
            width="8px",
            height="8px",
            background=color,
            border_radius=BorderRadius.RADIUS_FULL,
            box_shadow=f"0 0 10px {color}40",
        ),
        rx.vstack(
            rx.text(
                title,
                font_size=Typography.TEXT_SM,
                font_weight=Typography.FONT_MEDIUM,
                color=Colors.TEXT_PRIMARY,
                font_family=Typography.SANS,
            ),
            rx.text(
                description,
                font_size=Typography.TEXT_XS,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
            ),
            spacing="1",
            align="start",
        ),
        rx.text(
            time,
            font_size=Typography.TEXT_XS,
            color=Colors.TEXT_MUTED,
            font_family=Typography.MONO,
        ),
        justify="between",
        align="center",
        width="100%",
        padding="3",
        background=f"rgba(255, 255, 255, 0.02)",
        border_radius=BorderRadius.RADIUS_LG,
    )


def quick_actions() -> rx.Component:
    """
    Quick actions section with common tasks.
    
    Returns:
        Quick actions component
    """
    return rx.grid(
        quick_action_card(
            "Create Project",
            "Start a new project",
            "plus",
            lambda: ProjectState.toggle_create_form(),
        ),
        quick_action_card(
            "Invite Client",
            "Add a new client",
            "user-plus",
            lambda: rx.redirect("/clients/invite"),
        ),
        quick_action_card(
            "Create Invoice",
            "Send an invoice",
            "file-text",
            lambda: rx.redirect("/invoices/new"),
        ),
        quick_action_card(
            "View Reports",
            "See analytics",
            "bar-chart",
            lambda: rx.redirect("/dashboard"),
        ),
        template_columns="repeat(auto-fit, minmax(200px, 1fr))",
        gap="4",
        width="100%",
    )


def quick_action_card(
    title: str,
    description: str,
    icon: str,
    on_click: callable,
) -> rx.Component:
    """
    Individual quick action card.
    
    Args:
        title: Action title
        description: Action description
        icon: Icon name
        on_click: Click handler
    
    Returns:
        Quick action card component
    """
    return glass_card(
        rx.vstack(
            rx.icon(
                icon,
                size=24,
                color=Colors.NEST_ACCENT,
            ),
            rx.text(
                title,
                font_size=Typography.TEXT_BASE,
                font_weight=Typography.FONT_MEDIUM,
                color=Colors.TEXT_PRIMARY,
                font_family=Typography.SANS,
            ),
            rx.text(
                description,
                font_size=Typography.TEXT_SM,
                color=Colors.TEXT_TERTIARY,
                font_family=Typography.SANS,
            ),
            spacing="3",
            align="start",
        ),
        padding="6",
        cursor="pointer",
        on_click=on_click,
    )


def create_project_modal() -> rx.Component:
    """
    Create project modal with glassmorphism design.
    
    Returns:
        Create project modal component
    """
    return glass_modal(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    "Create New Project",
                    size="6",
                    font_family=Typography.DISPLAY,
                    font_weight=Typography.FONT_BOLD,
                    color=Colors.TEXT_PRIMARY,
                ),
                rx.button(
                    rx.icon("x", size=20),
                    on_click=ProjectState.toggle_create_form,
                    background="transparent",
                    border="none",
                    color=Colors.TEXT_SECONDARY,
                    cursor="pointer",
                    _hover={
                        "color": Colors.TEXT_PRIMARY,
                    },
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            
            glass_divider(margin=f"{"4"} 0"),
            
            rx.form(
                rx.vstack(
                    rx.vstack(
                        rx.text(
                            "Project Title",
                            font_size=Typography.TEXT_SM,
                            font_weight=Typography.FONT_MEDIUM,
                            color=Colors.TEXT_SECONDARY,
                            margin_bottom="2",
                        ),
                        glass_input(
                            placeholder="Enter project title",
                            name="title",
                            required=True,
                            value=ProjectState.project_title,
                            on_change=ProjectState.set_project_title,
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    rx.vstack(
                        rx.text(
                            "Description",
                            font_size=Typography.TEXT_SM,
                            font_weight=Typography.FONT_MEDIUM,
                            color=Colors.TEXT_SECONDARY,
                            margin_bottom="2",
                        ),
                        glass_textarea(
                            placeholder="Project description (optional)",
                            name="description",
                            value=ProjectState.project_description,
                            on_change=ProjectState.set_project_description,
                            rows=3,
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    rx.vstack(
                        rx.text(
                            "Due Date",
                            font_size=Typography.TEXT_SM,
                            font_weight=Typography.FONT_MEDIUM,
                            color=Colors.TEXT_SECONDARY,
                            margin_bottom="2",
                        ),
                        glass_input(
                            placeholder="Select due date",
                            type="date",
                            name="due_date",
                            value=ProjectState.project_due_date,
                            on_change=ProjectState.set_project_due_date,
                        ),
                        spacing="2",
                        align="start",
                        width="100%",
                    ),
                    
                    glass_divider(margin=f"{"6"} 0"),
                    
                    rx.hstack(
                        glass_button(
                            "Cancel",
                            variant="ghost",
                            on_click=ProjectState.toggle_create_form,
                        ),
                        glass_button(
                            "Create Project",
                            variant="primary",
                            type="submit",
                        ),
                        spacing="4",
                        justify="end",
                        width="100%",
                    ),
                    
                    spacing="6",
                    width="100%",
                ),
                on_submit=ProjectState.create_project,
                reset_on_submit=True,
            ),
            
            spacing="6",
            width="100%",
        ),
        is_open=ProjectState.show_create_form,
        on_close=ProjectState.toggle_create_form,
    )


# Tracking class for letter spacing
class Tracking:
    TIGHT = "-0.025em"
    NORMAL = "0"
    WIDE = "0.025em"