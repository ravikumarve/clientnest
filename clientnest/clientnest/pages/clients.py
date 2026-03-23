import reflex as rx
from ..state.agency import AgencyState


def clients() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Clients", size="8"),
            rx.hstack(
                rx.button(
                    "Invite Client",
                    on_click=AgencyState.clear_invite_form,
                    color_scheme="blue",
                ),
                rx.spacer(),
                rx.input(
                    placeholder="Search clients...",
                    on_change=lambda e: setattr(
                        AgencyState, "search_term", e.target.value
                    ),
                ),
                align_items="center",
                width="100%",
            ),
            rx.cond(
                AgencyState.clients.length() > 0,
                clients_table(),
                rx.text(
                    "No clients found. Invite your first client!",
                    size="4",
                    color_scheme="gray",
                ),
            ),
            rx.cond(
                AgencyState.show_invite_form,
                invite_client_form(),
                rx.box(),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            width="100%",
        ),
    )


def clients_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_client_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Projects"),
                rx.table.column_header_cell("Last Active"),
                rx.table.column_header_cell("Actions"),
            )
        ),
        rx.table.body(
            rx.foreach(
                AgencyState.clients,
                lambda client: rx.table.row(
                    rx.table.cell(client["name"]),
                    rx.table.cell(client["email"]),
                    rx.table.cell(client["projects_count"]),
                    rx.table.cell(client["last_active"] or "Never"),
                    rx.table.cell(
                        rx.hstack(
                            rx.button(
                                rx.icon("eye"),
                                size="1",
                                variant="ghost",
                            ),
                            rx.button(
                                rx.icon("message-square"),
                                size="1",
                                variant="ghost",
                            ),
                            spacing="2",
                        )
                    ),
                ),
            )
        ),
    )


def invite_client_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Invite New Client", size="6"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Client Email",
                        type="email",
                        name="email",
                        required=True,
                        value=AgencyState.invite_email,
                        on_change=lambda e: setattr(
                            AgencyState, "invite_email", e.target.value
                        ),
                    ),
                    rx.hstack(
                        rx.button(
                            "Cancel",
                            on_click=AgencyState.clear_invite_form,
                            variant="soft",
                        ),
                        rx.button(
                            "Send Invitation",
                            type="submit",
                            color_scheme="blue",
                        ),
                        spacing="3",
                    ),
                ),
                on_submit=AgencyState.invite_client,
                reset_on_submit=True,
            ),
            border="1px solid",
            border_color="gray.300",
            border_radius="lg",
            padding="4",
            width="100%",
            max_width="400px",
        ),
        position="fixed",
        top="20%",
        right="5%",
        z_index="1000",
        background_color="white",
    )
