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