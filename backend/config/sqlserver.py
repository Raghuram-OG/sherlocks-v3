import os
from dotenv import load_dotenv
import pymssql

load_dotenv()

def get_connection():
    return pymssql.connect(
        server=os.getenv('DB_SERVER'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

# For backward compatibility with your existing code
SQLSERVER_CONNECTION_STRING = ""  # Keep this to avoid errors, but it won't be used
