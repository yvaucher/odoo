{
    'name': 'Twitter Roller',
    'category': 'Website',
    'summary': 'Add twitter scroller snippet in website builder',
    'website': 'https://www.odoo.com/page/website-builder',
    'license': 'AGPL-3',
    'version': '1.0',
    'description': """
Display best tweets
========================

        """,
    'author': 'OpenERP SA',
    'depends': ['website'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/twitter_data.xml',
        'views/twitter_view.xml',
        'views/twitter_snippet.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
}
