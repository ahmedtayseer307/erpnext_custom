from frappe.utils import time_diff_in_hours


def clac_hours(doc,event):
    if not doc.check_in or not doc.check_out:
        doc.status = "Absent"
    else:
        doc.hours = time_diff_in_hours(doc.check_out, doc.check_in)