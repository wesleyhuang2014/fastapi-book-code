from sqlite3 import connect, IntegrityError
import os

_db_name = os.environ.get("CRYPTID_SQLITE_DB", "cryptid.db")
conn = connect(_db_name, check_same_thread=False)
curs = conn.cursor()