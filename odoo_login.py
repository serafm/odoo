import odoorpc


class OdooLogin:

    def __init__(self, host, db_name, user, password, odoo=None):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.odoo = odoo
        self.host = host

    def connect_server(self):
        self.odoo = odoorpc.ODOO(self.host, port=8016)

    def database_login(self):
        self.odoo.login(self.db_name, self.user, self.password)


class FetchData:

    def __init__(self, data_model_name, records=None, odoo=None):
        self.data_model_name = data_model_name
        self.odoo = odoo
        self.records = records

    def fetch_data(self):
        if self.data_model_name in self.odoo.env:
            self.records = self.odoo.env[self.data_model_name]
            product_ids = self.records.search([])
            for product in self.records.browse(product_ids):
                print(product.name)
                print(product.price)


# HERE EN KSERO TI KAMNO RE ZARTILIE

odoo_login = OdooLogin(
    'localhost',
    'DemoDB',
    'admin',
    'admin'
)

odoo_login.connect_server()

odoo_login.database_login()
