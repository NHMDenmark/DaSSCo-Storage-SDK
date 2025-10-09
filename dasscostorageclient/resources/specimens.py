from ..utils import *
from .models.specimen import SpecimenModel
import json

class Specimens:

    def __init__(self, access_token):
        self.access_token = access_token

    def create_or_update(self, specimenPID: str, body: dict):
        """
        Creates or updates the given specimen in ARS

        Args:
            specimenPID (str): The specimenPID of the specimen to be created/updated
            body (dict): The specimen to be created/updated in the given specimen

        Returns:
            The specimen object that contains the data of the created/updated specimen
        """
        res = send_request(
            RequestMethod.PUT,
            self.access_token,
            f"/v1/specimens/{specimenPID}",
            body)
        print(json.dumps(res.json(), indent=2))
        return {
            'data': SpecimenModel.model_validate(res.json()),
            'status_code': res.status_code
        }
    
