frappe.ui.form.on("Bid Record", {
  refresh(frm) {
    initialize_financial_fields(frm);
  },

  estimated_contract_value(frm) {
    calculate_metrics(frm);
  },
});

function initialize_financial_fields(frm) {
  frm.set_value("total_timesheet_cost", frm.doc.total_timesheet_cost || 0);
  frm.set_value("total_manual_cost", frm.doc.total_manual_cost || 0);
  frm.set_value("total_bid_cost", frm.doc.total_bid_cost || 0);
  frm.set_value("estimated_profit", frm.doc.estimated_profit || 0);
  frm.set_value("roi_ratio", frm.doc.roi_ratio || 0);
}

function calculate_metrics(frm) {
  let contract = frm.doc.estimated_contract_value || 0;
  let total_cost = frm.doc.total_bid_cost || 0;

  let profit = contract - total_cost;

  frm.set_value("estimated_profit", profit);

  if (total_cost > 0) {
    frm.set_value("roi_ratio", (profit / total_cost) * 100);
  } else {
    frm.set_value("roi_ratio", 0);
  }
}
