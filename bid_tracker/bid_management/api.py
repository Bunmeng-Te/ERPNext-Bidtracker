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


def update_bid_record_totals(doc, method=None):
    if not doc.bid_record:
        return

    bid = frappe.get_doc("Bid Record", doc.bid_record)

    bid.calculate_totals()

    bid.db_set("total_manual_cost", bid.total_manual_cost)
    bid.db_set("total_timesheet_cost", bid.total_timesheet_cost)
    bid.db_set("total_bid_cost", bid.total_bid_cost)
    bid.db_set("estimated_profit", bid.estimated_profit)
    bid.db_set("roi_ratio", bid.roi_ratio)