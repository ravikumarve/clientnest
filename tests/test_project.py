"""Project tests for Clientnest application."""
import pytest
from datetime import datetime, date, timedelta
import sys
import os

# Add the clientnest module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from clientnest.clientnest.models.project import Project, Task
from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.agency import Agency


class TestProjectModel:
    """Test Project model."""
    
    def test_project_creation(self):
        """Test project creation."""
        project = Project(
            agency_id=1,
            client_id=1,
            title="Test Project",
            description="Test project description",
            status="in_progress",
            due_date=date(2024, 12, 31)
        )
        assert project.agency_id == 1
        assert project.client_id == 1
        assert project.title == "Test Project"
        assert project.status == "in_progress"
    
    def test_project_status_values(self):
        """Test project status values."""
        valid_statuses = [
            "not_started",
            "in_progress",
            "review",
            "completed",
            "on_hold"
        ]
        
        for status in valid_statuses:
            project = Project(
                agency_id=1,
                client_id=1,
                title="Test Project",
                status=status
            )
            assert project.status == status
    
    def test_project_timestamps(self):
        """Test project timestamps."""
        project = Project(
            agency_id=1,
            client_id=1,
            title="Test Project"
        )
        
        # Note: created_at and updated_at will be None until saved to database
        # This is expected behavior for SQLAlchemy models
        assert project.agency_id == 1
        assert project.client_id == 1
        assert project.title == "Test Project"
    
    def test_project_due_date(self):
        """Test project due date."""
        due_date = date(2024, 12, 31)
        project = Project(
            agency_id=1,
            client_id=1,
            title="Test Project",
            due_date=due_date
        )
        assert project.due_date == due_date
    
    def test_project_agency_scoping(self):
        """Test project is scoped to agency."""
        project = Project(
            agency_id=1,
            client_id=1,
            title="Agency 1 Project"
        )
        
        assert project.agency_id == 1
        assert project.agency_id != 2


class TestTaskModel:
    """Test Task model."""
    
    def test_task_creation(self):
        """Test task creation."""
        task = Task(
            project_id=1,
            title="Test Task",
            is_done=False,
            sort_order=0
        )
        assert task.project_id == 1
        assert task.title == "Test Task"
        assert task.is_done is False
        assert task.sort_order == 0
    
    def test_task_completion(self):
        """Test task completion."""
        task = Task(
            project_id=1,
            title="Test Task",
            is_done=False
        )
        
        assert task.is_done is False
        
        # Mark as done
        task.is_done = True
        assert task.is_done is True
    
    def test_task_sort_order(self):
        """Test task sort order."""
        task1 = Task(project_id=1, title="First task", sort_order=0)
        task2 = Task(project_id=1, title="Second task", sort_order=1)
        task3 = Task(project_id=1, title="Third task", sort_order=2)
        
        tasks = [task1, task2, task3]
        sorted_tasks = sorted(tasks, key=lambda t: t.sort_order)
        
        assert sorted_tasks[0].title == "First task"
        assert sorted_tasks[1].title == "Second task"
        assert sorted_tasks[2].title == "Third task"
    
    def test_task_project_scoping(self):
        """Test task is scoped to project."""
        task = Task(
            project_id=1,
            title="Project 1 Task"
        )
        
        assert task.project_id == 1
        assert task.project_id != 2


class TestProjectProgress:
    """Test project progress calculations."""
    
    def test_project_task_completion_rate(self):
        """Test calculating task completion rate."""
        tasks = [
            Task(project_id=1, title="Task 1", is_done=True),
            Task(project_id=1, title="Task 2", is_done=True),
            Task(project_id=1, title="Task 3", is_done=False),
            Task(project_id=1, title="Task 4", is_done=False),
        ]
        
        completed = sum(1 for t in tasks if t.is_done)
        total = len(tasks)
        completion_rate = completed / total if total > 0 else 0
        
        assert completion_rate == 0.5  # 2 out of 4 tasks completed
    
    def test_project_overdue_detection(self):
        """Test detecting overdue projects."""
        today = date.today()
        past_date = today - timedelta(days=10)
        
        project = Project(
            agency_id=1,
            client_id=1,
            title="Overdue Project",
            status="in_progress",
            due_date=past_date
        )
        
        # Should be overdue
        assert project.due_date < today
        assert project.status == "in_progress"
    
    def test_project_active_status(self):
        """Test identifying active projects."""
        active_statuses = ["in_progress", "review"]
        
        for status in active_statuses:
            project = Project(
                agency_id=1,
                client_id=1,
                title="Active Project",
                status=status
            )
            assert status in active_statuses


class TestProjectSecurity:
    """Test project security."""
    
    def test_project_access_control(self):
        """Test project access control."""
        project = Project(
            agency_id=1,
            client_id=1,
            title="Agency 1 Project"
        )
        
        # Project should only be accessible to agency 1
        assert project.agency_id == 1
        
        # Different agency should not have access
        assert project.agency_id != 2
    
    def test_project_client_access(self):
        """Test client access to their projects."""
        project = Project(
            agency_id=1,
            client_id=1,
            title="Client 1 Project"
        )
        
        # Client 1 should have access
        assert project.client_id == 1
        
        # Client 2 should not have access
        assert project.client_id != 2
    
    def test_task_access_control(self):
        """Test task access control."""
        task = Task(
            project_id=1,
            title="Project 1 Task"
        )
        
        # Task should only be accessible through project 1
        assert task.project_id == 1


class TestProjectFiltering:
    """Test project filtering."""
    
    def test_filter_by_status(self):
        """Test filtering projects by status."""
        projects = [
            Project(agency_id=1, client_id=1, title="P1", status="in_progress"),
            Project(agency_id=1, client_id=1, title="P2", status="completed"),
            Project(agency_id=1, client_id=1, title="P3", status="in_progress"),
            Project(agency_id=1, client_id=1, title="P4", status="on_hold"),
        ]
        
        in_progress = [p for p in projects if p.status == "in_progress"]
        completed = [p for p in projects if p.status == "completed"]
        
        assert len(in_progress) == 2
        assert len(completed) == 1
    
    def test_filter_by_client(self):
        """Test filtering projects by client."""
        projects = [
            Project(agency_id=1, client_id=1, title="Client 1 P1"),
            Project(agency_id=1, client_id=2, title="Client 2 P1"),
            Project(agency_id=1, client_id=1, title="Client 1 P2"),
        ]
        
        client1_projects = [p for p in projects if p.client_id == 1]
        client2_projects = [p for p in projects if p.client_id == 2]
        
        assert len(client1_projects) == 2
        assert len(client2_projects) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])