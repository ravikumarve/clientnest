import reflex as rx
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
import uuid
from datetime import datetime, timedelta


class EmailService:
    """Email service for sending notifications and invites."""

    @staticmethod
    def send_invite_email(
        to_email: str, agency_name: str, invite_token: str, inviter_name: str
    ) -> bool:
        """Send client invitation email."""
        try:
            # Get email configuration from environment
            smtp_host = rx.get_env_var("SMTP_HOST")
            smtp_port = int(rx.get_env_var("SMTP_PORT", "587"))
            smtp_user = rx.get_env_var("SMTP_USER")
            smtp_pass = rx.get_env_var("SMTP_PASS")

            # Use Resend if SMTP not configured
            if not smtp_host and rx.get_env_var("RESEND_API_KEY"):
                return EmailService._send_via_resend(
                    to_email, agency_name, invite_token, inviter_name
                )

            if not all([smtp_host, smtp_user, smtp_pass]):
                print("Email configuration incomplete - skipping email send")
                return False

            # Create message
            app_url = rx.get_env_var("APP_URL", "http://localhost:3000")
            accept_url = f"{app_url}/accept-invite/{invite_token}"

            subject = f"Invitation to join {agency_name}'s client portal"

            html_content = f"""
            <!DOCTYPE html>
            <html>
            <body>
                <h2>You've been invited to {agency_name}'s client portal</h2>
                <p>Hello,</p>
                <p>{inviter_name} has invited you to join their client portal on Clientnest.</p>
                <p>Click the link below to accept the invitation and set up your account:</p>
                <a href="{accept_url}" style="
                    display: inline-block;
                    padding: 12px 24px;
                    background-color: #2563EB;
                    color: white;
                    text-decoration: none;
                    border-radius: 6px;
                    font-weight: bold;
                ">Accept Invitation</a>
                <p>This invitation link will expire in 7 days.</p>
                <p>If you didn't expect this invitation, please ignore this email.</p>
            </body>
            </html>
            """

            text_content = f"""
            You've been invited to {agency_name}'s client portal
            
            Hello,
            
            {inviter_name} has invited you to join their client portal on Clientnest.
            
            Accept your invitation here: {accept_url}
            
            This invitation link will expire in 7 days.
            
            If you didn't expect this invitation, please ignore this email.
            """

            # Create message
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = smtp_user
            msg["To"] = to_email

            # Attach parts
            msg.attach(MIMEText(text_content, "plain"))
            msg.attach(MIMEText(html_content, "html"))

            # Send email
            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)

            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    @staticmethod
    def _send_via_resend(
        to_email: str, agency_name: str, invite_token: str, inviter_name: str
    ) -> bool:
        """Send email using Resend service."""
        try:
            import resend

            resend.api_key = rx.get_env_var("RESEND_API_KEY")

            app_url = rx.get_env_var("APP_URL", "http://localhost:3000")
            accept_url = f"{app_url}/accept-invite/{invite_token}"

            html_content = f"""
            <h2>You've been invited to {agency_name}'s client portal</h2>
            <p>Hello,</p>
            <p>{inviter_name} has invited you to join their client portal on Clientnest.</p>
            <p>Click the link below to accept the invitation and set up your account:</p>
            <a href="{accept_url}" style="
                display: inline-block;
                padding: 12px 24px;
                background-color: #2563EB;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                font-weight: bold;
            ">Accept Invitation</a>
            <p>This invitation link will expire in 7 days.</p>
            """

            params = {
                "from": "Clientnest <invites@clientnest.app>",
                "to": [to_email],
                "subject": f"Invitation to join {agency_name}'s client portal",
                "html": html_content,
            }

            resend.Emails.send(params)
            return True

        except ImportError:
            print("Resend package not installed")
            return False
        except Exception as e:
            print(f"Failed to send via Resend: {e}")
            return False

    @staticmethod
    def send_notification_email(
        to_email: str, subject: str, message: str, project_name: Optional[str] = None
    ) -> bool:
        """Send notification email for project updates."""
        try:
            smtp_host = rx.get_env_var("SMTP_HOST")
            smtp_user = rx.get_env_var("SMTP_USER")

            if not smtp_host or not smtp_user:
                print("Email configuration incomplete - skipping notification email")
                return False

            # Create simple text email
            msg = MIMEMultipart()
            msg["Subject"] = subject
            msg["From"] = smtp_user
            msg["To"] = to_email

            body = message
            if project_name:
                body = f"Regarding project: {project_name}\n\n{message}"

            msg.attach(MIMEText(body, "plain"))

            # Send email
            smtp_port = int(rx.get_env_var("SMTP_PORT", "587"))
            smtp_pass = rx.get_env_var("SMTP_PASS")

            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_pass)
                server.send_message(msg)

            return True

        except Exception as e:
            print(f"Failed to send notification email: {e}")
            return False
