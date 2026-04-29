from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .base import Base


class Agency(Base):
    __tablename__ = "agency"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    slug = Column(String(80), unique=True, nullable=False, index=True)
    logo_url = Column(String(300), nullable=True)
    brand_color = Column(String(7), default="#2563EB")
    custom_domain = Column(String(200), nullable=True)
    plan = Column(String(20), default="free")  # free | solo | agency | studio
    subscription_id = Column(String(100), nullable=True)  # LemonSqueezy subscription ID
    subscription_status = Column(
        String(20), default="inactive"
    )  # active | inactive | cancelled | past_due
    created_at = Column(DateTime(timezone=True), server_default=func.now())
