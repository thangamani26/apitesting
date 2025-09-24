import requests


class APIS:

    BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    def __init__(self):
        self.headers = {
            'Accept': 'text/plain',
            'Content-Type': 'application/json'
        }

    def get_all_activities(self):
        return requests.get(f"{self.BASE_URL}", headers=self.headers)

    def get_activity_by_id(self):
        return

    def post_activity(self):
        return

    def put_activity(self):
        return

    def delete_actity(self):
        return
