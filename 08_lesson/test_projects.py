import uuid

import requests

from yougile_api import YougileApi


def test_create_project(api):
    title = f"Проект {uuid.uuid4()}"
    resp = api.create_project(title)

    assert resp.status_code == 201
    project_id = resp.json()["id"]
    created = api.get_project(project_id).json()
    assert created["title"] == title


def test_create_project_without_title(api):
    resp = requests.post(
        f"{YougileApi.BASE_URL}/projects",
        json={},
        headers=api.headers,
    )

    assert resp.status_code == 400


def test_update_project(api):
    project_id = api.create_project(f"Старый {uuid.uuid4()}").json()["id"]
    new_title = f"Новый {uuid.uuid4()}"

    resp = api.update_project(project_id, new_title)

    assert resp.status_code == 200
    updated = api.get_project(project_id).json()
    assert updated["title"] == new_title


def test_update_nonexistent_project(api):
    resp = api.update_project(str(uuid.uuid4()), "Тест")

    assert resp.status_code == 404


def test_get_project(api):
    title = f"Проект {uuid.uuid4()}"
    project_id = api.create_project(title).json()["id"]

    resp = api.get_project(project_id)

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == project_id
    assert body["title"] == title


def test_get_nonexistent_project(api):
    resp = api.get_project(str(uuid.uuid4()))

    assert resp.status_code == 404
