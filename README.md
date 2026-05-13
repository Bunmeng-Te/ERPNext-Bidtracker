````md
# ERPNext BidTracker

ERPNext BidTracker is a custom ERPNext extension developed for pre-contract bid management, bid cost tracking, workflow approvals, and profitability analysis.

This project extends ERPNext Version 15 using the Frappe Framework and provides a centralized system for managing business development bid operations, labour cost tracking, financial reporting, and role-based access control (RBAC).

---

# Features

## Bid Management
- Create and manage Bid Records
- Link Opportunities to Bid Records
- Track bid lifecycle and workflow stages
- Support bid status transitions:
  - Draft
  - Qualifying
  - Active
  - Submitted
  - Won
  - Lost
  - Withdrawn

---

## Cost Tracking
- Track bid-related operational expenses
- Create manual Bid Cost Entries
- Integrate ERPNext Timesheets with Bid Records
- Automatically aggregate labour costs
- Calculate total bid costs dynamically

---

## Financial Reporting
- Pre-contract P&L reporting
- Bid profitability analysis
- ROI and win/loss tracking
- Aggregated dashboard metrics
- Bid PNL Summary Report

---

## Role-Based Access Control (RBAC)

Custom business roles:
- BD Team
- BD Manager
- Finance Reviewer
- Executive Viewer
- Super User
- System Manager

Permission management includes:
- Role Permissions Manager
- Workflow permissions
- Report and Page permissions

---

# Technology Stack

- ERPNext v15
- Frappe Framework v15
- Python 3.11
- MariaDB
- Redis
- Node.js
- Yarn
- Nginx
- Azure Virtual Machine

---

# Project Structure

```text
apps/bid_tracker/
├── bid_tracker/
│   ├── bid_management/
│   │   ├── doctype/
│   │   ├── report/
│   │   ├── public/
│   │   └── api.py
│   ├── fixtures/
│   ├── patches/
│   ├── hooks.py
│   └── install.py
````

---

# Installation

## Initialize Frappe Bench

```bash
bench init frappe-bench --frappe-branch version-15
```

---

## Install ERPNext

```bash
bench get-app erpnext --branch version-15

bench new-site mysite.localhost

bench --site mysite.localhost install-app erpnext
```

---

## Install BidTracker App

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

# Running Development Server

```bash
bench start
```

Access ERPNext:

```text
http://localhost:8000
```

---

# Production Deployment

Production deployment includes:

* Azure VM hosting
* Nginx reverse proxy
* HTTPS configuration
* ERPNext production setup
* Supervisor process management

Production URL:

```text
https://erpnext-bidtracker.com
```

---

# Contributors

* Bunmeng Te
* Rudra Pandey

---

# License

This project is developed for academic and demonstration purposes.

```
```
