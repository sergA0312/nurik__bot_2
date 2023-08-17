CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),        
        FIRST_NAME CHAR(50),        
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""
CREATE_USER_FORM_QUERY = """
        CREATE TABLE IF NOT EXISTS user_form
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        AGE INTEGER,
        BIO TEXT,
        PHOTO TEXT,
        UNIQUE (TELEGRAM_ID)
        )

"""
START_INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""

SELECT_USER_QUERY = """SELECT telegram_id, username, first_name FROM telegram_users"""

INSERT_USER_FORM_QUERY = """INSERT OR IGNORE INTO user_form VALUES (?,?,?,?,?,?)"""

SELECT_USER_FORM_BY_TELEGRAM_ID_QUERY = """SELECT * FROM user_form WHERE TELEGRAM_ID = ?"""