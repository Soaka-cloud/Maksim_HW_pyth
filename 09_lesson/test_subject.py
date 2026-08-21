import os
import uuid

import pytest

from subject_table import SubjectTable


@pytest.fixture
def db():
    connection_string = os.getenv("DB_CONNECTION_STRING")
    if not connection_string:
        pytest.skip("Задайте DB_CONNECTION_STRING")
    return SubjectTable(connection_string)


def test_add_subject(db):
    subject_id = db.get_max_id() + 1
    title = f"Предмет {uuid.uuid4()}"

    db.create(subject_id, title)

    rows = db.get_by_id(subject_id)
    assert len(rows) == 1
    assert rows[0]["subject_id"] == subject_id
    assert rows[0]["subject_title"] == title

    db.delete(subject_id)


def test_update_subject(db):
    subject_id = db.get_max_id() + 1
    title = f"Предмет {uuid.uuid4()}"
    new_title = f"Обновлённый {uuid.uuid4()}"

    db.create(subject_id, title)
    db.update(subject_id, new_title)

    rows = db.get_by_id(subject_id)
    assert len(rows) == 1
    assert rows[0]["subject_title"] == new_title

    db.delete(subject_id)


def test_delete_subject(db):
    subject_id = db.get_max_id() + 1
    title = f"Предмет {uuid.uuid4()}"

    db.create(subject_id, title)
    db.delete(subject_id)

    rows = db.get_by_id(subject_id)
    assert len(rows) == 0
