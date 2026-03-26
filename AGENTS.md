# Clientnest — OpenCode Agent Context

You are building **Clientnest**, a white-label client portal SaaS.
Read this entire file before writing a single line of code.
Every decision about schema, state, routing, and patterns is already made here. Follow it exactly.

---

## Project Overview

**What it is:** A SaaS platform where freelancers and small agencies get a branded portal
to manage clients — project tracking, file sharing, messaging, and invoicing in one place.

**Core differentiator:** White-label on every paid plan starting at $19/month.
Competitor ManyRequests charges $399/month for white-label. That gap is the entire business.

**One-line pitch:** White-label client portal for solo consultants and small agencies —
at a price ManyRequests refuses to offer.

---

## Tech Stack

| Layer | Technology | Notes |
|---|---|---|
| Framework | Reflex (Python) | Full-stack Python, no JS |
| Database | SQLite via SQLAlchemy | Zero infra cost locally |
| Auth | Custom bcrypt + sessions | No external auth dependency |
| Payments | LemonSqueezy | Handles INR + USD, webhooks |
| File Storage | Local filesystem (v1) | uploads/ directory, gitignored |
| Email | SMTP / Resend free tier | Invites and notifications |
| Deployment | Railway (post first customer) | ~$7/month, not needed for dev |

---

## Absolute Rules — Never Break These

1. **All DB access inside State event handlers only.** Never query DB in component functions.
2. **Use `rx.cond` for all conditional rendering.** Never Python `if/else` in component return values.
3. **Use `on_load` in `rx.page` decorator for all data fetching** when a page loads.
4. **One State subclass per feature** — never one giant State class.
5. **Every DB query must include `agency_id` filter** — zero cross-agency data leakage ever.
6. **Never store plaintext passwords.** Always bcrypt with cost factor 12.
7. **File downloads served through authenticated backend route only.** Never expose raw file paths.
8. **LemonSqueezy webhook must validate HMAC signature** before any DB write.
9. **`UIState` must never import DB models.** It is pure UI logic only.
10.**- All State vars that need on_change must have explicit setter methods defined as `def set_varname(self, value: str)`. Never rely on  auto-generated setters — deprecated in Reflex 0.8.9.

---

## Reflex Patterns Reference

```python
# ✅ CORRECT — data fetching on page load
@rx.page(route="/dashboard", on_load=DashboardState.load_data)
def dashboard():
    return rx.box(...)

# ✅ CORRECT — conditional rendering
rx.cond(AuthState.is_logged_in, dashboard_view(), login_prompt())

# ✅ CORRECT — computed var
class ProjectState(rx.State):
    projects: list[dict] = []

    @rx.var
    def active_count(self) -> int:
        return len([p for p in self.projects if p["status"] == "in_progress"])

# ✅ CORRECT — all DB writes in event handlers
class ProjectState(rx.State):
    @rx.event
    def create_project(self, form_data: dict):
        with rx.session() as session:
            project = Project(**form_data, agency_id=self.agency_id)
            session.add(project)
            session.commit()

# ❌ WRONG — never do this
def project_card():
    projects = db.query(Project).all()  # NO — DB in component
    return rx.box(...)
```

---

## Database Schema

### Agency
```
id              Integer PK auto
name            String(120)
slug            String(80) UNIQUE          # url-safe e.g. "ravi-studio"
logo_url        String(300) nullable
brand_color     String(7) default "#2563EB"
custom_domain   String(200) nullable
plan            String(20) default "free"  # free | solo | agency | studio
subscription_id String(100) nullable       # LemonSqueezy subscription ID
subscription_status String(20) default "inactive"  # active | inactive | cancelled | past_due
created_at      DateTime auto
```

### User
```
id              Integer PK auto
agency_id       FK -> Agency
email           String(200) UNIQUE
password_hash   String(200)                # bcrypt only
role            String(20)                 # owner | member | client
name            String(120)
avatar_url      String(300) nullable
is_active       Boolean default True
last_login      DateTime nullable
created_at      DateTime auto
```

### Project
```
id              Integer PK auto
agency_id       FK -> Agency
client_id       FK -> User
title           String(200)
description     Text nullable
status          String(30)  # not_started | in_progress | review | completed | on_hold
due_date        Date nullable
created_at      DateTime auto
updated_at      DateTime auto
```

