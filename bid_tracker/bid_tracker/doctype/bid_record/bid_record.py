import frappe
from frappe.model.document import Document


class BidRecord(Document):
    def validate(self):
        self.sync_customer_from_opportunity()
        self.calculate_totals()

    def sync_customer_from_opportunity(self):
        if self.opportunity and not self.customer:
            self.customer = frappe.db.get_value("Opportunity", self.opportunity, "party_name")

    def calculate_totals(self):
        self.total_manual_cost = self.get_manual_cost()
        self.total_timesheet_cost = self.get_timesheet_cost()
        self.total_bid_cost = flt(self.total_manual_cost) + flt(self.total_timesheet_cost)
        self.estimated_profit = flt(self.estimated_contract_value) - flt(self.total_bid_cost)
        if flt(self.total_bid_cost) > 0:
            self.roi_ratio = self.estimated_profit / self.total_bid_cost
        else:
            self.roi_ratio = 0

    def get_manual_cost(self):
        return frappe.db.sql(
            """
            SELECT COALESCE(SUM(amount), 0)
            FROM `tabBid Cost Entry`
            WHERE bid_record = %s
            """,
            (self.name,),
        )[0][0]

    def get_timesheet_cost(self):
        # Prefer Timesheet.costing_amount if available on your ERPNext version.
        if frappe.db.has_column("Timesheet", "costing_amount"):
            return frappe.db.sql(
                """
                SELECT COALESCE(SUM(costing_amount), 0)
                FROM `tabTimesheet`
                WHERE bid_record = %s
                """,
                (self.name,),
            )[0][0]

        # Fallback: estimate labour cost using total_hours * per-hour rate.
        # You can replace 50 with a field or employee costing rule in your environment.
        fallback_hourly_rate = 50
        if frappe.db.has_column("Timesheet", "total_hours"):
            hours = frappe.db.sql(
                """
                SELECT COALESCE(SUM(total_hours), 0)
                FROM `tabTimesheet`
                WHERE bid_record = %s
                """,
                (self.name,),
            )[0][0]
            return flt(hours) * fallback_hourly_rate
        return 0


def flt(value):
    try:
        return float(value or 0)
    except Exception:
        return 0.0
