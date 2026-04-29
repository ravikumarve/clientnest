from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from .base import Base


class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False, index=True)
    uploaded_by = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    filename = Column(String(300), nullable=False)  # original filename shown to user
    stored_path = Column(
        String(500), nullable=False
    )  # uploads/{agency_id}/{project_id}/{uuid}_{filename}
    file_size = Column(Integer, nullable=False)  # bytes
    mime_type = Column(String(100), nullable=False)
    is_deleted = Column(Boolean, default=False)  # soft delete
    created_at = Column(DateTime(timezone=True), server_default=func.now())
