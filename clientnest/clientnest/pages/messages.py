import reflex as rx
from ..state.message import MessageState


def messages_thread() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            MessageState.messages,
            lambda message: rx.hstack(
                rx.avatar(
                    fallback=message["sender_initials"],
                    size="3",
                ),
                rx.vstack(
                    rx.text(message["sender_name"], weight="bold", size="3"),
                    rx.text(message["body"], white_space="pre-wrap"),
                    rx.text(message["created_at"], size="2", color="gray"),
                    spacing="1",
                    align_items="start",
                ),
                align_items="start",
                spacing="3",
                width="100%",
                padding="3",
                border="1px solid",
                border_color=rx.cond(message["is_read"], "gray.100", "blue.100"),
                border_radius="md",
                background=rx.cond(message["is_read"], "gray.50", "blue.50"),
            ),
        ),
        spacing="3",
        width="100%",
        padding="4",
        overflow_y="auto",
        max_height="60vh",
    )


def message_input() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Type a message...",
            value=MessageState.new_message,
            on_change=MessageState.set_new_message,
            on_key_down=MessageState.send_on_enter,
            flex="1",
        ),
        rx.button(
            "Send",
            on_click=MessageState.send_message,
            color_scheme="blue",
            disabled=MessageState.new_message == "",
        ),
        width="100%",
        spacing="3",
        padding="4",
        border_top="1px solid",
        border_color="gray.200",
    )


@rx.page(route="/projects/[id]/messages", on_load=MessageState.load_messages)
def project_messages() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.hstack(
                rx.button(
                    rx.icon("arrow-left"),
                    on_click=rx.redirect("/projects"),
                    size="2",
                    variant="ghost",
                ),
                rx.heading("Messages", size="7"),
                rx.spacer(),
                rx.cond(
                    MessageState.unread_count > 0,
                    rx.badge(
                        MessageState.unread_count,
                        color_scheme="red",
                        variant="soft",
                    ),
                    rx.box(),
                ),
                align_items="center",
                width="100%",
            ),
            rx.cond(
                MessageState.loading,
                rx.center(rx.spinner(size="3"), height="200px"),
                rx.cond(
                    MessageState.messages.length() > 0,
                    messages_thread(),
                    rx.center(
                        rx.text(
                            "No messages yet. Start the conversation!",
                            size="4",
                            color="gray",
                        ),
                        height="200px",
                    ),
                ),
            ),
            message_input(),
            spacing="4",
            width="100%",
            min_height="85vh",
        ),
    )
