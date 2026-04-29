"""Navigation bar components for Clientnest."""
import reflex as rx


def navbar() -> rx.Component:
    """Create the main navigation bar component.
    
    Returns:
        A navigation bar component.
    """
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.icon("briefcase", size=6),
                rx.heading("Clientnest", size="6"),
                align_items="center",
                spacing="2",
            ),
            rx.spacer(),
            # Navigation items
            rx.hstack(
                nav_link("Dashboard", "/dashboard"),
                nav_link("Projects", "/projects"),
                nav_link("Clients", "/clients"),
                nav_link("Invoices", "/invoices"),
                nav_link("Settings", "/settings"),
                spacing="4",
            ),
            # User menu
            rx.menu.root(
                rx.menu.trigger(
                    rx.avatar(
                        size="sm",
                        cursor="pointer",
                    ),
                ),
                rx.menu.content(
                    rx.menu.item("Profile"),
                    rx.menu.item("Billing"),
                    rx.menu.separator(),
                    rx.menu.item("Logout", color="red"),
                ),
            ),
            align_items="center",
            spacing="6",
        ),
        padding="4",
        background="white",
        border_bottom="1px solid #e2e8f0",
        position="sticky",
        top="0",
        z_index="10",
    )


def sidebar() -> rx.Component:
    """Create the sidebar navigation component.
    
    Returns:
        A sidebar component.
    """
    return rx.box(
        rx.vstack(
            # Logo
            rx.hstack(
                rx.icon("briefcase", size=5),
                rx.heading("Clientnest", size="5"),
                align_items="center",
                spacing="2",
            ),
            rx.divider(),
            # Navigation items
            rx.vstack(
                sidebar_link("Dashboard", "/dashboard", "layout-dashboard"),
                sidebar_link("Projects", "/projects", "folder"),
                sidebar_link("Clients", "/clients", "users"),
                sidebar_link("Invoices", "/invoices", "file-text"),
                sidebar_link("Settings", "/settings", "settings"),
                spacing="2",
                align_items="stretch",
            ),
            rx.spacer(),
            # User info
            rx.box(
                rx.hstack(
                    rx.avatar(size="sm"),
                    rx.vstack(
                        rx.text("User Name", size="1", weight="bold"),
                        rx.text("user@example.com", size="1", color="gray"),
                        spacing="0",
                        align_items="start",
                    ),
                    align_items="center",
                    spacing="2",
                ),
                padding="3",
                background="gray.1",
                border_radius="md",
            ),
            spacing="4",
            align_items="stretch",
        ),
        width="250px",
        height="100vh",
        background="white",
        border_right="1px solid #e2e8f0",
        position="fixed",
        left="0",
        top="0",
        padding="4",
        display=["none", "none", "flex"],
    )


def mobile_navbar() -> rx.Component:
    """Create the mobile navigation bar component.
    
    Returns:
        A mobile navigation bar component.
    """
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.icon("briefcase", size=5),
                rx.heading("Clientnest", size="5"),
                align_items="center",
                spacing="2",
            ),
            rx.spacer(),
            # Mobile menu button
            rx.button(
                rx.icon("menu", size=5),
                on_click=lambda: rx.toggle_sidebar(),
                variant="ghost",
            ),
            align_items="center",
            spacing="4",
        ),
        padding="4",
        background="white",
        border_bottom="1px solid #e2e8f0",
        display=["flex", "flex", "none"],
    )


