# Use sqlalchemy to connect to SQL databases using Python/Pandas.

import pandas as pd
import sqlalchemy as db
import pymysql # For MySQL. For MS SQL Server, use pyodbc
import keyring

# Create an engine with database and authentication details. For MS SQL Server, you can enable windows authentication. That way there's not need to give a password.
# Another way is to encode the password using keyring
engine = db.create_engine('mysql+pymysql://root:'+keyring.get_password('mysql_db', 'root')+'@localhost/sample_db?host=localhost?port=3306')
# mysql_db : connection name given in keyring while encoding, roor : user name, sample_db : Schema DB
table_name = 'sample_table'

query = 'SELECT * from sample_table'
df = pd.read_sql(query, engine) # Reads data using the give query and engine and write it as a dataframe

#To truncate and load a table
conn = engine.connect() # Create a connection
conn.execute("TRUNCATE TABLE " + table_name) # Query to truncate the table

# Loads the data into the given table; if_exists accepts 'append' or 'replace' - to check if the table exists
df.to_sql(table_name, con=engine, if_exists='append', index = False)
