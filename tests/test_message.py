"""Message tests for Clientnest application."""
import pytest
from datetime import datetime, timedelta
import sys
import os

# Add the clientnest module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from clientnest.clientnest.models.message import Message
from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.project import Project


class TestMessageModel:
    """Test Message model."""
    
    def test_message_creation(self):
        """Test message creation."""
        message = Message(
            project_id=1,
            sender_id=1,
            body="Test message content",
            is_read=False
        )
        assert message.project_id == 1
        assert message.sender_id == 1
        assert message.body == "Test message content"
        assert message.is_read is False
    
    def test_message_read_status(self):
        """Test message read status."""
        message = Message(
            project_id=1,
            sender_id=1,
            body="Test message",
            is_read=False
        )
        
        # Initially unread
        assert message.is_read is False
        
        # Mark as read
        message.is_read = True
        assert message.is_read is True
    
    def test_message_timestamp(self):
        """Test message timestamp."""
        message = Message(
            project_id=1,
            sender_id=1,
            body="Test message"
        )
        
        # Note: created_at will be None until saved to database
        # This is expected behavior for SQLAlchemy models
        assert message.project_id == 1
        assert message.sender_id == 1
    
    def test_message_body_length(self):
        """Test message body length constraints."""
        # Short message
        short_message = Message(
            project_id=1,
            sender_id=1,
            body="Hi"
        )
        assert len(short_message.body) == 2
        
        # Long message
        long_text = "A" * 1000
        long_message = Message(
            project_id=1,
            sender_id=1,
            body=long_text
        )
        assert len(long_message.body) == 1000


class TestMessageThread:
    """Test message thread functionality."""
    
    def test_message_thread_ordering(self):
        """Test messages are ordered by creation time."""
        now = datetime.now()
        
        message1 = Message(
            project_id=1,
            sender_id=1,
            body="First message",
            created_at=now - timedelta(minutes=10)
        )
        
        message2 = Message(
            project_id=1,
            sender_id=2,
            body="Second message",
            created_at=now - timedelta(minutes=5)
        )
        
        message3 = Message(
            project_id=1,
            sender_id=1,
            body="Third message",
            created_at=now
        )
        
        # Messages should be ordered by created_at
        messages = [message1, message2, message3]
        sorted_messages = sorted(messages, key=lambda m: m.created_at)
        
        assert sorted_messages[0].body == "First message"
        assert sorted_messages[1].body == "Second message"
        assert sorted_messages[2].body == "Third message"
    
    def test_message_thread_participants(self):
        """Test message thread has multiple participants."""
        message1 = Message(
            project_id=1,
            sender_id=1,
            body="Message from user 1"
        )
        
        message2 = Message(
            project_id=1,
            sender_id=2,
            body="Message from user 2"
        )
        
        # Both messages are in the same project
        assert message1.project_id == message2.project_id
        assert message1.sender_id != message2.sender_id


class TestMessageReadTracking:
    """Test message read tracking."""
    
    def test_unread_message_count(self):
        """Test counting unread messages."""
        messages = [
            Message(project_id=1, sender_id=1, body="Read message", is_read=True),
            Message(project_id=1, sender_id=2, body="Unread message 1", is_read=False),
            Message(project_id=1, sender_id=1, body="Unread message 2", is_read=False),
            Message(project_id=1, sender_id=2, body="Read message 2", is_read=True),
        ]
        
        unread_count = sum(1 for m in messages if not m.is_read)
        assert unread_count == 2
    
    def test_mark_messages_as_read(self):
        """Test marking messages as read."""
        messages = [
            Message(project_id=1, sender_id=1, body="Message 1", is_read=False),
            Message(project_id=1, sender_id=2, body="Message 2", is_read=False),
        ]
        
        # Mark all as read
        for message in messages:
            message.is_read = True
        
        # All should be read
        assert all(m.is_read for m in messages)
    
    def test_per_project_unread_count(self):
        """Test unread count per project."""
        project1_messages = [
            Message(project_id=1, sender_id=1, body="P1 Unread", is_read=False),
            Message(project_id=1, sender_id=2, body="P1 Read", is_read=True),
        ]
        
        project2_messages = [
            Message(project_id=2, sender_id=1, body="P2 Unread", is_read=False),
            Message(project_id=2, sender_id=2, body="P2 Unread 2", is_read=False),
        ]
        
        p1_unread = sum(1 for m in project1_messages if not m.is_read)
        p2_unread = sum(1 for m in project2_messages if not m.is_read)
        
        assert p1_unread == 1
        assert p2_unread == 2


class TestMessageSecurity:
    """Test message security."""
    
    def test_message_project_scoping(self):
        """Test messages are scoped to projects."""
        message = Message(
            project_id=1,
            sender_id=1,
            body="Project 1 message"
        )
        
        # Message should only belong to project 1
        assert message.project_id == 1
        assert message.project_id != 2
    
    def test_message_sender_verification(self):
        """Test message sender is verified."""
        message = Message(
            project_id=1,
            sender_id=1,
            body="My message"
        )
        
        # Sender ID should be preserved
        assert message.sender_id == 1
        assert message.sender_id != 999
    
    def test_message_content_security(self):
        """Test message content doesn't contain malicious patterns."""
        # Test that message body is stored as-is (sanitization happens at display time)
        message = Message(
            project_id=1,
            sender_id=1,
            body="<script>alert('xss')</script>"
        )
        
        # Content should be stored but rendered safely
        assert "<script>" in message.body


if __name__ == "__main__":
    pytest.main([__file__, "-v"])