from utils import *


class Institutions:

    def __init__(self, access_token):
        self.access_token = access_token

    def list_institutions(self):
        """
        Gets all institutions
        """
        return send_request(RequestMethod.GET, self.access_token, "/v1/institutions").get('data')

    def get_institution(self, name: str):
        """
        Gets the specified institution

        :param name: The name of the institution
        :return: Asset
        """
        return send_request(RequestMethod.GET, self.access_token, f"/v1/institutions/{name}").get('data')

    def create_institution(self, name: str):
        """
          Creates an institution

          Args:
              name: The name of the institution
        """
        body = {
            'name': name,
        }
        return send_request(RequestMethod.POST, self.access_token, "/v1/institutions", body).get('data')