### Task
```
id              Integer PK auto
project_id      FK -> Project
title           String(300)
is_done         Boolean default False
sort_order      Integer default 0
created_at      DateTime auto
```

### Message
```
id              Integer PK auto
project_id      FK -> Project
sender_id       FK -> User
body            Text
is_read         Boolean default False
created_at      DateTime auto
```

### File
```
id              Integer PK auto
project_id      FK -> Project
uploaded_by     FK -> User
filename        String(300)                # original filename shown to user
stored_path     String(500)               # uploads/{agency_id}/{project_id}/{uuid}_{filename}
file_size       Integer                    # bytes
mime_type       String(100)
is_deleted      Boolean default False      # soft delete
created_at      DateTime auto
```

### Invoice
```
id                          Integer PK auto
agency_id                   FK -> Agency
client_id                   FK -> User
project_id                  FK -> Project nullable
amount                      Float
currency                    String(3) default "USD"   # USD | INR
status                      String(20) default "unpaid"  # unpaid | paid | overdue | cancelled
lemonsqueezy_checkout_url   String(500) nullable
paid_at                     DateTime nullable
due_date                    Date nullable
notes                       Text nullable
created_at                  DateTime auto
```

---

## State Architecture

| State Class | Key Vars | Responsibility |
|---|---|---|
| `AuthState` | user_id, agency_id, role, is_logged_in, current_user | Login, logout, session, role checks |
| `AgencyState` | agency, brand_color, logo_url, plan, is_subscribed | Profile, subscription gating, white-label |
| `ProjectState` | projects, current_project, tasks, project_filter | CRUD for projects and tasks |
| `MessageState` | messages, new_message, unread_count | Per-project messaging |
| `FileState` | files, upload_progress, uploading | File upload/download per project |
| `InvoiceState` | invoices, current_invoice, creating | Invoice creation and tracking |
| `UIState` | sidebar_open, active_tab, modal_open, toast_message | Pure UI state — no DB ever |

---

## Route Map

| Route | Auth | Role | Page Function |
|---|---|---|---|
| `/` | No | All | `index()` — landing page |
| `/login` | No | All | `login()` |
| `/signup` | No | All | `signup()` |
| `/dashboard` | Yes | owner, member | `dashboard()` |
| `/clients` | Yes | owner, member | `clients()` |
| `/clients/invite` | Yes | owner | `invite_client()` |
| `/projects` | Yes | owner, member | `projects()` |
| `/projects/[id]` | Yes | owner, member, client | `project_detail()` |
| `/projects/[id]/messages` | Yes | owner, member, client | `project_messages()` |
| `/projects/[id]/files` | Yes | owner, member, client | `project_files()` |
| `/invoices` | Yes | owner | `invoices()` |
| `/invoices/new` | Yes | owner | `new_invoice()` |
| `/settings` | Yes | owner | `settings()` |
| `/settings/billing` | Yes | owner | `billing()` |
| `/portal` | Yes | client | `client_portal()` |
| `/webhooks/lemonsqueezy` | No (API) | System | `webhook_ls()` |
| `/accept-invite/[token]` | No | All | `accept_invite()` |

---

## File Structure

```
clientnest/
├── clientnest/
│   ├── clientnest.py          # app entry — imports all pages, creates rx.App()
│   ├── models/
│   │   ├── __init__.py
│   │   ├── agency.py
│   │   ├── user.py
│   │   ├── project.py         # Project + Task models
│   │   ├── message.py
│   │   ├── file.py
│   │   └── invoice.py
│   ├── state/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── agency.py
│   │   ├── project.py
│   │   ├── message.py
│   │   ├── file.py
│   │   ├── invoice.py
│   │   └── ui.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── index.py
│   │   ├── auth.py            # login + signup
│   │   ├── dashboard.py
│   │   ├── projects.py
│   │   ├── messages.py
│   │   ├── files.py
│   │   ├── invoices.py
│   │   ├── settings.py
│   │   ├── portal.py          # client-facing view
│   │   └── webhooks.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── navbar.py          # sidebar navigation
│   │   ├── cards.py           # stat cards, project cards
│   │   ├── table.py           # reusable data table
│   │   └── badges.py          # status badges
│   ├── styles.py              # design tokens — colors, spacing, font sizes
│   ├── config.py              # env vars, LemonSqueezy plan mapping
│   └── email.py               # SMTP/Resend helpers
├── uploads/                   # local file storage (gitignored)
├── .env                       # LEMONSQUEEZY_API_KEY, WEBHOOK_SECRET, SMTP
├── requirements.txt
└── AGENTS.md                  # this file
```

