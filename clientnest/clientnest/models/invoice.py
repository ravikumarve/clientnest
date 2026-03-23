from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from .base import Base


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, index=True)
    agency_id = Column(Integer, ForeignKey("agency.id"), nullable=False, index=True)
    client_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=True, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")  # USD | INR
    status = Column(String(20), default="unpaid")  # unpaid | paid | overdue | cancelled
    lemonsqueezy_checkout_url = Column(String(500), nullable=True)
    paid_at = Column(DateTime(timezone=True), nullable=True)
    due_date = Column(DateTime(timezone=True), nullable=True)
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
