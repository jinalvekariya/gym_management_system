// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	duration: function(frm) {
		if(frm.doc.duration=="1 Month"){
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,1))
			frm.set_value("total_amount",frm.doc.rate*1)}
		else if(frm.doc.duration=="3 Month") {
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,3))
			frm.set_value("total_amount",frm.doc.rate*3)
		}
		else if (frm.doc.duration=="6 Month") {
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,6))
			frm.set_value("total_amount",frm.doc.rate*6)
		}
		else if (frm.doc.duration=="12 Month") {
			frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,12))
			frm.set_value("total_amount",frm.doc.rate*12)
		}else{
			frm.set_value("to_date",null)
			frm.set_value("total_amount",0)
		}
	},
	from_date:function(frm){
		if(frm.doc.from_date){
			if(frm.doc.duration=="1 Month"){
				frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,1))
			}
			else if(frm.doc.duration=="3 Month") {
				frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,3))
			}
			else if (frm.doc.duration=="6 Month") {
				frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,3))
			}
			else if (frm.doc.duration=="12 Month") {
				frm.set_value("to_date",frappe.datetime.add_months(frm.doc.from_date,12))
			}else{
				frm.set_value("to_date",null)
			}
		}
	},
	gym_workout_plan: function(frm) {
		if(frm.doc.duration=="1 Month"){
			frm.set_value("total_amount",frm.doc.rate*1)}
		else if(frm.doc.duration=="3 Month") {
			frm.set_value("total_amount",frm.doc.rate*3)
		}
		else if (frm.doc.duration=="6 Month") {
			frm.set_value("total_amount",frm.doc.rate*6)
		}
		else if (frm.doc.duration=="12 Month") {
			frm.set_value("total_amount",frm.doc.rate*12)
		}
		else{
			frm.set_value("total_amount",0)
		}
	}
});

