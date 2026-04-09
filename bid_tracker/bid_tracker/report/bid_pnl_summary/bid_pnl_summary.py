import frappe


def execute(filters=None):
    columns = [
        {"fieldname": "name", "label": "Bid ID", "fieldtype": "Link", "options": "Bid Record", "width": 140},
        {"fieldname": "bid_title", "label": "Bid Title", "fieldtype": "Data", "width": 180},
        {"fieldname": "opportunity", "label": "Opportunity", "fieldtype": "Link", "options": "Opportunity", "width": 140},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 110},
        {"fieldname": "estimated_contract_value", "label": "Estimated Contract Value", "fieldtype": "Currency", "width": 160},
        {"fieldname": "total_timesheet_cost", "label": "Timesheet Cost", "fieldtype": "Currency", "width": 130},
        {"fieldname": "total_manual_cost", "label": "Manual Cost", "fieldtype": "Currency", "width": 120},
        {"fieldname": "total_bid_cost", "label": "Total Bid Cost", "fieldtype": "Currency", "width": 130},
        {"fieldname": "estimated_profit", "label": "Estimated Profit", "fieldtype": "Currency", "width": 130},
        {"fieldname": "roi_ratio", "label": "ROI Ratio", "fieldtype": "Percent", "width": 100},
    ]

    data = frappe.db.get_all(
        "Bid Record",
        fields=[
            "name",
            "bid_title",
            "opportunity",
            "status",
            "estimated_contract_value",
            "total_timesheet_cost",
            "total_manual_cost",
            "total_bid_cost",
            "estimated_profit",
            "roi_ratio",
        ],
        order_by="modified desc",
    )
    return columns, data
