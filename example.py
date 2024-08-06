from dasscostorageclient import DaSSCoStorageClient
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)

institutions = client.institutions.list()

print(institutions)
