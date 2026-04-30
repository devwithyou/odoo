{
    "name": "Pharmacy Management",
    "author": "Muhammad Salaar",
    "version": "1.0",
    "depends": ["base"],
    "application": True,
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/pharmacy_dashboard_views.xml",
        "views/pharmacy_medicine_views.xml",
        "views/pharmacy_customer_views.xml",
        "views/pharmacy_batch_views.xml",
        "views/pharmacy_sale_views.xml",
        "views/pharmacy_menu.xml",
        "reports/pharmacy_sale_report.xml",
    ],
}
