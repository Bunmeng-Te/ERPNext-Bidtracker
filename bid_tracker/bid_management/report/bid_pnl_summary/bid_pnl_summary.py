import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data


def get_columns():
    return [
        {
            "label": "Bid Record",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Bid Record",
            "width": 180,
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": "Estimated Contract Value",
            "fieldname": "estimated_contract_value",
            "fieldtype": "Currency",
            "width": 180,
        },
        {
            "label": "Total Bid Cost",
            "fieldname": "total_bid_cost",
            "fieldtype": "Currency",
            "width": 160,
        },
        {
            "label": "Estimated Profit",
            "fieldname": "estimated_profit",
            "fieldtype": "Currency",
            "width": 160,
        },
        {
            "label": "ROI Ratio",
            "fieldname": "roi_ratio",
            "fieldtype": "Percent",
            "width": 120,
        },
    ]


def get_data():
    return frappe.get_all(
        "Bid Record",
        fields=[
            "name",
            "status",
            "estimated_contract_value",
            "total_bid_cost",
            "estimated_profit",
            "roi_ratio",
        ],
        order_by="creation desc",
    )