from .init import conn, curs, IntegrityError
from model.explorer import Explorer
from errors import Missing, Duplicate

curs.execute("""create table if not exists explorer(
                name text primary key,
                nationality text)""")

def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], nationality=row[1])

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None

def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg = f"Explorer {name} not found")

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(explorer: Explorer) -> Explorer:
    qry = """insert into explorer (name, nationality)
             values (:name, :nationality)"""
    params = model_to_dict(explorer)
    try:
        res = curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg = f"Explorer {explorer.name} already exists")
    return get_one(explorer.name)

def modify(name: str, explorer: Explorer) -> Explorer:
    qry = """update explorer
             set nationality=:nationality, name=:name
             where name=:name0"""
    params = model_to_dict(explorer)
    params["name0"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(msg = f"Explorer {name} not found")

def delete(explorer: Explorer) -> bool:
    qry = "delete from explorer where name = :name"
    params = {"name": explorer.name}
    res = curs.execute(qry, params)
    return bool(res)