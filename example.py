from dotenv import load_dotenv
from dasscostorageclient import DaSSCoStorageClient
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client = DaSSCoStorageClient(client_id, client_secret)

res = client.institutions.list_institutions()

print(res.json())

# # Seek to the end of the file
# file.seek(0, os.SEEK_END)
# # Get the current position of the cursor, which is the file size
# file_size = file.tell()
#
# print(file_size)


#
# body = {
#     "asset_pid": "asdf-12346-3333-100a21",
#     "asset_guid": "test_asset4",
#     "funding": "some funding",
#     "subject": "folder",
#     "institution": "test-institution",
#     "pipeline": "ti-p1",
#     "collection": "test-collection",
#     "workstation": "ti-ws-01",
#     "status": "WORKING_COPY",
# }
#
# print(client.assets.create_asset(body, 15))
