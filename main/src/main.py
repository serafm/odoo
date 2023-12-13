from dbConnect import DatabaseLogin
from fetchData import FetchData
from server import ServerDialog


def main():
    # Server object. Replace host and port with valid ones.
    server = ServerDialog('localhost', 5432)
    # Connect to the server
    odoo_login = server.connect_server()

    # Database object with user credentials for login. Replace them with valid names.
    database = DatabaseLogin('db_name', 'user', 'password', odoo_login)
    # Login to database
    database.connect_database()

    # Fetch Data object to retrieve data from model name.
    fetch = FetchData('product.product', odoo_login)
    # Fetch data and print results
    fetch.fetch_data()


main()
