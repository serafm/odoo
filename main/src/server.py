import odoorpc


class ServerDialog:

    def __init__(self, host, port, odoo=None):
        """
        Initialize the ServerDialog class with a host parameter

        :param host: The hostname or IP address of the server.
        :param port: The port number used for the server connection.
        :param odoo: The Odoo server object to be created
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