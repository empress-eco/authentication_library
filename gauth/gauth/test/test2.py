import frappe
frappe.init(site="aysha.erpgulf.com")
frappe.connect()

#get time from frappe 
print(frappe.utils.now_datetime())
#get linux time
print(frappe.utils.now())
#print unix_timestamp
print(frappe.utils.get_datetime(frappe.utils.now_datetime()).timestamp())


# doc = frappe.db.get_list(
#     'Sales Invoice',
#     filters={"name": "ACC-SINV-2023-00013"},
#     # fields=["name", "customer", "customer_name", "posting_date", "due_date", "grand_total", "outstanding_amount", "status", "company", "currency", "base_grand_total", "base_outstanding_amount", "base_paid_amount", "base_discount_amount", "base_rounded_total", "base_change_amount", "base_net_total", "base_total_taxes_and_charges", "base_total"]
#     fields=["name","items.description","items.amount"]
# )
# print(doc)

# print("something")


