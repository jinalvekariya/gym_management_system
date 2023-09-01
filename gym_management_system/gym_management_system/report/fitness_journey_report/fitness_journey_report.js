// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Fitness Journey Report"] = {
	"filters": [
		{
            "fieldname": "gym_member",
            "label": "Gym Member",
            "fieldtype": "Link",
            "options": "Gym Member"
        },
        {
            "fieldname":"from_date",
            "label":"From Date",
            "fieldtype": "Date",
    
        },
        {
            "fieldname":"to_date",
            "label":"To Date",
            "fieldtype": "Date",
    
        }
	]
};