---

## Feature Specs

### Auth Flows

**Signup:**
1. Form: Agency Name, Your Name, Email, Password
2. Create `Agency` with auto-generated slug (lowercase, hyphenated from name)
3. Create `User` with role=owner linked to agency
4. Set session in AuthState
5. Redirect to `/dashboard`

**Login:**
1. Email + password
2. `bcrypt.checkpw()` validation
3. Success: set AuthState, redirect to `/dashboard` (owner/member) or `/portal` (client)
4. Failure: inline error only — no redirect

**Client Invite:**
1. Agency owner enters client email
2. Generate UUID token, store with 7-day expiry
3. Send email with `/accept-invite/{token}`
4. Client sets name + password
5. Create User with role=client linked to agency
6. Redirect to `/portal`

---

### Project Status Values

| Value | Label | Badge Color |
|---|---|---|
| not_started | Not Started | Gray |
| in_progress | In Progress | Blue |
| review | In Review | Amber |
| completed | Completed | Green |
| on_hold | On Hold | Red |

---

### Plan Gating

| Feature | Free | Solo $19/mo | Agency $39/mo |
|---|---|---|---|
| Clients | 2 max | Unlimited | Unlimited |
| Projects | 3 max | Unlimited | Unlimited |
| Storage | 500MB | 5GB | 20GB |
| White-label | No | Yes | Yes |
| Custom domain | No | No | Yes |
| Team members | 1 | 1 | 5 |
| Invoicing | No | Yes | Yes |

**Gating pattern — implement in AgencyState:**
```python
@rx.var
def can_invite_client(self) -> bool:
    if self.plan == "free":
        return self.client_count < 2
    return True

@rx.var
def has_white_label(self) -> bool:
    return self.plan in ["solo", "agency", "studio"]
```

**UI rule:** Always show upgrade prompt when gated — never just hide the button.
```python
rx.cond(AgencyState.can_invite_client, invite_button(), upgrade_prompt())
```

---

### LemonSqueezy Webhook Handler

```
POST /webhooks/lemonsqueezy

1. Validate HMAC SHA256 signature using LEMONSQUEEZY_WEBHOOK_SECRET
2. Parse event type from payload
3. On subscription_created / subscription_updated:
   → Update agency.plan, agency.subscription_status, agency.subscription_id
4. On subscription_cancelled:
   → Set agency.subscription_status = "cancelled", agency.plan = "free"
5. On order_created (invoice payment):
   → Find Invoice by order metadata
   → Set invoice.status = "paid", invoice.paid_at = now()
6. Return HTTP 200
```

---

### Messaging

- Messages scoped per project — no global inbox in v1
- Thread: oldest at top, sender name + avatar initial + timestamp + body
- Mark all read on `on_load` of messages page
- Poll every 30 seconds using `rx.interval` — no WebSocket in v1
- Both agency members and assigned client can message on a project

---

### File Management

- Upload: `rx.upload`, any file type, max 50MB per file
- Store at: `uploads/{agency_id}/{project_id}/{uuid}_{original_filename}`
- Download: authenticated backend route only — 403 on direct path access
- Soft delete via `is_deleted` flag — never hard delete in v1

---

### Client Portal View

Client sees ONLY:
- Their own projects (where client_id = current user)
- Messages on their projects
- Files on their projects
- Their own invoices

Client CANNOT access:
- `/dashboard`
- `/clients`
- `/invoices` (agency list view)
- `/settings`
- Any other client's data

Portal is white-labeled with agency's logo, name, and brand_color.

---

## What is OUT OF SCOPE for v1

Do not build these. Do not suggest these. Defer all of these to v2:

- Real-time WebSocket chat
- Time tracking
- File preview (PDF/image viewer) — download only
- Mobile app
- Multi-currency beyond USD and INR
- AI features
- Zapier or API integrations
- Team permissions beyond owner/member/client

---

## Environment Variables (.env)

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

---

## Current Build Phase

**WEEK 1 — Foundation** ✅ COMPLETED
**WEEK 2 — Core CRUD** ✅ COMPLETED

---

**WEEK 1 — Foundation**

