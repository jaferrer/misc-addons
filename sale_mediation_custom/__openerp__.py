{
    'name' : 'Sales in mediation company (custom) ',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Workflow',
    'website' : 'https://it-projects.info',
    'description': """
    Tested on odoo 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d

    """,
    'depends' : ['sale_mediation', 'sale', 'crm', 'project', 'contract_purchases', 'account_analytic_analysis', 'access_custom', 'website_proposal', 'sales_team'],
    'data':[
        'report.xml',
        'wizard/sale_case.xml',
        'views.xml',
        #'data.xml',
        ],
    'installable': True,
}