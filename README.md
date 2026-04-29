# 🚀 Clientnest — White-Label Client Portal SaaS

<div align="center">

**The $19/month alternative to $399/month ManyRequests**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Reflex](https://img.shields.io/badge/Reflex-0.8+-green.svg)](https://reflex.dev/)
[![Tests](https://img.shields.io/badge/tests-35%2F35%20passing-brightgreen.svg)](https://github.com/clientnest/clientnest)

**Your clients see YOUR brand, not ours.**

Fully branded client portal for solo consultants and small agencies — project tracking, file sharing, messaging, and invoicing in one place.

[**Get Started Free**](#-getting-started) • [**View Demo**](#-features) • [**Read Docs**](#-documentation)

</div>

---

## 🎯 Why Clientnest?

Stop paying **$399/month** for white-label. Get the same features for **$19/month**.

| Feature | ManyRequests | Clientnest | **You Save** |
|---|---|---|---|
| **White-label** | $399/mo | **$19/mo** | **$380/mo (95%)** |
| **Client portal** | ✅ | ✅ | — |
| **Project tracking** | ✅ | ✅ | — |
| **Invoicing** | ✅ | ✅ | — |
| **File sharing** | ✅ | ✅ | — |
| **Messaging** | ✅ | ✅ | — |
| **Self-hostable** | ❌ | ✅ | — |
| **Free trial** | ❌ | ✅ | — |

**That's $4,560 per year in savings.** Enough to hire a part-time VA or invest in marketing.

---

## 💎 Core Features

### 🎨 **White-Label Everything**
- **Custom logo** — Upload your brand logo
- **Brand colors** — Match your brand identity
- **Custom domain** — Use your own domain (Agency plan)
- **Zero Clientnest branding** — Your clients see only your brand

### 📊 **Project Management**
- **Project tracking** — Create and manage projects effortlessly
- **Task checklists** — Break down projects into actionable tasks
- **Progress bars** — Visual progress tracking at a glance
- **Status management** — Track project status (Not Started → In Progress → Review → Completed)
- **Due dates** — Never miss a deadline again

### 💬 **Client Communication**
- **Per-project messaging** — Keep conversations organized by project
- **Real-time updates** — Messages refresh every 30 seconds
- **Unread badges** — Never miss an important message
- **Threaded discussions** — Clean, organized communication history

### 📁 **File Management**
- **Drag-drop uploads** — Upload files intuitively
- **Secure storage** — Files stored securely with access controls
- **Download protection** — Authenticated downloads prevent unauthorized access
- **Storage quotas** — 500MB (Free) → 5GB (Solo) → 20GB (Agency)
- **Soft delete** — Recover accidentally deleted files

### 💰 **Invoicing & Payments**
- **Easy invoicing** — Create professional invoices in seconds
- **Multiple currencies** — Support for USD and INR
- **Payment tracking** — Track invoice status (Unpaid → Paid → Overdue)
- **LemonSqueezy integration** — Seamless payment processing
- **Automated reminders** — Never forget to follow up on payments

### 🔐 **Enterprise Security**
- **Secure authentication** — bcrypt password hashing
- **CSRF protection** — Protect against cross-site request forgery
- **Rate limiting** — Prevent abuse with intelligent rate limiting
- **Session management** — 24-hour session timeout
- **Account lockout** — 5 failed attempts = 30-minute lockout
- **Audit logging** — Comprehensive security event tracking

---

## 💰 Simple, Transparent Pricing

### 🆓 **Free** — $0/month
Perfect for getting started
- ✅ **2 clients** — Test with real clients
- ✅ **3 projects** — Manage small workloads
- ✅ **500MB storage** — Enough for essential files
- ❌ No white-label
- ❌ No invoicing

[**Start Free**](#-getting-started)

---

### 🚀 **Solo** — $19/month
For individual freelancers
- ✅ **Unlimited clients** — Scale without limits
- ✅ **Unlimited projects** — Manage as many projects as you need
- ✅ **5GB storage** — Plenty for most freelancers
- ✅ **White-label** — Your brand, your way
- ✅ **Invoicing** — Get paid faster
- ✅ **1 team member** — Just you

[**Get Started**](#-getting-started)

---

### 🏢 **Agency** — $39/month
For growing agencies
- ✅ **Everything in Solo**
- ✅ **20GB storage** — Handle larger projects
- ✅ **5 team members** — Collaborate with your team
- ✅ **Custom domain** — Use your own domain
- ✅ **Priority support** — Get help when you need it

[**Get Started**](#-getting-startable)

---

## 🎯 How It Works

### 1. **Sign Up Free** → 2 minutes
Create your account with your agency name and email. No credit card required.

### 2. **Invite Clients** → 5 minutes
Send invites to your clients. They set their password and get instant access.

### 3. **Create Projects** → 10 minutes
Set up projects, add tasks, and start collaborating immediately.

### 4. **Get Paid** → Automatic
Send invoices and get paid through LemonSqueezy. Track everything in one place.

---

## 🛠️ Tech Stack

Built for performance, security, and simplicity.

| Layer | Technology | Why |
|---|---|---|
| **Framework** | [Reflex](https://reflex.dev/) (Python) | Full-stack Python, no JavaScript required |
| **Database** | [SQLite](https://www.sqlite.org/) via [SQLAlchemy](https://www.sqlalchemy.org/) | Zero infrastructure cost, easy to migrate to PostgreSQL |
| **Authentication** | Custom bcrypt + sessions | No external dependencies, full control |
| **Payments** | [LemonSqueezy](https://www.lemonsqueezy.com/) | Handles INR + USD, excellent webhook support |
| **File Storage** | Local filesystem (v1) | Simple, cost-effective, easy to migrate to S3 |
| **Email** | SMTP / [Resend](https://resend.com/) free tier | Reliable email delivery for invites and notifications |
| **Deployment** | [Railway](https://railway.app/) | Simple deployment, ~$7/month |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git (for cloning)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/clientnest.git
cd clientnest
```

**2. Create a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

**5. Initialize the database**
```bash
reflex init
reflex db init
```

**6. Run the application**
```bash
reflex run
```

**7. Access your dashboard**
Open your browser and navigate to:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000

---

## 📁 Project Structure

```
clientnest/
├── clientnest/
│   ├── clientnest.py          # App entry point — routes + FastAPI webhook
│   ├── webhook_api.py         # LemonSqueezy webhook handler (HMAC validated)
│   ├── models/                # SQLAlchemy models
│   │   ├── agency.py          # Agency model
│   │   ├── user.py            # User model
│   │   ├── project.py         # Project + Task models
│   │   ├── message.py         # Message model
│   │   ├── file.py            # File model
│   │   ├── invoice.py         # Invoice model
│   │   └── client_invite.py   # Client invite model
│   ├── state/                 # Reflex State classes (one per feature)
│   │   ├── auth.py            # Authentication state
│   │   ├── agency.py          # Agency management state
│   │   ├── project.py         # Project + task state
│   │   ├── message.py         # Messaging state
│   │   ├── file.py            # File upload/download state
│   │   ├── invoice.py         # Invoice management state
│   │   └── ui.py              # Pure UI state (sidebar, modals, toasts)
│   ├── pages/                 # Page components
│   │   ├── index.py           # Landing page
│   │   ├── auth.py            # Login + signup pages
│   │   ├── dashboard.py       # Dashboard page
│   │   ├── projects.py        # Project list + detail pages
│   │   ├── messages.py        # Messaging page
│   │   ├── files.py           # File management page
│   │   ├── invoices.py        # Invoice list + creation pages
│   │   ├── settings.py        # Settings pages
│   │   ├── portal.py          # Client portal page
│   │   └── clients.py         # Client management page
│   ├── components/            # Reusable UI components
│   │   ├── navbar.py          # Sidebar navigation
│   │   ├── cards.py           # Stat cards, project cards
│   │   ├── table.py           # Reusable data table
│   │   └── badges.py          # Status badges
│   ├── email.py               # SMTP/Resend helpers
│   ├── styles.py              # Design tokens
│   ├── config.py              # Environment configuration
│   ├── csrf.py                # CSRF protection
│   ├── rate_limiter.py        # Rate limiting utilities
│   ├── validators.py          # Input validation
│   ├── error_handler.py      # Error handling
│   ├── encryption.py          # Data encryption utilities
│   ├── security_logger.py    # Security event logging
│   └── middleware.py          # Security headers middleware
├── tests/                     # pytest suite (35 tests)
│   ├── test_agency.py         # Agency model tests
│   ├── test_auth.py           # Authentication tests
│   ├── test_files.py          # File model tests
│   ├── test_invoice.py        # Invoice model tests
│   ├── test_message.py        # Message model tests
│   ├── test_project.py        # Project + Task model tests
│   ├── test_security.py       # Security tests
│   └── test_webhook.py        # Webhook integration tests
├── scripts/                   # Utility scripts
│   ├── backup_database.sh     # Database backup script
│   ├── backup_files.sh        # File storage backup script
│   ├── backup_config.sh       # Configuration backup script
│   └── scan_dependencies.py   # Dependency vulnerability scanner
├── uploads/                   # File storage (gitignored)
├── logs/                      # Application logs
├── .env                       # Environment variables (gitignored)
├── .env.example               # Environment variables template
├── requirements.txt            # Python dependencies
├── requirements-security.txt  # Security tools dependencies
├── Dockerfile                 # Production container
├── railway.toml               # Railway deployment config
├── rxconfig.py                # Reflex configuration
├── README.md                  # This file
├── BACKUP_RECOVERY.md         # Backup and recovery procedures
├── ARCHITECTURE_REVIEW.md     # Backend architecture review
├── SECURITY.md                # Security documentation
└── AGENTS.md                  # Development guide
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```bash
# Application
APP_URL=http://localhost:3000
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=sqlite:///clientnest.db

# LemonSqueezy
LEMONSQUEEZY_API_KEY=your-lemonsqueezy-api-key
LEMONSQUEEZY_WEBHOOK_SECRET=your-webhook-secret
LEMONSQUEEZY_SOLO_VARIANT_ID=your-solo-variant-id
LEMONSQUEEZY_AGENCY_VARIANT_ID=your-agency-variant-id

# Email (SMTP/Resend)
SMTP_HOST=smtp.resend.com
SMTP_PORT=587
SMTP_USER=your-smtp-username
SMTP_PASS=your-smtp-password

# File Storage
UPLOAD_DIR=uploads
MAX_FILE_SIZE=52428800  # 50MB in bytes
```

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
pytest tests/ -v
```

**Test Coverage:**
- ✅ 35/35 tests passing
- ✅ Agency model functionality
- ✅ User authentication and password hashing
- ✅ File upload/download with soft delete
- ✅ Invoice creation and status transitions
- ✅ Message creation and read tracking
- ✅ Project and task management
- ✅ Security features (IDOR protection, access control, rate limiting)
- ✅ Webhook integration (HMAC validation, event handling)

---

## 🚀 Deployment

### Railway Deployment

**1. Install Railway CLI**
```bash
npm install -g @railway/cli
```

**2. Login to Railway**
```bash
railway login
```

**3. Initialize project**
```bash
railway init
```

**4. Configure environment variables**
```bash
railway variables set LEMONSQUEEZY_API_KEY=your-key
railway variables set LEMONSQUEEZY_WEBHOOK_SECRET=your-secret
# ... set other variables
```

**5. Deploy**
```bash
railway up
```

**Cost:** ~$7/month for basic Railway deployment.

### Docker Deployment

**1. Build the image**
```bash
docker build -t clientnest .
```

**2. Run the container**
```bash
docker run -p 3000:3000 -p 8000:8000 \
  -e LEMONSQUEEZY_API_KEY=your-key \
  -e LEMONSQUEEZY_WEBHOOK_SECRET=your-secret \
  clientnest
```

---

## 📚 Documentation

- **[Getting Started Guide](#-getting-started)** — Quick start instructions
- **[API Documentation](docs/api.md)** — Webhook API reference
- **[Security Guide](SECURITY.md)** — Security best practices
- **[Backup & Recovery](BACKUP_RECOVERY.md)** — Disaster recovery procedures
- **[Architecture Review](ARCHITECTURE_REVIEW.md)** — Backend architecture overview

---

## 🎨 Features in Detail

### 🎯 **Project Dashboard**
- **Stat cards** — Quick overview of clients, projects, and invoices
- **Recent activity** — See what's happening across all projects
- **Quick actions** — Create projects, invite clients, send invoices

### 📋 **Project Management**
- **Project list** — Filter by status (All, Active, Review, Completed)
- **Project detail** — View project info, client, status, due date
- **Task checklist** — Add, complete, and delete tasks
- **Progress tracking** — Visual progress bars show completion

### 💬 **Messaging**
- **Per-project threads** — Keep conversations organized
- **Real-time updates** — Messages refresh every 30 seconds
- **Unread badges** — See unread message count
- **Sender identification** — See who sent each message

### 📁 **File Management**
- **Drag-drop upload** — Intuitive file upload interface
- **File list** — See all files with metadata
- **Download protection** — Authenticated downloads only
- **Storage tracking** — See your storage usage

### 💰 **Invoicing**
- **Invoice creation** — Create invoices with client, project, amount
- **Currency support** — USD and INR
- **Payment tracking** — Track unpaid, paid, and overdue invoices
- **LemonSqueezy integration** — Seamless payment processing

### ⚙️ **Settings**
- **White-label customization** — Logo, brand colors
- **Billing management** — View plan, upgrade, cancel
- **Account settings** — Update profile, change password

### 🌐 **Client Portal**
- **Scoped views** — Clients see only their projects
- **White-branded** — Your logo and colors
- **Simple navigation** — Easy-to-use interface

---

## 🔒 Security

Clientnest takes security seriously:

- **✅ Authentication** — bcrypt password hashing with cost factor 12
- **✅ Authorization** — Role-based access control (owner, member, client)
- **✅ CSRF Protection** — Token-based CSRF protection on all forms
- **✅ Session Management** — 24-hour session timeout with activity tracking
- **✅ Rate Limiting** — Token bucket algorithm (100 req/min for webhooks)
- **✅ Input Validation** — Comprehensive validation on all user inputs
- **✅ File Upload Security** — MIME type validation, extension whitelist, size limits
- **✅ Download Protection** — Authenticated routes prevent unauthorized access
- **✅ Security Logging** — 30+ security event types with structured logging
- **✅ Data Encryption** — AES-256 encryption for sensitive fields
- **✅ Security Headers** — OWASP recommended headers (CSP, HSTS, X-Frame-Options)

**Security Audit:** All Critical, High, and Medium vulnerabilities fixed. Launch-ready security posture.

---

## 🚫 What's Not Included (v1)

These features are intentionally deferred to v2:

- ❌ Real-time WebSocket chat (30-second polling is sufficient for MVP)
- ❌ Time tracking functionality
- ❌ File previews (PDF/image viewer) — download only
- ❌ Mobile app (web-first approach)
- ❌ Multi-currency beyond USD and INR
- ❌ AI features
- ❌ Zapier or API integrations
- ❌ Advanced team permissions beyond owner/member/client

**Focus:** Core client portal functionality with white-label branding.

---

## 🤝 Contributing

This is a solo indie dev project, but contributions are welcome!

**How to Contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Development Guidelines:**
- Follow the existing code style
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[Reflex](https://reflex.dev/)** — Amazing full-stack Python framework
- **[LemonSqueezy](https://www.lemonsqueezy.com/)** — Excellent payment infrastructure
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — Powerful ORM for Python
- **[Railway](https://railway.app/)** — Simple deployment platform

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/clientnest/issues)
- **Email:** support@clientnest.com
- **Twitter:** [@clientnest](https://twitter.com/clientnest)

---

## 🎯 Roadmap

### v1.0 (Current) ✅
- ✅ Core client portal functionality
- ✅ White-label branding
- ✅ Project management
- ✅ File sharing
- ✅ Messaging
- ✅ Invoicing
- ✅ Security hardening

### v1.1 (Next Quarter)
- 🔄 Onboarding tour
- 🔄 Dashboard empty states
- 🔄 Enhanced file upload progress
- 🔄 Mobile responsiveness improvements

### v2.0 (Future)
- 📅 Time tracking
- 💬 Real-time WebSocket chat
- 📱 Mobile app
- 🌍 Multi-currency support
- 🔌 Zapier integrations
- 🤖 AI-powered features

---

<div align="center">

**Built with ❤️ for solo consultants and small agencies**

[**Get Started Free**](#-getting-started) • [**View Demo**](#-features) • [**Star on GitHub**](https://github.com/yourusername/clientnest)

**Stop paying $399/month. Start paying $19/month.**

[![Clientnest](https://img.shields.io/badge/Clientnest-White--Label%20Client%20Portal-blue.svg)](https://github.com/yourusername/clientnest)

</div>
