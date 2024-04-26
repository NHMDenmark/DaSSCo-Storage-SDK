import requests_mock
from dotenv import load_dotenv
from dasscostorageclient import DaSSCoStorageClient
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)


TOKEN_URL = "https://idp.test.dassco.dk/realms/dassco/protocol/openid-connect/token"

with requests_mock.Mocker() as m:
    m.post(TOKEN_URL, json={'access_token': '123'})
    mockClient = DaSSCoStorageClient('client_id', 'client_secret')


