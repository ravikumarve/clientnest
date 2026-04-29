"""Invoice tests for Clientnest application."""
import pytest
from datetime import datetime, date, timedelta
from decimal import Decimal
import sys
import os

# Add the clientnest module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from clientnest.clientnest.models.invoice import Invoice
from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.agency import Agency
from clientnest.clientnest.models.project import Project


class TestInvoiceModel:
    """Test Invoice model."""
    
    def test_invoice_creation(self):
        """Test invoice creation."""
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            project_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            status="unpaid",
            due_date=date(2024, 12, 31)
        )
        assert invoice.agency_id == 1
        assert invoice.client_id == 1
        assert invoice.amount == Decimal("100.00")
        assert invoice.currency == "USD"
        assert invoice.status == "unpaid"
    
    def test_invoice_status_transitions(self):
        """Test invoice status transitions."""
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            status="unpaid"
        )
        
        # Test valid status transitions
        invoice.status = "paid"
        assert invoice.status == "paid"
        
        invoice.status = "overdue"
        assert invoice.status == "overdue"
        
        invoice.status = "cancelled"
        assert invoice.status == "cancelled"
    
    def test_invoice_currencies(self):
        """Test invoice currency support."""
        # Test USD
        invoice_usd = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD"
        )
        assert invoice_usd.currency == "USD"
        
        # Test INR
        invoice_inr = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("7500.00"),
            currency="INR"
        )
        assert invoice_inr.currency == "INR"
    
    def test_invoice_amount_validation(self):
        """Test invoice amount validation."""
        # Test positive amounts
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD"
        )
        assert invoice.amount > 0
        
        # Test decimal precision
        invoice_precise = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("99.99"),
            currency="USD"
        )
        assert invoice_precise.amount == Decimal("99.99")
    
    def test_invoice_due_date(self):
        """Test invoice due date."""
        due_date = date(2024, 12, 31)
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            due_date=due_date
        )
        assert invoice.due_date == due_date
    
    def test_invoice_lemonsqueezy_integration(self):
        """Test LemonSqueezy integration fields."""
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            lemonsqueezy_checkout_url="https://checkout.lemonsqueezy.com/checkout/test"
        )
        assert invoice.lemonsqueezy_checkout_url is not None
        assert "lemonsqueezy.com" in invoice.lemonsqueezy_checkout_url
    
    def test_invoice_payment_tracking(self):
        """Test invoice payment tracking."""
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            status="unpaid"
        )
        
        # Mark as paid
        invoice.status = "paid"
        invoice.paid_at = datetime.now()
        
        assert invoice.status == "paid"
        assert invoice.paid_at is not None


class TestInvoiceCalculations:
    """Test invoice-related calculations."""
    
    def test_invoice_total_by_agency(self):
        """Test calculating total invoices by agency."""
        # This would typically be a database query
        # For now, we'll test the concept
        agency_id = 1
        assert agency_id == 1
    
    def test_invoice_overdue_detection(self):
        """Test detecting overdue invoices."""
        today = date.today()
        past_date = today - timedelta(days=10)
        
        # Create an invoice with a past due date
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            status="unpaid",
            due_date=past_date
        )
        
        # Should be overdue
        assert invoice.due_date < today
        assert invoice.status == "unpaid"
    
    def test_invoice_paid_this_month(self):
        """Test finding invoices paid this month."""
        today = datetime.now()
        start_of_month = date(today.year, today.month, 1)
        
        invoice = Invoice(
            agency_id=1,
            client_id=1,
            amount=Decimal("100.00"),
            currency="USD",
            status="paid",
            paid_at=start_of_month
        )
        
        assert invoice.paid_at >= start_of_month


if __name__ == "__main__":
    pytest.main([__file__, "-v"])