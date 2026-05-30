<div align="center">

# ERPNext BidTracker

Custom ERPNext extension module for pre-contract bid management, bid cost tracking, workflow approvals, profitability analysis, ROI reporting, and role-based operational management.

Built on top of ERPNext v15 and the Frappe Framework.

</div>

---

## Overview

ERPNext BidTracker is a custom Frappe application built on ERPNext to support pre-contract bid management for Prompcorp Facilities Management.

The system centralizes bid records, CRM opportunities, staff timesheets, bid-related expenses, workflow approvals, profitability analysis, ROI calculations, reporting, and role-based access control within a single ERP platform.

It extends ERPNext with custom DocTypes, workflow automation, dashboard analytics, script reports, notification logic, and controlled user access for business development, finance review, and executive visibility.

The application is designed as a centralized multi-user web platform accessible through both desktop and mobile browsers.

---

## Core Features

### Bid Record Management

- Create and manage Bid Records
- Link Bid Records with ERPNext CRM Opportunities
- Track bid status, assigned teams, sectors, and bid ownership
- Manage bid lifecycle stages from draft to final outcome
- Support multiple bid statuses:
  - Draft
  - Qualifying
  - Active
  - Submitted
  - Won
  - Lost
  - Withdrawn

---

### Timesheet Integration

- Link ERPNext Timesheets to Bid Records
- Record labour hours against specific bids
- Automatically aggregate labour hours and labour costs
- Support bid-level visibility of staff time contribution

---

### Bid Cost Tracking

- Create and manage manual Bid Cost Entries
- Track travel, printing, subcontractor, material, and administrative expenses
- Record non-timesheet bid-related costs
- Aggregate manual costs with timesheet labour costs
- Calculate total bid cost dynamically

---

### Financial Reporting

- Generate pre-contract Profit & Loss analysis
- Calculate ROI ratio and profitability metrics
- Track estimated contract value and estimated profit
- Support management decision-making before bid submission
- Provide dashboard metrics and bid performance visibility
- Include Bid PnL Summary Script Report

---

### Workflow Automation

- Manage multi-stage bid approval workflows
- Control bid status transitions through ERPNext Workflow
- Support role-based workflow actions
- Trigger notification-driven approval and review flow
- Improve visibility of bid progress and decision points

---

### Role-Based Access Control (RBAC)

Custom business roles:

- BD Team
- BD Manager
- Finance Reviewer
- Executive Viewer

Administrative and testing roles include:

- Super User
- System Manager

Permission configuration includes:

- CRUD permissions
- Workflow permissions
- Report permissions
- Page permissions
- Dashboard visibility controls
- Sensitive financial information protection

---

### ERPNext Integration

The system integrates with ERPNext modules and platform features including:

- CRM Opportunities
- Timesheets
- Projects
- Users and Roles
- Workflow Engine
- Email Notifications
- Dashboards
- Script Reports

---

## Technology Stack

### Backend

- ERPNext v15
- Frappe Framework v15
- Python 3.11
- MariaDB
- Redis

### Frontend

- JavaScript
- Frappe Desk UI

### Infrastructure

- Node.js
- Yarn
- Nginx
- Supervisor
- Azure Virtual Machine
- Cloudflare DNS & HTTPS

---

## Project Structure

```
frappe-bench/
├── apps/
│   ├── frappe/         <--- Core Frappe framework
│   │   └── ...
│   │
│   ├── erpnext/        <--- Core ERPNext application
│   │   └── ...
│   │
│   └── bid_tracker/    <--- Current repository (Custom ERPNext extension for this project)
│       ├── README.md
│       ├── pyproject.toml
│       ├── setup.py
│       └── bid_tracker/
│           ├── bid_management/
│           │   ├── api.py
│           │   ├── config/
│           │   │   └── desktop.py
│           │   ├── doctype/
│           │   │   ├── bid_record/
│           │   │   │   ├── bid_record.json
│           │   │   │   └── bid_record.py
│           │   │   └── bid_cost_entry/
│           │   │       ├── bid_cost_entry.json
│           │   │       └── bid_cost_entry.py
│           │   ├── public/
│           │   │   └── js/
│           │   │       └── bid_record.js
│           │   └── report/
│           │       └── bid_pnl_summary/
│           │           ├── bid_pnl_summary.json
│           │           └── bid_pnl_summary.py
│           │
│           ├── fixtures/
│           │   ├── dashboard.json
│           │   ├── dashboard_chart.json
│           │   ├── notification.json
│           │   ├── number_card.json
│           │   ├── role.json
│           │   ├── workflow.json
│           │   ├── workflow_action_master.json
│           │   └── workflow_state.json
│           │
│           ├── patches/
│           │   └── v1_0/
│           │       ├── add_timesheet_bid_record.py
│           │       └── backfill_dashboard_metrics.py
│           │
│           ├── hooks.py
│           ├── install.py
│           ├── modules.txt
│           └── patches.txt
│
├── config/
├── env/
├── logs/
├── sites/
├── Procfile
└── patches.txt
```

---

## Installation

### Initialize Frappe Bench

```bash
bench init frappe-bench --frappe-branch version-15
```

---

### Install ERPNext

```bash
bench get-app erpnext --branch version-15

bench new-site mysite.localhost

bench --site mysite.localhost install-app erpnext
```

---

### Install ERPNext BidTracker

```bash
cd apps

git clone https://github.com/Bunmeng-Te/ERPNext-Bidtracker.git bid_tracker

cd ..

bench setup requirements

bench --site mysite.localhost install-app bid_tracker

bench migrate

bench build
```

---

## Running Development Environment

Start development server:

```bash
bench start
```

Access ERPNext locally:

```text
http://localhost:8000
```

---

## Production Deployment

The production environment was deployed using:

- Azure Virtual Machine
- Nginx reverse proxy
- HTTPS configuration
- Cloudflare DNS integration
- Supervisor process management
- Redis runtime services
- SocketIO real-time services

Production URL:

```text
https://erpnext-bidtracker.com
```

---

## Production Runtime Architecture

```text
Cloudflare
    ↓
Nginx Reverse Proxy
    ↓
Supervisor-managed ERPNext Services
    ├── Redis Cache
    ├── Redis Queue
    ├── Web Service
    ├── SocketIO
    ├── Workers
    └── Scheduler
    ↓
MariaDB
```

---

## Deployment Workflow

After pulling latest changes from GitHub:

```bash
cd ~/frappe-bench/apps/bid_tracker

git pull origin main

cd ~/frappe-bench

bench migrate

bench build --production

sudo supervisorctl restart all
```

---

## Team

- Bunmeng Te — Technical Lead, Full Stack Developer, Infrastructure Engineer & DevSecOps
- Rudra Pandey — Development Support & QA Tester
- Hai — Risk Analyst & QA Tester
- Zayah — Security Analyst & Prototyping
- Andy Le — Research & Documentation

---

## Academic Context

This project was developed as part of an academic ERP implementation and software engineering project.

The production deployment includes:
- centralized multi-user access
- HTTPS domain configuration
- cloud-hosted ERPNext runtime
- real-time synchronization
- workflow-driven operational management

---

## License

This project is developed for academic, educational, and demonstration purposes.