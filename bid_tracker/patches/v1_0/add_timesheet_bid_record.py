import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
    custom_fields = {
        "Timesheet": [
            {
                "fieldname": "bid_record",
                "label": "Bid Record",
                "fieldtype": "Link",
                "options": "Bid Record",
                "insert_after": "parent_project",
                "in_list_view": 1,
            }
        ]
    }

    create_custom_fields(custom_fields, update=True)