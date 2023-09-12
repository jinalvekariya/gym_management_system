# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters:None):
    columns = get_columns()
    data = get_gym_member(filters)
    message = None
    labels = ['Cardio Training', 'Yoga Training', 'Body Building Training']
    cardiotraining=0
    yogatraining=0
    bodybuildingtraining=0
    class_type = {
        'Cardio Training': 0,
        'Yoga Training': 0,
        'Body Building Training': 0,
    }
    
    datasets = []
    
    for entry in data:
        if entry['class_type'] == 'Cardio Training':
            cardiotraining += 1
        if entry['class_type'] == 'Yoga Training':
            yogatraining += 1
        if entry['class_type'] == 'Body Building Training':
            bodybuildingtraining += 1
            
    datasets.append({
        'name': 'Class Status',
        'values': [class_type.get('Cardio Training'), class_type.get('Yoga Training'), class_type.get('Body Building Training')]
    })
    
    chart = {
        'data': {
            'labels': labels,
            'datasets': [
                {"values": [cardiotraining, yogatraining, bodybuildingtraining]}
            ]
        },
        'type': 'pie',
        'height': 300, 
    }
    
    return columns, data ,message, chart, datasets, "Popular Group Class Chart"

def get_columns():
    columns = [	
        {
            'fieldname': 'full_name',
            'label': 'Full Name',
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'class_type',
            'label': 'Class Type',
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'select_day',
            'label': 'Day',
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'class_time',
            'label': 'time',
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'gym_trainer',
            'label': 'Gym Trainer',
            'fieldtype': 'Data'
        },
    ]
    return columns

def get_gym_member(filters=None):
    data = []
    filter = []
    if filters.get('class_type'):
        class_type=filters.get('class_type')
        filter.append({'class_type':class_type})
        
        
    gym_member_data = frappe.db.get_list("Group Class", filters=filter, fields=["full_name", "class_type", "select_day", "class_time", "gym_trainer"])
    for d in gym_member_data:
        row = {
            'full_name': d.full_name,
            'class_type': d.class_type,
            'select_day': d.select_day,
            'class_time': d.class_time,
            'gym_trainer': d.gym_trainer
            }
        data.append(row)
    
    return data

