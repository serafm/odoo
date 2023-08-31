import odoorpc


class ServerDialog:

    def __init__(self, host, port):
        """
        Initialize the ServerDialog class with a host parameter

        :param host: The hostname or IP address of the server.
        :param port: The port number used for the server connection.
        """
        self.host = host
        self.port = port

    def connect_server(self):
        """
        Attempt to establish a connection to the Odoo server using the provided host and port

        :return: Odoo server object
        """
        try:
            odoo = odoorpc.ODOO(self.host, self.port)
            print('Server connected successfully!')
            return odoo  # Return the connected Odoo server object
        except Exception as e:
            # Handle the exception if the connection attempt fails
            print(f"Error connecting to the server: {str(e)}")


class DatabaseLogin:

    def __init__(self, db_name, user, password, odoo):
        """
        Initialize user credentials for database login.

        :param db_name: Name of the database to connect to.
        :param user: Username for authentication.
        :param password: Password for authentication.
        :param odoo: Reference to the connected Odoo server object.
        """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.odoo = odoo

    def connect_database(self):
        """
        Log in to the database using provided user credentials.

        :return: None
        """
        try:
            self.odoo.login(self.db_name, self.user, self.password)
            print('Logged in database successfully!')
        except Exception as e:
            # Handle the exception if login fails
            print(f"Error connecting to the database: {str(e)}")


class FetchData:

    def __init__(self, model_name, odoo):
        """
        Initialize the model name for data retrieval.

        :param model_name: Name of the model from which data will be retrieved.
        :param odoo: Reference to the connected Odoo server object.
        """
        self.model_name = model_name
        self.odoo = odoo

    def fetch_data(self):
        """
        Retrieve data from the database using the provided model name and print the results.

        :return: None
        """
        # Check if the model name exists in the Odoo environment
        if self.model_name in self.odoo.env:
            # Search and read data for all records, fetching 'name' and 'price' fields
            data = self.odoo.env[self.model_name]
            result = data.search_read([], ['name', 'price'])

            # Print retrieved results, showing product name and price
            print("Product List:")
            for product in result:
                product_name = product['name']
                product_price = product['price']
                print(f"Name: {product_name}, Price: {product_price}")

        else:
            return 'No data found'


# Server object
server = ServerDialog('https://50192056-saas-16-4-all.runbot107.odoo.com', 5432)

# Connect to the server
odoo_api = server.connect_server()


# Database object with user credentials for login
database = DatabaseLogin('50192056-saas-16-4-all',
                         'admin',
                         'admin12345',
                         odoo_api)

# Login to database
database.connect_database()

# Fetch Data object to retrieve data from model name
fetch = FetchData('product.product',
                  odoo_api)

# Fetch data and print results
fetch.fetch_data()
