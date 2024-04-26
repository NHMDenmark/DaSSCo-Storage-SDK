from dasscostorageclient import DaSSCoStorageClient
from dasscostorageclient.core.enums import WorkstationStatus

client_id = "ingestion-server"
client_secret = "xD5leNJ3HCDS1R1j9gBsN9rLLe9kn2hp"

client = DaSSCoStorageClient(client_id, client_secret)

workstation = client.workstations.create("test-institution", "ti-ws-02", WorkstationStatus.IN_SERVICE)

print(workstation)



# from dotenv import load_dotenv
# from dasscostorageclient import DaSSCoStorageClient
# import os
#
# load_dotenv()
#
# file = open("C:/Users/wdm563/PycharmProjects/DaSSCo-Storage-API/helloworld.txt", 'rb')
#
# file_data = file.read()
#
# file.close()
#
# filename = os.path.basename(file.name)
#
# print(filename)
