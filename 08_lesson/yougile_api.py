import requests


class YougileApi:
    BASE_URL = "https://yougile.com/api-v2"

    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}

    @staticmethod
    def get_token(login, password):
        resp = requests.post(
            f"{YougileApi.BASE_URL}/auth/keys/get",
            json={"login": login, "password": password},
        )
        resp.raise_for_status()
        return resp.json()[0]["key"]

    def create_project(self, title):
        return requests.post(
            f"{self.BASE_URL}/projects",
            json={"title": title},
            headers=self.headers,
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            json={"title": title},
            headers=self.headers,
        )