def mobile_sidebar() -> rx.Component:
    """Create the mobile sidebar component.
    
    Returns:
        A mobile sidebar component.
    """
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                rx.icon("menu", size=5),
                variant="ghost",
            ),
        ),
        rx.drawer.content(
            rx.vstack(
                # Logo
                rx.hstack(
                    rx.icon("briefcase", size=5),
                    rx.heading("Clientnest", size="5"),
                    align_items="center",
                    spacing="2",
                ),
                rx.divider(),
                # Navigation items
                rx.vstack(
                    sidebar_link("Dashboard", "/dashboard", "layout-dashboard"),
                    sidebar_link("Projects", "/projects", "folder"),
                    sidebar_link("Clients", "/clients", "users"),
                    sidebar_link("Invoices", "/invoices", "file-text"),
                    sidebar_link("Settings", "/settings", "settings"),
                    spacing="2",
                    align_items="stretch",
                ),
                rx.spacer(),
                # User info
                rx.box(
                    rx.hstack(
                        rx.avatar(size="sm"),
                        rx.vstack(
                            rx.text("User Name", size="1", weight="bold"),
                            rx.text("user@example.com", size="1", color="gray"),
                            spacing="0",
                            align_items="start",
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    padding="3",
                    background="gray.1",
                    border_radius="md",
                ),
                spacing="4",
                align_items="stretch",
            ),
            width="250px",
            padding="4",
        ),
    )


def nav_link(text: str, href: str) -> rx.Component:
    """Create a navigation link component.
    
    Args:
        text: The link text.
        href: The link href.
        
    Returns:
        A navigation link component.
    """
    return rx.link(
        text,
        href=href,
        color="gray",
        _hover={"color": "blue"},
        transition="all 0.2s",
    )


def sidebar_link(text: str, href: str, icon: str) -> rx.Component:
    """Create a sidebar link component.
    
    Args:
        text: The link text.
        href: The link href.
        icon: The icon name.
        
    Returns:
        A sidebar link component.
    """
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=4),
            rx.text(text, size="2"),
            align_items="center",
            spacing="2",
        ),
        href=href,
        padding="2",
        border_radius="md",
        _hover={"background": "gray.1"},
        transition="all 0.2s",
    )


def breadcrumb(items: list[tuple[str, str]]) -> rx.Component:
    """Create a breadcrumb component.
    
    Args:
        items: A list of (text, href) tuples.
        
    Returns:
        A breadcrumb component.
    """
    return rx.hstack(
        *[
            rx.fragment(
                rx.link(text, href=href, color="gray"),
                rx.icon("chevron-right", size=3, color="gray") if i < len(items) - 1 else None,
            )
            for i, (text, href) in enumerate(items)
        ],
        spacing="2",
        align_items="center",
        padding="2",
    )


def tabs(tabs: list[tuple[str, str]], active_tab: str) -> rx.Component:
    """Create a tabs component.
    
    Args:
        tabs: A list of (label, value) tuples.
        active_tab: The currently active tab value.
        
    Returns:
        A tabs component.
    """
    return rx.tabs.root(
        rx.tabs.list(
            *[
                rx.tabs.trigger(
                    label,
                    value=value,
                )
                for label, value in tabs
            ],
        ),
        *[
            rx.tabs.content(
                rx.text(f"Content for {label}"),
                value=value,
            )
            for label, value in tabs
        ],
        value=active_tab,
    )


def pagination(current_page: int, total_pages: int) -> rx.Component:
    """Create a pagination component.
    
    Args:
        current_page: The current page number.
        total_pages: The total number of pages.
        
    Returns:
        A pagination component.
    """
    return rx.hstack(
        rx.button(
            rx.icon("chevron-left", size=3),
            on_click=lambda: rx.previous_page(),
            disabled=current_page == 1,
            variant="soft",
        ),
        rx.text(
            f"Page {current_page} of {total_pages}",
            size="2",
        ),
        rx.button(
            rx.icon("chevron-right", size=3),
            on_click=lambda: rx.next_page(),
            disabled=current_page == total_pages,
            variant="soft",
        ),
        spacing="2",
        align_items="center",
    )


def search_bar(placeholder: str = "Search...") -> rx.Component:
    """Create a search bar component.
    
    Args:
        placeholder: The placeholder text.
        
    Returns:
        A search bar component.
    """
    return rx.hstack(
        rx.icon("search", size=4, color="gray"),
        rx.input(
            placeholder=placeholder,
            variant="ghost",
            width="100%",
        ),
        align_items="center",
        spacing="2",
        padding="2",
        background="gray.1",
        border_radius="md",
    )


def user_menu() -> rx.Component:
    """Create a user menu component.
    
    Returns:
        A user menu component.
    """
    return rx.menu.root(
        rx.menu.trigger(
            rx.hstack(
                rx.avatar(size="sm"),
                rx.icon("chevron-down", size=3),
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


def notification_dropdown() -> rx.Component:
    """Create a notification dropdown component.
    
    Returns:
        A notification dropdown component.
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
            rx.divider(),
            rx.vstack(
                rx.text("New project assigned", size="2"),
                rx.text("Invoice overdue", size="2"),
                rx.text("Client message received", size="2"),
                spacing="2",
            ),
            width="300",
        ),
    )
