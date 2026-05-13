import frappe


def execute():
    records = frappe.get_all("Bid Record", pluck="name")

    for name in records:
        doc = frappe.get_doc("Bid Record", name)

        doc.dashboard_estimated_contract_value = doc.estimated_contract_value or 0
        doc.dashboard_total_bid_cost = doc.total_bid_cost or 0
        doc.dashboard_estimated_profit = doc.estimated_profit or 0

        doc.db_update()