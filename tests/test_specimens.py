import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import pytest
from tests.dassco_test_client import client
import json
import random

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # before

    yield # run tests

    # after 

@pytest.mark.order(1)
def test_can_create_specimen():

    random_int = random.randint(1, 10000000)

    specimen_pid = f"test_pid_{random_int}"
    specimen = {
    "institution": "test-institution",
    "collection": "test-collection",
    "barcode": f"test-barcode-{random_int}",
    "specimen_pid": specimen_pid,
    "preparation_types": ["pinned"],
    "specimen_id": None,
    "role_restrictions": []
    }

    res = client.specimens.create_or_update(specimen_pid, specimen)

    status_code = res.get('status_code')
    specimen = res.get('data')

    assert status_code == 200
    assert specimen.specimen_pid == specimen_pid

    print(f"Generated specimen pid: {specimen_pid}")