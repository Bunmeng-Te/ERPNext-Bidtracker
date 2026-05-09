frappe.ui.form.on("Bid Record", {
  refresh(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button(__("Recalculate P&L"), async () => {
        const r = await frappe.call({
          method: "bid_tracker.api.recalculate_bid",
          args: { bid_name: frm.doc.name },
        });
        if (r.message) {
          await frm.reload_doc();
          frappe.show_alert({
            message: __("P&L recalculated"),
            indicator: "green",
          });
        }
      });
    }
  },
});
