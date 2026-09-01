{
    'name': 'Library Management',
    'version': '19.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'reports/library_book_reports.xml',
        'views/library_book_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
