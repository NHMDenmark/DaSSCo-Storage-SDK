import pytest
from .dassco_test_client import client

ASSET_GUID = "dassco_storageclient_test_asset"

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # before

    yield # run tests

    # after
 

@pytest.mark.order(1)
def test_can_create_asset():
    body = {
        "asset_pid": ASSET_GUID,
        "asset_guid": "test_asset",
        "funding": ["some funding"],
        "subject": "folder",
        "institution": "test-institution",
        "pipeline": "test-pipeline",
        "collection": "test-collection",
        "workstation": "test-workstation",
        "status": "WORKING_COPY",
    }
    res = client.assets.create(body, 1)
    status_code = res.get('status_code')
    asset = res.get('data')
    assert status_code == 200
    assert asset.guid == 'test_asset'
    assert asset.http_info.allocated_storage_mb == 1

@pytest.mark.order(2)
def test_can_get_asset():
    res = client.assets.get(ASSET_GUID)
    status_code = res.get('status_code')
    asset = res.get('data')
    assert status_code == 200
    assert asset.guid == ASSET_GUID

@pytest.mark.order(3)
def test_can_update_asset():
    
    body = {
        'funding': ['test funding'],
        'subject': 'test subject',
        'updateUser': 'Test user',  # Required
        'institution': 'test-institution',  # Required
        'pipeline': 'test-pipeline',  # Required
        'collection': 'test-collection',  # Required
        'workstation': 'test-workstation',  # Required
        'status': 'WORKING_COPY'  # Required
    }
    res = client.assets.update(ASSET_GUID, body)
    status_code = res.get('status_code')
    asset = res.get('data')
    assert status_code == 200
    assert asset.funding == ['test funding']
    assert asset.subject == 'test subject'

@pytest.mark.order(4)
def test_can_list_events():
    res = client.assets.list_events(ASSET_GUID)
    status_code = res.get('status_code')
    events = res.get('data')
    assert status_code == 200
    assert isinstance(events, list)

@pytest.mark.order(5)
def test_delete_metadata():
    res_del = client.assets.delete_metadata(ASSET_GUID)
    status_code = res_del.get('status_code')
    assert status_code == 204