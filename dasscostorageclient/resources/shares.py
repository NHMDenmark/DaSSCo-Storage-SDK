from utils import *
from resources.models.sambainfo import SambaInfo


class Shares:

    def __init__(self, access_token):
        self.access_token = access_token

    def disconnect_share(self, share_name: str, asset_guid: str):
        body = {
            'shareName': share_name,
            'assetGuid': asset_guid
        }
        res = send_request(RequestMethod.POST, self.access_token, "/v1/shares/disconnect", body)
        return SambaInfo.model_validate(res.get('data'))

    def open_share(self):
        pass

    def reopen_share(self):
        pass

    def close_share(self, share_name: str, sync=False):
        body = {
            'shareName': share_name,
        }
        res = send_request(RequestMethod.POST, self.access_token, f"/v1/shares/close?syncERDA={sync}", body)
        return SambaInfo.model_validate(res.get('data'))
