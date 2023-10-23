from model.creature import Creature

_creatures = [
    Creature(name="yeti",
             description="Abominable Snowman",
             location="Himalayas"),
    Creature(name="bigboot",
             description="AKA Sasquatch, the New World Cousin Eddie of the yeti",
             location="North America"),
]

def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """Add an creature"""
    return creature

def modify(id, creature: Creature) -> Creature:
    """Partially modify an creature"""
    return creature

def replace(id, creature: Creature) -> Creature:
    """Completely replace an creature"""
    return creature

def delete(creature: Creature) -> bool:
    """Delete an creature; return None if it existed"""
    return None
