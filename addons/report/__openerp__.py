{
    'name': 'Report',
    'category': 'Base',
    'summary': 'Report',
    'version': '1.0',
    'description': """
Report
        """,
    'author': 'OpenERP SA',
    'license': 'AGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'views/layouts.xml',
        'views/views.xml',
        'data/report_paperformat.xml',
        'security/ir.model.access.csv',
        'views/report.xml',
    ],
    'installable': True,
    'auto_install': True,
}