Tasks for this session:
1. Run `reflex init` in the `clientnest/` directory
2. Create all files in the structure above (empty `__init__.py` where needed)
3. Create all 7 SQLAlchemy models exactly as specified in the schema section
4. Create `AuthState` in `state/auth.py` with: user_id, agency_id, role, is_logged_in vars
5. Create `signup()` page and `login()` page in `pages/auth.py`
6. Wire signup form → create Agency + User → set AuthState → redirect to `/dashboard`
7. Wire login form → validate → set AuthState → redirect based on role
8. Create `dashboard()` page skeleton (just the layout, no data yet)
9. Confirm `reflex run` starts with no errors

Do not move to Week 2 tasks until all Week 1 tasks pass `reflex run` cleanly.

**WEEK 2 — Core CRUD** ← CURRENT WEEK

Tasks for this session:
1. Create `ProjectState` in `state/project.py` with vars: projects, current_project, tasks, project_filter
2. Create project list page at `/projects` — table view with columns: Project Name, Client, Status, Due Date, Last Updated, Actions
3. Add status filter tabs on project list: All / Active / Review / Completed
4. Create project detail page at `/projects/[id]` — title, client name, status dropdown, due date, progress bar
5. Add task checklist to project detail — add task inline, check/uncheck, delete, all live via State
6. Create client invite flow — `/clients/invite` page, generate UUID token, store with 7-day expiry, send invite email
7. Create client list page at `/clients` — table showing all clients with name, email, projects count, last active
8. Wire "Create Project" button on dashboard to open inline form: Title, Client dropdown, Description, Due Date
9. Confirm `reflex run` starts with no errors after all above

Do not move to Week 3 tasks until all Week 2 tasks pass `reflex run` cleanly.

**WEEK 3 — Communication** ← CURRENT WEEK

Tasks for this session:
1. Create `MessageState` in `state/message.py` with vars: messages, new_message, unread_count
2. Create per-project messaging page at `/projects/[id]/messages` — thread view oldest at top, sender name + initial + timestamp + body
3. Add text input at bottom of messages page, Send button, Enter key to send
4. Mark all messages as read on on_load of messages page
5. Add rx.interval polling every 30 seconds to refresh messages — no WebSocket
6. Add unread count badge on project cards and sidebar
7. Create `FileState` in `state/file.py` with vars: files, upload_progress, uploading
8. Create file manager page at `/projects/[id]/files` — rx.upload, any file type, max 50MB
9. Store uploaded files at: uploads/{agency_id}/{project_id}/{uuid}_{original_filename}
10. File list shows: filename, uploader name, file size, upload date, download button
11. Download served through authenticated backend route — 403 on direct path access
12. Soft delete via is_deleted flag on File model
13. Confirm `reflex run` starts with no errors after all above

**WEEK 3 — Communication** ✅ COMPLETED

**WEEK 4 — Invoicing & Polish** ✅ COMPLETED

Tasks for this session:
1. Create `InvoiceState` in `state/invoice.py` with vars: invoices, current_invoice, creating
2. Create invoice list page at `/invoices` — table view with columns: Invoice #, Client, Amount, Status, Due Date, Actions
3. Create new invoice page at `/invoices/new` — form with: Client dropdown, Project dropdown (optional), Amount, Currency (USD/INR), Due Date, Notes
4. Generate LemonSqueezy checkout URLs for invoice payments
5. Create billing page at `/settings/billing` — show current plan, upgrade buttons for Solo/Agency plans
6. Add white-label settings to `/settings` — agency name, logo upload, brand color picker
7. Implement plan gating throughout the app using AgencyState computed vars
8. Add client portal view at `/portal` — projects, messages, files scoped to current user only
9. Create LemonSqueezy webhook handler at `/webhooks/lemonsqueezy` — validate HMAC, update subscriptions, mark invoices paid
10. Confirm `reflex run` starts with no errors after all above

Do not move to Week 5 tasks until all Week 4 tasks pass `reflex run` cleanly.

**WEEK 5 — Polish & Launch Preparation** ✅ COMPLETED

Tasks completed:
1. ✅ Implement email integration for client invites and notifications
2. ✅ Complete file upload/download functionality with storage quotas  
3. ✅ Add white-label customization foundation (brand color and logo methods)
4. ✅ Implement comprehensive testing suite
5. ✅ Prepare for deployment (Railway + Docker configuration)
6. ✅ Add monitoring and error logging
7. ✅ Conduct security audit of authentication and payment flows
8. ✅ Confirm `reflex run` starts with no errors

