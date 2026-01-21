from sqlalchemy import create_engine, inspect, text

class SqlMethods:

    __scripts = {
        "select": text("select * from subject"),
        "insert": text("insert into subject(\"subject_title\", \"subject_id\") values (:subject_title, :subject_id)"),
        "delete": text("delete from subject where \"subject_title\" = :subject_title"),
        "select by id": text("select * from subject where \"subject_id\" = :subject_id"),
        "update": text("update subject set \"subject_title\" = :new_title, \"subject_id\" = :new_id where \"subject_title\" = :title")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subject_list(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def insert(self, title, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert"], {"subject_title": title, "subject_id": id})
        conn.commit()
        conn.close()

    def get_subject(self, id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select by id"], {"subject_id": id})
        subject = result.mappings().all()
        conn.close()
        return subject
    
    def delete(self, title):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete"], {"subject_title": title})
        conn.commit()
        conn.close()

    def update(self, new_title, new_id, title):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update"], {"new_title": new_title, "new_id": new_id, "title": title})
        conn.commit()
        conn.close()
