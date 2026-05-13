import frappe
from frappe.model.document import Document


class BidCostEntry(Document):
    def on_update(self):
        self.update_bid_record()

    def on_trash(self):
        self.update_bid_record()

    def update_bid_record(self):
        if self.bid_record:
            doc = frappe.get_doc("Bid Record", self.bid_record)
            doc.calculate_totals()
            doc.save(ignore_permissions=True)