import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_QUERY)
        self.connection.commit()

    def sql_insert_users(self, telegram_id,
                         username, first_name, last_name):
        self.cursor.execute(sql_queries.START_INSERT_USER_QUERY,
                            (None, telegram_id, username, first_name, last_name)
                            )
        self.connection.commit()

    def sql_admin_select_username_users_table(self):
        self.cursor.row_factory = lambda cursor, row: {
            "telegram_id": row[0],
            "username": row[1],
            "first_name": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY
        ).fetchall()

    def sql_insert_user_form(self, telegram_id,
                             nickname, age, bio, photo):
        self.cursor.execute(sql_queries.INSERT_USER_FORM_QUERY,
                            (None, telegram_id, nickname, age, bio, photo)
                            )
        self.connection.commit()

    def sql_select_user_form_by_telegram_id(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "bio": row[4],
            "photo": row[5],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_BY_TELEGRAM_ID_QUERY, (telegram_id,)
        ).fetchall()