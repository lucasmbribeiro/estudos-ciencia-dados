import os
from dotenv import load_dotenv
load_dotenv()

SAMPLE_SPREADSHEET_ID  = "1GYyp6cLDAhUDFz-itEUmp5lVxpqBJrj0075fjVVk7yM"

TYPE = "service_account"
PRIVATE_KEY_ID = os.getenv('PRIVATE_KEY_ID')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CLIENT_EMAIL = os.getenv('CLIENT_EMAIL')
CLIENT_ID = os.getenv('CLIENT_ID')