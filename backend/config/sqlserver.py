import os
from dotenv import load_dotenv
import pymssql

load_dotenv()

def get_connection():
    return pymssql.connect(
        server=os.getenv('DB_SERVER'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        as_dict=True  # This will return results as dictionaries
    )

# Keep this for backward compatibility but it won't be used
SQLSERVER_CONNECTION_STRING = ""
