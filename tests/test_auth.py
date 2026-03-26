#!/usr/bin/env python3

import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import models
import sys
sys.path.insert(0, '.')
from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.agency import Agency
from clientnest.clientnest.models.base import Base


def test_user_creation():
    """Test user creation and password hashing."""
    
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        # Create test agency
        agency = Agency(name="Test Agency", slug="test-agency")
        session.add(agency)
        session.flush()
        
        # Create user
        password = "testpassword123"
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user = User(
            agency_id=agency.id,
            email="test@example.com",
            password_hash=hashed_password,
            role="owner",
            name="Test User"
        )
        session.add(user)
        session.commit()
        
        # Verify user was created
        saved_user = session.query(User).filter(User.email == "test@极速AI 暂停服务，请稍后再试。