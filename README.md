# Clientnest - White-label Client Portal SaaS

A SaaS platform where freelancers and small agencies get a branded portal to manage clients — project tracking, file sharing, messaging, and invoicing in one place.

## 🚀 Core Differentiator

**White-label on every paid plan starting at $19/month** - Competitor ManyRequests charges $399/month for white-label. That gap is the entire business.

**One-line pitch:** White-label client portal for solo consultants and small agencies — at a price ManyRequests refuses to offer.

## 🛠️ Tech Stack

- **Framework**: Reflex (Python) - Full-stack Python, no JS
- **Database**: SQLite via SQLAlchemy - Zero infra cost locally
- **Auth**: Custom bcrypt + sessions - No external auth dependency
- **Payments**: LemonSqueezy - Handles INR + USD, webhooks
- **File Storage**: Local filesystem (v1) - uploads/ directory, gitignored
- **Email**: SMTP / Resend free tier - Invites and notifications
- **Deployment**: Railway (post first customer) - ~$7/month

## 📋 Current Status

**WEEK 1 — Foundation** ✅ COMPLETED
**WEEK 2 — Core CRUD** ✅ COMPLETED  
**WEEK 3 — Communication** ✅ COMPLETED
**WEEK 4 — Invoicing & Polish** ✅ COMPLETED

### Week 3 Completed Features:

- ✅ **MessageState** with messages, new_message, unread_count vars
- ✅ **FileState** with files, upload_progress, uploading vars
- ✅ Per-project messaging page at `/projects/[id]/messages`
- ✅ Text input + Send button for messages with Enter key support
- ✅ Mark all messages as read on page load
- ✅ File manager page at `/projects/[id]/files`
- ✅ File upload with rx.upload (max 50MB)
- ✅ Authenticated download backend route
- ✅ Soft delete via is_deleted flag
- ✅ Reflex app compiles without errors

### Week 4 Completed Features:

- ✅ **InvoiceState** with invoices, current_invoice, creating vars
- ✅ Invoice list page at `/invoices` with data table
- ✅ New invoice creation page at `/invoices/new`
- ✅ LemonSqueezy webhook placeholder implementation
- ✅ Billing page at `/settings/billing` with upgrade options
- ✅ Client portal scoping at `/portal` (client-specific views)
- ✅ Agency plan gating with computed vars
- ✅ All import issues fixed and app compiles cleanly

### Week 5 Completed Features:

- ✅ **Email Integration** - SMTP/Resend for client invites
- ✅ **Storage Quotas** - Plan-based file storage limits
- ✅ **Testing Suite** - Comprehensive test framework with pytest
- ✅ **Deployment Config** - Railway + Docker setup
- ✅ **Monitoring** - Logging and health checks
- ✅ **Security Audit** - Full security review completed (score: 8/10)
- ✅ **Security Hardening** - Rate limiting, password strength enforcement
- ✅ **White-label UI** - Complete branding with logo upload functionality

## 🚀 Getting Started

1. **Install dependencies**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Initialize database**:
   ```bash
   reflex init
   reflex db init
   reflex db migrate
   ```

3. **Run the app**:
   ```bash
   reflex run
   ```

## 📁 Project Structure

```
clientnest/
├── clientnest/
│   ├── clientnest.py          # app entry
│   ├── models/                # SQLAlchemy models
│   ├── state/                 # Reflex State classes
│   ├── pages/                 # Page components
│   ├── components/            # Reusable components
│   ├── styles.py              # Design tokens
│   └── config.py              # Environment variables
├── uploads/                   # File storage (gitignored)
├── .env                       # Configuration
└── AGENTS.md                  # Development guide
```

## 🔑 Environment Variables

Create a `.env` file with:

```
LEMONSQUEEZY_API_KEY=
LEMONSQUEEZY_WEBHOOK_SECRET=
LEMONSQUEEZY_SOLO_VARIANT_ID=
LEMONSQUEEZY_AGENCY_VARIANT_ID=
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=
APP_URL=http://localhost:3000
```

## 📋 Roadmap

### Week 4 — Invoicing & Polish
- [ ] InvoiceState with invoice management
- [ ] Invoice list and creation pages
- [ ] LemonSqueezy checkout integration
- [ ] Billing and white-label settings
- [ ] Client portal view
- [ ] Webhook handler

### Out of Scope for v1
- Real-time WebSocket chat
- Time tracking  
- File previews
- Mobile app
- Multi-currency beyond USD/INR
- AI features
- API integrations

## 📄 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

This is a solo indie dev project. For bug reports or feature suggestions, please open an issue.