import reflex as rx


class DashboardState(rx.State):
    """Dashboard state."""

    # Dashboard data
    projects_count: int = 0
    clients_count: int = 0
    invoices_count: int = 0

    @rx.event
    def load_data(self):
        """Load dashboard data on page load."""
        # Placeholder for now - will be implemented in later weeks
        pass
