// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Group Class Report"] = {
	"filters": [
        {
            "fieldname": "class_type",
            "label": "Class Type",
            "fieldtype": "Select",
            "options": "\nCardio Training\nYoga Training\nBody Building Training"
        },
		{
			"fieldname": "gym_trainer",
            "label": "Gym Trainer",
            "fieldtype": "Data",
		}
	]
};

