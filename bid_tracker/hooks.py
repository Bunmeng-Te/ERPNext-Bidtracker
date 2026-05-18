app_name = "bid_tracker"
app_title = "Bid Tracker"
app_publisher = "OpenAI"
app_description = "Custom ERPNext module for pre-contract bid tracking"
app_email = "bidtrackererpnext@gmail.com"
app_license = "MIT"

after_install = "bid_tracker.install.after_install"

doctype_js = {
    "Bid Record": "public/js/bid_record.js",
}

doc_events = {
    "Timesheet": {
        "on_update": "bid_tracker.bid_management.api.update_bid_record_totals",
        "on_submit": "bid_tracker.bid_management.api.update_bid_record_totals",
        "on_cancel": "bid_tracker.bid_management.api.update_bid_record_totals",
    },
    "Bid Cost Entry": {
        "on_update": "bid_tracker.bid_management.api.update_bid_record_totals",
        "on_trash": "bid_tracker.bid_management.api.update_bid_record_totals",
    }
}


fixtures = [
    "Workflow",
    "Workflow State",
    "Workflow Action Master",
    "Notification",
    "Role",
    "Dashboard",
    "Number Card",
    "Report",
    "Workspace",
    {
    "dt": "Dashboard Chart",
    "filters": [
        ["name", "in", ["Bid Status Breakdown"]]
    ]
    }
]