"""Client invite model for Clientnest."""
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ClientInvite(Base):
    """Client invite model for managing client invitations."""
    
    __tablename__ = "client_invites"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Agency that sent the invite
    agency_id: Mapped[int] = mapped_column(index=True, nullable=False)
    
    # Email of the invited client
    email: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    
    # Unique token for the invite
    token: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    
    # Whether the invite has been accepted
    is_accepted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Whether the invite has been cancelled
    is_cancelled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Expiry date for the invite (7 days from creation)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    # When the invite was created
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    
    # When the invite was accepted
    accepted_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    
    # ID of the user who accepted the invite
    accepted_by: Mapped[Optional[int]] = mapped_column(nullable=True)
    
    # Name of the inviter (for display in email)
    inviter_name: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    
    # Custom message for the invite
    message: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    
    def __repr__(self) -> str:
        """String representation of the client invite."""
        return f"<ClientInvite(id={self.id}, email={self.email}, agency_id={self.agency_id})>"
    
    def is_expired(self) -> bool:
        """Check if the invite has expired.
        
        Returns:
            True if the invite has expired, False otherwise.
        """
        return datetime.utcnow() > self.expires_at
    
    def is_valid(self) -> bool:
        """Check if the invite is valid (not expired, not accepted, not cancelled).
        
        Returns:
            True if the invite is valid, False otherwise.
        """
        return not self.is_expired() and not self.is_accepted and not self.is_cancelled
    
    def mark_as_accepted(self, user_id: int) -> None:
        """Mark the invite as accepted.
        
        Args:
            user_id: The ID of the user who accepted the invite.
        """
        self.is_accepted = True
        self.accepted_at = datetime.utcnow()
        self.accepted_by = user_id
    
    def cancel(self) -> None:
        """Cancel the invite."""
        self.is_cancelled = True
    
    @classmethod
    def create(cls, agency_id: int, email: str, token: str, inviter_name: Optional[str] = None, message: Optional[str] = None) -> "ClientInvite":
        """Create a new client invite.
        
        Args:
            agency_id: The ID of the agency sending the invite.
            email: The email of the invited client.
            token: The unique token for the invite.
            inviter_name: The name of the inviter (optional).
            message: A custom message for the invite (optional).
            
        Returns:
            A new ClientInvite instance.
        """
        expires_at = datetime.utcnow() + timedelta(days=7)
        
        return cls(
            agency_id=agency_id,
            email=email,
            token=token,
            expires_at=expires_at,
            inviter_name=inviter_name,
            message=message,
        )
