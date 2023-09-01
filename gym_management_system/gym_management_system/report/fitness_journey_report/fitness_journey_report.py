# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    labels = []
    values = []
    for i in data:
        labels.append(i['date'])
        values.append(i['burn_calories'])
        
    chart = {
        "type": "bar",
        "data": {
            "labels": labels,
            "datasets": [
                {"values": values},	
            ],
        },
    }
    return columns, data, "Fittness Journey Report", chart

def get_columns():
    return [	
        "Burn Calories:int:100",
        "Date:Date:100"
    ]

def get_data(filters=None):
    data=[]
    from_date = None
    to_date = None	
    if filters.gym_member and filters.from_date and filters.to_date:
        from_date=datetime.strptime(filters.from_date, '%Y-%m-%d').date()
        to_date=datetime.strptime(filters.to_date, '%Y-%m-%d').date()

        doc= frappe.get_doc("Gym Member",filters.gym_member)
        print(from_date)
        for ch in doc.health_metrics:
            if from_date and to_date:
                if(from_date<=ch.date and to_date>=ch.date):
                    row={
                     "burn_calories":ch.burn_calories,
                     "date":ch.date
                    }
                    data.append(row)


    return data