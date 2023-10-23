from model.explorer import Explorer

_explorers = [
    Explorer(name="Claude Hande",
             nationality="France"),
    Explorer(name = "Noah Weiser",
             nationality="Germany"),
]

def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer

def modify(id, explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    return explorer

def replace(id, explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer

def delete(explorer: Explorer) -> bool:
    """Delete an explorer; return None if it existed"""
    return None
