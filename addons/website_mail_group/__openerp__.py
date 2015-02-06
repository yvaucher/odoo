{
    'name': 'Mailing List Archive',
    'category': 'Website',
    'summary': '',
    'version': '1.0',
    'description': """
OpenERP Mail Group : Mailing List Archives
==========================================

        """,
    'author': 'OpenERP SA',
    'license': 'AGPL-3',
    'depends': ['website_mail'],
    'data': [
        'views/website_mail_group.xml',
        'views/snippets.xml',
    ],
    'qweb': [],
    'installable': True,
}
