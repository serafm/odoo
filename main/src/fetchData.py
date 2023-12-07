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
            print('Data not found')
            return -1
