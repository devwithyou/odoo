{
    'name': 'Schooling System',
    'author': 'Muhammad Salar',
    'version': '1.0',
    "depends": ["base"],
    'application': True,
    'installable': True,

    'data': [
        'security/ir.model.access.csv',
        'views/school_erp_menu.xml',
        'views/school_students_views.xml',
        'views/school_teacher_views.xml',
        'views/school_fees_vies.xml',
    ],
}