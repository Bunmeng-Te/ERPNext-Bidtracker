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