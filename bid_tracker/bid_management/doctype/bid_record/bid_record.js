frappe.ui.form.on("Bid Record", {
  estimated_contract_value(frm) {
    calculate_metrics(frm);
  },
});

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
