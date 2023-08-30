import xmlrpc.client
import odoorpc

info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
print("heree")

url, db, username, password = info['host'], info['database'], info['user'], info['password']
print("heree")
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

odoo = odoorpc.ODOO(url, port=8069)
print(odoo.db.list())
