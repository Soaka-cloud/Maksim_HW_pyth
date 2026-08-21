import os

import pytest

from yougile_api import YougileApi


@pytest.fixture
def api():
    token = os.getenv("YOUGILE_KEY")
    if not token:
        login = os.getenv("YOUGILE_LOGIN")
        password = os.getenv("YOUGILE_PASSWORD")
        if not (login and password):
            pytest.skip(
                "Задайте YOUGILE_KEY или YOUGILE_LOGIN и YOUGILE_PASSWORD"
            )
        token = YougileApi.get_token(login, password)
    return YougileApi(token)
