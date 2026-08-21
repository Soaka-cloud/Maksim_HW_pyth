from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "insert": text(
            "INSERT INTO subject(subject_id, subject_title) "
            "VALUES (:subject_id, :subject_title)"
        ),
        "update": text(
            "UPDATE subject SET subject_title = :subject_title "
            "WHERE subject_id = :subject_id"
        ),
        "delete": text(
            "DELETE FROM subject WHERE subject_id = :subject_id"
        ),
        "select by id": text(
            "SELECT * FROM subject WHERE subject_id = :subject_id"
        ),
        "get max id": text("SELECT MAX(subject_id) FROM subject"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, subject_id, subject_title):
        connection = self.__db.connect()
        connection.execute(
            self.__scripts["insert"],
            {"subject_id": subject_id, "subject_title": subject_title},
        )
        connection.commit()
        connection.close()

    def update(self, subject_id, subject_title):
        connection = self.__db.connect()
        connection.execute(
            self.__scripts["update"],
            {"subject_id": subject_id, "subject_title": subject_title},
        )
        connection.commit()
        connection.close()

    def delete(self, subject_id):
        connection = self.__db.connect()
        connection.execute(
            self.__scripts["delete"],
            {"subject_id": subject_id},
        )
        connection.commit()
        connection.close()

    def get_by_id(self, subject_id):
        connection = self.__db.connect()
        result = connection.execute(
            self.__scripts["select by id"],
            {"subject_id": subject_id},
        )
        rows = result.mappings().all()
        connection.close()
        return rows

    def get_max_id(self):
        connection = self.__db.connect()
        result = connection.execute(self.__scripts["get max id"])
        max_id = result.scalar()
        connection.close()
        return max_id
