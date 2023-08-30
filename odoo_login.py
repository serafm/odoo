import odoorpc


class OdooLogin:

    def __init__(self, host, db_name, user, password, odoo=None):
        """ Initialize user credentials """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.odoo = odoo
        self.host = host

    def connect_server(self):
        """ Connect to the Odoo server """
        self.odoo = odoorpc.ODOO(self.host, port=8016)

    def database_login(self):
        """ Login in to the database """
        self.odoo.login(self.db_name, self.user, self.password)


class FetchData:

    def __init__(self, model_name, records=None, odoo=None):
        """ Initialize model name for data retrieval """
        self.model_name = model_name
        self.odoo = odoo
        self.records = records

    def fetch_data(self):
        """ Retrieve data from the database and print the results """
        if self.model_name in self.odoo.env:
            self.records = self.odoo.env[self.model_name]
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
