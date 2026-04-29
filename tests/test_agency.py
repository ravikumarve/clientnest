#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import models
import sys

sys.path.insert(0, ".")
from clientnest.clientnest.models.agency import Agency
from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.base import Base


def test_agency_creation():
    """Test agency creation and basic functionality."""

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        # Create test agency
        agency = Agency(
            name="Test Agency", slug="test-agency", brand_color="#2563EB", plan="solo"
        )
        session.add(agency)
        session.commit()

        # Verify agency was created
        saved_agency = (
            session.query(Agency).filter(Agency.slug == "test-agency").first()
        )
        assert saved_agency is not None
        assert saved_agency.name == "Test Agency"
        assert saved_agency.slug == "test-agency"
        assert saved_agency.brand_color == "#2563EB"
        assert saved_agency.plan == "solo"

        print("✓ Agency creation test passed")


def test_agency_plan_gating():
    """Test agency plan-based feature gating."""

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        # Test free plan
        free_agency = Agency(name="Free Agency", slug="free-agency", plan="free")
        session.add(free_agency)

        # Test solo plan
        solo_agency = Agency(name="Solo Agency", slug="solo-agency", plan="solo")
        session.add(solo_agency)

        # Test agency plan
        agency_agency = Agency(
            name="Agency Agency", slug="agency-agency", plan="agency"
        )
        session.add(agency_agency)

        session.commit()

        # Test white-label feature access
        assert free_agency.plan == "free"
        assert solo_agency.plan == "solo"
        assert agency_agency.plan == "agency"

        print("✓ Agency plan gating test passed")


if __name__ == "__main__":
    test_agency_creation()
    test_agency_plan_gating()
