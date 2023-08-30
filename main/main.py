import odoorpc


class ServerDialog:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect_server(self):
        """ Connect to the Odoo server """
        try:
            odoo = odoorpc.ODOO(self.host, 'jsonrpc', self.port)
            return odoo
        except Exception as e:
            # Handle the exception
            print(f"Error connecting to the server: {str(e)}")


class DatabaseLogin:

    def __init__(self, db_name, user, password, odoo):
        """ Initialize user credentials """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.odoo = odoo

    def connect_database(self):
        """ Login in to the database with user credentials"""
        try:
            self.odoo.login(self.db_name, self.user, self.password)
        except Exception as e:
            # Handle the exception
            print(f"Error connecting to the database: {str(e)}")


class FetchData:

    def __init__(self, model_name, odoo):
        """ Initialize model name for data retrieval """
        self.model_name = model_name
        self.odoo = odoo

    def fetch_data(self):
        """ Retrieve data from the database from the given model name and print the results """
        # Check if model name exist and retrieve data
        if self.model_name in self.odoo.env:
            # Fetch data from model
            data = self.odoo.env[self.model_name]
            result = data.search_read([], ['name', 'price'])

            # Print results for every product by name and price
            print("Product List:")
            for product in result:
                product_name = product['name']
                product_price = product['price']
                print(f"Name: {product_name}, Price: {product_price}")

        else:
            return 'No data found'


# Server object
server = ServerDialog('localhost',
                      8016)

# Connect to the server
odoo_api = server.connect_server()

# Database object with user credentials for login
database = DatabaseLogin('demoDB',
                         'admin',
                         'admin',
                         odoo_api)

# Login to database
database.connect_database()

# Fetch Data object to retrieve data from model name
fetch = FetchData('product.product',
                  odoo_api)

# Fetch data and print results
fetch.fetch_data()
