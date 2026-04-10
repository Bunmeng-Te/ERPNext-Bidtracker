# Bid Tracker ERPNext Extension Module

This is a custom Frappe / ERPNext app scaffold for the university assignment.

It implements:

- Bid Record DocType
- Bid Cost Entry DocType
- Timesheet to Bid link (created on install)
- Pre-contract P&L and ROI calculation
- Recalculate button on Bid Record
- Query Report: Bid P&L Summary

## Main files

- `bid_tracker/bid_tracker/doctype/bid_record/` - main bid record
- `bid_tracker/bid_tracker/doctype/bid_cost_entry/` - manual costs
- `bid_tracker/api.py` - whitelisted server methods
- `bid_tracker/install.py` - installs custom fields and property setters
- `bid_tracker/bid_tracker/report/bid_pnl_summary/` - query report

## Install (inside bench)

```bash
bench new-app bid_tracker
# replace generated files with this package
bench --site yoursite install-app bid_tracker
bench --site yoursite migrate
```
