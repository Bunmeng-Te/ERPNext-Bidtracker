# Bid Tracker ERPNext Extension Module

This is a custom Frappe / ERPNext app scaffold for the university assignment.
It implements:
- Bid Record DocType
- Bid Cost Entry DocType
- Timesheet -> Bid link (created on install)
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

## Important
This package is designed to be a realistic working starter for a Frappe custom app, but you still need to:
1. install it inside your ERPNext bench
2. run migrate
3. verify fieldnames and permissions in your exact Frappe/ERPNext version
4. optionally create a Workflow from the included states if your course requires the GUI workflow object

## Suggested demo flow
1. Create an Opportunity.
2. Create a Bid Record linked to that Opportunity.
3. Add manual costs using Bid Cost Entry.
4. Add a Timesheet and link it to the Bid Record.
5. Open the Bid Record and click Recalculate P&L.
6. Show Total Bid Cost, Estimated Profit, and ROI Ratio.
7. Open the Bid P&L Summary report.
```
