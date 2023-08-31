# Odoo API Python script

### Odoo Integration - Retrieve Product List

This Python script connects to an Odoo instance and
retrieves a list of products using Odoo RPC.

##### Requirements for execution

- **Valid server hostname:** Replace the host and port names in the new class object
with the appropriate server hostname and port number.
This will establish a connection with the desired server.
- **Database credentials:** Provide the necessary information to login
and fetch data from the database. Replace the database name, user, and password
names with the correct credentials for the database you want to access.


#### Approach
After carefully reading the task's description and requirements, 
my first step was to review the Odoo API documentation. Once I had a clear understanding
of the API functionalities, I proceeded to create a new GitHub repository to track my progress,
manage, and version-control my code.
To break down the problem into manageable parts, I divided it 
into sub-problems. Initially, I focused on establishing a secure 
connection to the server by developing a dedicated class. Subsequently,
I implemented a separate class to handle the connection to the database.
Finally, I created a class specifically designed to fetch the required data.

####  Challenges
I successfully developed the necessary classes and functions
for seamless integration and efficient data retrieval.
However, I encountered a minor setback when attempting to establish a connection with a demo instance database.
Despite this obstacle, I remained determined to find a solution.
Although I wasn't able to test the code with a demo Odoo instance database and fetch data in this particular case,
I gained invaluable knowledge about the Odoo API and its vast potential. This experience helped me acquire
the skills to connect to servers, databases, and interact with various data using APIs.
