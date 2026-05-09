import frappe


@frappe.whitelist()
def recalculate_bid(bid_name: str):
    doc = frappe.get_doc("Bid Record", bid_name)
    doc.calculate_totals()
    doc.save(ignore_permissions=True)
    return {
        "name": doc.name,
        "total_manual_cost": doc.total_manual_cost,
        "total_timesheet_cost": doc.total_timesheet_cost,
        "total_bid_cost": doc.total_bid_cost,
        "estimated_profit": doc.estimated_profit,
        "roi_ratio": doc.roi_ratio,
    }