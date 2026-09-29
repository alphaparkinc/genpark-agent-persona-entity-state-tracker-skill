"""Persona & Entity Relation State Tracker.
100% Python Standard Library.
"""

class PersonaEntityStateTracker:
    """Maintains persistent user profile attributes and entity relational graphs."""
    def __init__(self):
        self.profile = {}
        self.relations = {}

    def update_slot(self, slot_name, value):
        self.profile[slot_name] = value

    def add_relation(self, entity_a, relation, entity_b):
        self.relations[f"{entity_a}:{entity_b}"] = relation

    def get_state(self):
        return {"profile": self.profile, "relations": self.relations}
