# scripts/test_api.py
import xmlrpc.client

import os

URL = os.environ["ODOO_URL"]
DB = os.environ["ODOO_DB"]
USERNAME = os.environ["ODOO_USERNAME"]
PASSWORD = os.environ["ODOO_PASSWORD"]

common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
uid = common.authenticate(DB, USERNAME, PASSWORD, {})

models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

# Lecture
books = models.execute_kw(
    DB, uid, PASSWORD,
    'library.book', 'search_read',
    [[]],
    {'fields': ['name', 'state', 'due_date']}
)
print(books)

# Création
new_id = models.execute_kw(
    DB, uid, PASSWORD,
    'library.book', 'create',
    [{'name': 'Créé via API externe'}]
)
print("Créé, id:", new_id)
