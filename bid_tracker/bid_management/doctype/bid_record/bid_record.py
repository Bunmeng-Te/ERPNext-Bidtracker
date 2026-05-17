import frappe
from frappe.model.document import Document


class BidRecord(Document):
    def autoname(self):

        existing = frappe.get_all(
            "Bid Record",
            pluck="name"
        )

        used_numbers = []

        for name in existing:
            try:
                number = int(name.split("-")[-1])
                used_numbers.append(number)
            except:
                pass

        next_number = 1

        while next_number in used_numbers:
            next_number += 1

        year = frappe.utils.now_datetime().year

        self.name = f"BR-{year}-{next_number:05d}"

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

        self.dashboard_estimated_contract_value = flt(self.estimated_contract_value)
        self.dashboard_total_bid_cost = flt(self.total_bid_cost)
        self.dashboard_estimated_profit = flt(self.estimated_profit)


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
        timesheets = frappe.db.sql(
            """
            SELECT employee, total_hours
            FROM `tabTimesheet`
            WHERE bid_record = %s
            """,
            (self.name,),
            as_dict=True
        )

        total_cost = 0

        for ts in timesheets:
            hourly_rate = frappe.db.get_value(
                "Employee",
                ts.employee,
                "hourly_rate"
            ) or 0

            total_cost += flt(ts.total_hours) * flt(hourly_rate)

        return total_cost


def flt(value):
    try:
        return float(value or 0)
    except Exception:
        return 0.0