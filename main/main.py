import odoorpc


class ServerDialog:

    def __init__(self, host, port, odoo=None):
        """
        Initialize the ServerDialog class with a host parameter

        :param host: The hostname or IP address of the server.
        :param port: The port number used for the server connection.
        """
        self.host = host
        self.port = port
        self.odoo = odoo

    def connect_server(self):
        """
        Attempt to establish a connection to the Odoo server using the provided host and port

        :return: Odoo server object
        """
        try:
            self.odoo = odoorpc.ODOO(self.host, 'jsonrpc', self.port, version=16.0)
            print('Server connected successfully!')
            print("host: ", self.odoo.host)
            print("port: ", self.odoo.port)

            return self.odoo  # Return the connected Odoo server object

        except Exception as e:
            # Handle the exception if the connection attempt fails
            print(f"Error connecting to the server: {str(e)}")


class DatabaseLogin:

    def __init__(self, db_name, user, password):
        """
        Initialize user credentials for database login.

        :param db_name: Name of the database to connect to.
        :param user: Username for authentication.
        :param password: Password for authentication.
        """
        self.db_name = db_name
        self.user = user
        self.password = password

    def connect_database(self, odoo_login):
        """
        Log in to the database using provided user credentials.

        :return: None
        """
        try:
            odoo_login.login(self.db_name, self.user, self.password)
            print('Logged in database successfully!')
        except Exception as e:
            # Handle the exception if login fails
            print(f"Error connecting to the database: {str(e)}")


class FetchData:

    def __init__(self, model_name):
        """
        Initialize the model name for data retrieval.

        :param model_name: Name of the model from which data will be retrieved.
        """
        self.model_name = model_name

    def fetch_data(self, odoo_login):
        """
        Retrieve data from the database using the provided model name and print the results.

        :return: None
        """
        # Check if the model name exists in the Odoo environment
        if self.model_name in odoo_login.env:
            # Search and read data for all records, fetching 'name' and 'price' fields
            data = odoo_login.env[self.model_name]
            result = data.search_read([], ['name', 'price'])

            # Print retrieved results, showing product name and price
            print("Product List:")
            for product in result:
                product_name = product['name']
                product_price = product['price']
                print(f"Name: {product_name}, Price: {product_price}")

        else:
            return 'No data found'


# Server object. Replace host and port with valid ones.
server = ServerDialog('localhost', 5432)

# Connect to the server
odoo = server.connect_server()

# Database object with user credentials for login. Replace them with valid names.
database = DatabaseLogin('db_name',
                         'user',
                         'password')

# Login to database
database.connect_database(odoo)

# Fetch Data object to retrieve data from model name.
fetch = FetchData('product.product')

# Fetch data and print results
fetch.fetch_data(odoo)
