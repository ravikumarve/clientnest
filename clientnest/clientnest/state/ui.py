"""UI state management for Clientnest."""
from typing import Optional

import reflex as rx


class UIState(rx.State):
    """State for UI-related functionality."""
    
    # Sidebar state
    sidebar_open: bool = True
    
    # Active tab
    active_tab: str = "dashboard"
    
    # Modal state
    modal_open: bool = False
    modal_title: Optional[str] = None
    modal_content: Optional[str] = None
    
    # Toast notification state
    toast_message: Optional[str] = None
    toast_type: str = "info"  # info, success, warning, error
    toast_show: bool = False
    
    # Loading state
    loading: bool = False
    loading_message: Optional[str] = None
    
    # Confirmation dialog state
    confirm_dialog_open: bool = False
    confirm_dialog_title: Optional[str] = None
    confirm_dialog_message: Optional[str] = None
    confirm_dialog_action: Optional[str] = None
    
    # Form state
    form_errors: dict = {}
    form_data: dict = {}
    
    # Pagination state
    current_page: int = 1
    items_per_page: int = 10
    total_items: int = 0
    
    # Filter state
    filter_text: str = ""
    filter_status: Optional[str] = None
    filter_date_from: Optional[str] = None
    filter_date_to: Optional[str] = None
    
    # Sort state
    sort_field: Optional[str] = None
    sort_direction: str = "asc"  # asc or desc
    
    # Theme state
    theme: str = "light"  # light or dark
    
    # Explicit setter methods for State vars with on_change
    
    def set_sidebar_open(self, value: bool) -> None:
        """Set the sidebar open state.
        
        Args:
            value: The new sidebar open state.
        """
        self.sidebar_open = value
    
    def set_active_tab(self, value: str) -> None:
        """Set the active tab.
        
        Args:
            value: The new active tab.
        """
        self.active_tab = value
    
    def set_modal_open(self, value: bool) -> None:
        """Set the modal open state.
        
        Args:
            value: The new modal open state.
        """
        self.modal_open = value
    
    def set_modal_title(self, value: Optional[str]) -> None:
        """Set the modal title.
        
        Args:
            value: The new modal title.
        """
        self.modal_title = value
    
    def set_modal_content(self, value: Optional[str]) -> None:
        """Set the modal content.
        
        Args:
            value: The new modal content.
        """
        self.modal_content = value
    
    def set_toast_message(self, value: Optional[str]) -> None:
        """Set the toast message.
        
        Args:
            value: The new toast message.
        """
        self.toast_message = value
    
    def set_toast_type(self, value: str) -> None:
        """Set the toast type.
        
        Args:
            value: The new toast type.
        """
        self.toast_type = value
    
    def set_toast_show(self, value: bool) -> None:
        """Set the toast show state.
        
        Args:
            value: The new toast show state.
        """
        self.toast_show = value
    
    def set_loading(self, value: bool) -> None:
        """Set the loading state.
        
        Args:
            value: The new loading state.
        """
        self.loading = value
    
    def set_loading_message(self, value: Optional[str]) -> None:
        """Set the loading message.
        
        Args:
            value: The new loading message.
        """
        self.loading_message = value
    
    def set_confirm_dialog_open(self, value: bool) -> None:
        """Set the confirm dialog open state.
        
        Args:
            value: The new confirm dialog open state.
        """
        self.confirm_dialog_open = value
    
    def set_confirm_dialog_title(self, value: Optional[str]) -> None:
        """Set the confirm dialog title.
        
        Args:
            value: The new confirm dialog title.
        """
        self.confirm_dialog_title = value
    
    def set_confirm_dialog_message(self, value: Optional[str]) -> None:
        """Set the confirm dialog message.
        
        Args:
            value: The new confirm dialog message.
        """
        self.confirm_dialog_message = value
    
    def set_confirm_dialog_action(self, value: Optional[str]) -> None:
        """Set the confirm dialog action.
        
        Args:
            value: The new confirm dialog action.
        """
        self.confirm_dialog_action = value
    
    def set_form_errors(self, value: dict) -> None:
        """Set the form errors.
        
        Args:
            value: The new form errors.
        """
        self.form_errors = value
    
    def set_form_data(self, value: dict) -> None:
        """Set the form data.
        
        Args:
            value: The new form data.
        """
        self.form_data = value
    
    def set_current_page(self, value: int) -> None:
        """Set the current page.
        
        Args:
            value: The new current page.
        """
        self.current_page = value
    
    def set_items_per_page(self, value: int) -> None:
        """Set the items per page.
        
        Args:
            value: The new items per page.
        """
        self.items_per_page = value
    
    def set_total_items(self, value: int) -> None:
        """Set the total items.
        
        Args:
            value: The new total items.
        """
        self.total_items = value
    
    def set_filter_text(self, value: str) -> None:
        """Set the filter text.
        
        Args:
            value: The new filter text.
        """
        self.filter_text = value
    
    def set_filter_status(self, value: Optional[str]) -> None:
        """Set the filter status.
        
        Args:
            value: The new filter status.
        """
        self.filter_status = value
    
    def set_filter_date_from(self, value: Optional[str]) -> None:
        """Set the filter date from.
        
        Args:
            value: The new filter date from.
        """
        self.filter_date_from = value
    
    def set_filter_date_to(self, value: Optional[str]) -> None:
        """Set the filter date to.
        
        Args:
            value: The new filter date to.
        """
        self.filter_date_to = value
    
    def set_sort_field(self, value: Optional[str]) -> None:
        """Set the sort field.
        
        Args:
            value: The new sort field.
        """
        self.sort_field = value
    
    def set_sort_direction(self, value: str) -> None:
        """Set the sort direction.
        
        Args:
            value: The new sort direction.
        """
        self.sort_direction = value
    
    def set_theme(self, value: str) -> None:
        """Set the theme.
        
        Args:
            value: The new theme.
        """
        self.theme = value
    
    # Event handlers
    
    @rx.event
    def toggle_sidebar(self) -> None:
        """Toggle the sidebar open state."""
        self.sidebar_open = not self.sidebar_open
    
    @rx.event
    def open_modal(self, title: str, content: str) -> None:
        """Open a modal.
        
        Args:
            title: The modal title.
            content: The modal content.
        """
        self.modal_open = True
        self.modal_title = title
        self.modal_content = content
    
    @rx.event
    def close_modal(self) -> None:
        """Close the modal."""
        self.modal_open = False
        self.modal_title = None
        self.modal_content = None
    
    @rx.event
    def show_toast(self, message: str, toast_type: str = "info") -> None:
        """Show a toast notification.
        
        Args:
            message: The toast message.
            toast_type: The toast type (info, success, warning, error).
        """
        self.toast_message = message
        self.toast_type = toast_type
        self.toast_show = True
    
    @rx.event
    def hide_toast(self) -> None:
        """Hide the toast notification."""
        self.toast_show = False
    
    @rx.event
    def show_loading(self, message: Optional[str] = None) -> None:
        """Show loading state.
        
        Args:
            message: The loading message.
        """
        self.loading = True
        self.loading_message = message
    
    @rx.event
    def hide_loading(self) -> None:
        """Hide loading state."""
        self.loading = False
        self.loading_message = None
    
    @rx.event
    def show_confirm_dialog(self, title: str, message: str, action: str) -> None:
        """Show a confirmation dialog.
        
        Args:
            title: The dialog title.
            message: The dialog message.
            action: The action to perform on confirmation.
        """
        self.confirm_dialog_open = True
        self.confirm_dialog_title = title
        self.confirm_dialog_message = message
        self.confirm_dialog_action = action
    
    @rx.event
    def hide_confirm_dialog(self) -> None:
        """Hide the confirmation dialog."""
        self.confirm_dialog_open = False
        self.confirm_dialog_title = None
        self.confirm_dialog_message = None
        self.confirm_dialog_action = None
    
    @rx.event
    def confirm_action(self) -> None:
        """Perform the confirmed action."""
        if self.confirm_dialog_action == "delete":
            # Handle delete action
            pass
        elif self.confirm_dialog_action == "cancel":
            # Handle cancel action
            pass
        
        self.hide_confirm_dialog()
    
    @rx.event
    def clear_form_errors(self) -> None:
        """Clear form errors."""
        self.form_errors = {}
    
    @rx.event
    def clear_form_data(self) -> None:
        """Clear form data."""
        self.form_data = {}
    
    @rx.event
    def reset_filters(self) -> None:
        """Reset filters to default values."""
        self.filter_text = ""
        self.filter_status = None
        self.filter_date_from = None
        self.filter_date_to = None
    
    @rx.event
    def next_page(self) -> None:
        """Go to the next page."""
        max_page = (self.total_items + self.items_per_page - 1) // self.items_per_page
        if self.current_page < max_page:
            self.current_page += 1
    
    @rx.event
    def previous_page(self) -> None:
        """Go to the previous page."""
        if self.current_page > 1:
            self.current_page -= 1
    
    @rx.event
    def go_to_page(self, page: int) -> None:
        """Go to a specific page.
        
        Args:
            page: The page number to go to.
        """
        max_page = (self.total_items + self.items_per_page - 1) // self.items_per_page
        if 1 <= page <= max_page:
            self.current_page = page
    
    @rx.event
    def toggle_sort(self, field: str) -> None:
        """Toggle sort direction for a field.
        
        Args:
            field: The field to sort by.
        """
        if self.sort_field == field:
            # Toggle direction
            self.sort_direction = "desc" if self.sort_direction == "asc" else "asc"
        else:
            # New field, set to ascending
            self.sort_field = field
            self.sort_direction = "asc"
    
    @rx.event
    def toggle_theme(self) -> None:
        """Toggle between light and dark theme."""
        self.theme = "dark" if self.theme == "light" else "light"
    
    # Computed properties
    
    @rx.var
    def total_pages(self) -> int:
        """Calculate the total number of pages."""
        if self.items_per_page == 0:
            return 0
        return (self.total_items + self.items_per_page - 1) // self.items_per_page
    
    @rx.var
    def has_next_page(self) -> bool:
        """Check if there's a next page."""
        return self.current_page < self.total_pages
    
    @rx.var
    def has_previous_page(self) -> bool:
        """Check if there's a previous page."""
        return self.current_page > 1
    
    @rx.var
    def page_start(self) -> int:
        """Calculate the starting item number for the current page."""
        return (self.current_page - 1) * self.items_per_page + 1
    
    @rx.var
    def page_end(self) -> int:
        """Calculate the ending item number for the current page."""
        return min(self.current_page * self.items_per_page, self.total_items)
