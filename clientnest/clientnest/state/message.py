import reflex as rx
from ..models.message import Message
from ..models.project import Project
from ..models.user import User
from typing import List, Dict


class MessageState(rx.State):
    """State for project messaging."""

    messages: List[Dict] = []
    new_message: str = ""
    unread_count: int = 0
    current_project_id: int = 0
    loading: bool = False

    @rx.event
    def load_messages(self):
        """Load messages for a project — called via on_load."""
        try:
            project_id = int(self.router.page.params.get("id", 0))
        except Exception:
            project_id = 0

        self.current_project_id = project_id
        self.loading = True

        with rx.session() as session:
            messages = (
                session.query(Message)
                .filter(Message.project_id == project_id)
                .order_by(Message.created_at.asc())
                .all()
            )

            result = []
            unread = 0

            for msg in messages:
                sender = session.query(User).filter(User.id == msg.sender_id).first()
                sender_name = sender.name if sender else "Unknown"
                parts = sender_name.split()
                initials = "".join([p[0].upper() for p in parts[:2]]) if parts else "??"

                result.append({
                    "id": msg.id,
                    "body": msg.body,
                    "is_read": msg.is_read,
                    "created_at": msg.created_at.strftime("%b %d, %H:%M") if msg.created_at else "",
                    "sender_id": msg.sender_id,
                    "sender_name": sender_name,
                    "sender_initials": initials,
                    "project_id": msg.project_id,
                })

                if not msg.is_read:
                    unread += 1

            self.messages = result
            self.unread_count = unread
            self.loading = False

            # Mark all as read
            session.query(Message).filter(
                Message.project_id == project_id,
                Message.is_read == False,
            ).update({Message.is_read: True})
            session.commit()
            self.unread_count = 0

    @rx.event
    def send_message(self):
        """Send a new message."""
        if not self.new_message.strip():
            return

        with rx.session() as session:
            message = Message(
                project_id=self.current_project_id,
                body=self.new_message.strip(),
            )
            session.add(message)
            session.commit()

        self.new_message = ""
        yield MessageState.load_messages()

    @rx.event
    def set_new_message(self, value: str):
        self.new_message = value

    @rx.event
    def send_on_enter(self, key: str):
        if key == "Enter" and self.new_message.strip():
            yield MessageState.send_message()
