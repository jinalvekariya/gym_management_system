# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymServices(Document):
	def validate(self):
		if self.book_locker==1:
			if frappe.db.exists('Gym Services',{'book_locker': 1}) and self.is_new():
				book_locker = frappe.db.count('Gym Services',{'book_locker': 1})
				if book_locker >= frappe.db.get_single_value('Gym Settings', 'locker_limit'):
					frappe.throw("All slots are filled.")
				else:
					frappe.msgprint(('Your locker is booked successfully.'))
