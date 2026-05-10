import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def after_install():
    create_timesheet_bid_field()
    create_employee_hourly_rate_field()
    set_bid_cost_entry_naming()


def create_timesheet_bid_field():
    custom_fields = {
        "Timesheet": [
            {
                "fieldname": "bid_record",
                "label": "Bid Record",
                "fieldtype": "Link",
                "options": "Bid Record",
                "insert_after": "parent_project",
                "read_only": 0,
                "in_list_view": 1,
            }
        ]
    }

    create_custom_fields(custom_fields, update=True)


def create_employee_hourly_rate_field():
    custom_fields = {
        "Employee": [
            {
                "fieldname": "hourly_rate",
                "label": "Hourly Rate",
                "fieldtype": "Currency",
                "insert_after": "company",
                "default": 50,
            }
        ]
    }

    create_custom_fields(custom_fields, update=True)


def set_bid_cost_entry_naming():
    try:
        make_property_setter(
            "Bid Cost Entry",
            None,
            "autoname",
            "format",
            "Data",
            validate_fields_for_doctype=False,
        )

        make_property_setter(
            "Bid Cost Entry",
            None,
            "naming_series",
            "BCE-.YYYY.-.#####",
            "Data",
            validate_fields_for_doctype=False,
        )

    except Exception:
        frappe.log_error(
            frappe.get_traceback(),
            "Bid Tracker install warning"
        )