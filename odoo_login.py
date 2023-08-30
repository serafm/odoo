import odoorpc


class OdooLogin:

    def __init__(self, host, db_name, user, password, odoo=None):
        """ Initialize user credentials """
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.odoo = odoo

    def connect_server(self):
        """ Connect to the Odoo server """
        try:
            self.odoo = odoorpc.ODOO(self.host, port=8069)
        except Exception as e:
            # Handle the exception
            print(f"Error connecting to the server: {str(e)}")

    def database_login(self):
        """ Login in to the database with user credentials"""
        self.odoo.login(self.db_name, self.user, self.password)


class FetchData:

    def __init__(self, model_name, data=None, odoo=None):
        """ Initialize model name for data retrieval """
        self.model_name = model_name
        self.odoo = odoo
        self.data = data

    def fetch_data(self):
        """ Retrieve data from the database from the given model name and print the results """
        if self.model_name in self.odoo.env:
            self.data = self.odoo.execute(self.model_name, 'read', [], ['name', 'price'])


odoo_login = OdooLogin(
    'localhost',
    'DemoDB',
    'admin',
    'admin'
)

odoo_login.connect_server()

odoo_login.database_login()

records = FetchData('product.product')

records.fetch_data()
