from resources.models.asset import Asset
from utils import *


class Assets:

    def __init__(self, access_token):
        self.access_token = access_token

    def get_asset(self, guid):
        """
        Gets the metadata of the specified asset

        :param guid: The asset guid
        :return: Asset
        """
        res = send_request(RequestMethod.GET, self.access_token, f"/v1/assetmetadata/{guid}")
        return Asset.model_validate(res.get('data'))

    def create_asset(self, body: dict):
        res = send_request(RequestMethod.POST, self.access_token, f"/v1/assetmetadata", body)
        return Asset.model_validate(res.get('data'))

    def update_asset(self, guid: str, body: dict):
        res = send_request(RequestMethod.PUT, self.access_token, f"/v1/assetmetadata/{guid}", body)
        return Asset.model_validate(res.get('data'))
