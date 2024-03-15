from .dassco_test_client import client

ASSET_GUID = "test_asset12"
INSTITUTION_NAME = "test-institution"
COLLECTION_NAME = "test-collection"
FILE_NAME = "helloworld.txt"


def test_delete_share():
    res = client.file_proxy.delete_share(INSTITUTION_NAME, COLLECTION_NAME, ASSET_GUID, ["user1"], 1)
    assert res.status_code == 200


def test_open_share():
    res = client.file_proxy.open_share(INSTITUTION_NAME, COLLECTION_NAME, ASSET_GUID, ["user1"], 1)
    assert res.status_code == 200


def test_upload_file():
    res = client.file_proxy.upload(FILE_NAME, INSTITUTION_NAME, COLLECTION_NAME, ASSET_GUID, 1)
    assert res.status_code == 200


def test_get_file():
    res = client.file_proxy.get_file(INSTITUTION_NAME, COLLECTION_NAME, ASSET_GUID, FILE_NAME)
    file = open(FILE_NAME, 'rb')
    file_data = file.read()
    file.close()
    assert res.status_code == 200
    assert res.content == file_data


def test_delete_file():
    res = client.file_proxy.delete_file(INSTITUTION_NAME, COLLECTION_NAME, ASSET_GUID, FILE_NAME)
    assert res.status_code == 204
