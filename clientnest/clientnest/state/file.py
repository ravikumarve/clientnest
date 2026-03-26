import reflex as rx
import uuid
import os
from pathlib import Path
from ..models.file import File
from ..models.project import Project
from ..models.user import User
from .auth import AuthState
from typing import List, Dict


class FileState(rx.State):
    """State for file management."""

    files: List[Dict] = []
    upload_progress: int = 0
    uploading: bool = False
    current_project_id: int = 0

    @rx.event
    def load_files(self):
        """Load files for a project — called via on_load."""
        try:
            project_id = int(self.router.page.params.get("id", 0))
        except Exception:
            project_id = 0

        self.current_project_id = project_id

        with rx.session() as session:
            files = (
                session.query(File)
                .filter(
                    File.project_id == project_id,
                    File.is_deleted == False,
                )
                .order_by(File.created_at.desc())
                .all()
            )

            result = []
            for f in files:
                uploader = session.query(User).filter(User.id == f.uploaded_by).first()
                uploader_name = uploader.name if uploader else "Unknown"

                result.append(
                    {
                        "id": f.id,
                        "filename": f.filename,
                        "stored_path": f.stored_path,
                        "file_size": f.file_size,
                        "mime_type": f.mime_type,
                        "created_at": f.created_at.strftime("%b %d, %Y %H:%M")
                        if f.created_at
                        else "",
                        "uploader_name": uploader_name,
                        "uploader_id": f.uploaded_by,
                        "project_id": f.project_id,
                    }
                )

            self.files = result

    @rx.event
    def handle_upload(self, files: List[rx.UploadFile]):
        """Handle file upload."""
        if not files:
            return

        self.uploading = True
        self.upload_progress = 0

        uploads_dir = Path("uploads")
        uploads_dir.mkdir(exist_ok=True)

        for file in files:
            try:
                # Create project-specific directory
                project_dir = uploads_dir / str(self.current_project_id)
                project_dir.mkdir(exist_ok=True)

                # Generate unique filename
                unique_id = str(uuid.uuid4())
                stored_filename = f"{unique_id}_{file.filename}"
                file_path = project_dir / stored_filename

                # Write file
                with open(file_path, "wb") as f:
                    content = file.read()
                    f.write(content)

                # Save to database
                with rx.session() as session:
                    db_file = File(
                        project_id=self.current_project_id,
                        uploaded_by=AuthState.user_id,
                        filename=file.filename,
                        stored_path=str(file_path),
                        file_size=len(content),
                        mime_type=file.content_type or "application/octet-stream",
                    )
                    session.add(db_file)
                    session.commit()

                self.upload_progress = 100

            except Exception as e:
                print(f"Upload error: {e}")

        self.uploading = False
        yield FileState.load_files()

    @rx.event
    def download_file(self, file_id: int):
        """Download a file."""
        with rx.session() as session:
            file = session.query(File).filter(File.id == file_id).first()
            if file and not file.is_deleted:
                if Path(file.stored_path).exists():
                    return rx.download(
                        data=open(file.stored_path, "rb").read(),
                        filename=file.filename,
                        content_type=file.mime_type,
                    )
        return rx.window_alert("File not found")

    @rx.event
    def delete_file(self, file_id: int):
        """Soft delete a file."""
        with rx.session() as session:
            file = session.query(File).filter(File.id == file_id).first()
            if file:
                file.is_deleted = True
                session.commit()
                yield FileState.load_files()

    @rx.event
    def set_upload_progress(self, value: int):
        self.upload_progress = value

    @rx.event
    def set_uploading(self, value: bool):
        self.uploading = value
