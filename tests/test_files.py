#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import models
import sys

sys.path.insert(0, ".")
from clientnest.clientnest.models.file import File
from clientnest.clientnest.models.project import Project
from clientnest.clientnest.models.agency import Agency
from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.base import Base


def test_file_model():
    """Test file model creation and soft delete."""

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        # Create test data
        agency = Agency(name="Test Agency", slug="test-agency")
        session.add(agency)
        session.commit()

        user = User(
            agency_id=agency.id,
            email="test@example.com",
            password_hash="testhash",
            role="owner",
            name="Test User",
        )
        session.add(user)
        session.commit()

        project = Project(
            agency_id=agency.id,
            client_id=user.id,
            title="Test Project",
            status="in_progress",
        )
        session.add(project)
        session.commit()

        # Create test file
        file = File(
            project_id=project.id,
            uploaded_by=user.id,
            filename="test.txt",
            stored_path="/uploads/test.txt",
            file_size=1024,
            mime_type="text/plain",
        )
        session.add(file)
        session.commit()

        # Verify file was created
        saved_file = session.query(File).filter(File.filename == "test.txt").first()
        assert saved_file is not None
        assert saved_file.filename == "test.txt"
        assert saved_file.file_size == 1024
        assert saved_file.mime_type == "text/plain"
        assert saved_file.is_deleted == False

        # Test soft delete
        saved_file.is_deleted = True
        session.commit()

        # Verify soft delete
        deleted_file = session.query(File).filter(File.filename == "test.txt").first()
        assert deleted_file.is_deleted == True

        print("✓ File model test passed")


if __name__ == "__main__":
    test_file_model()
