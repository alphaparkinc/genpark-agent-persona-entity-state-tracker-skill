from client import PersonaEntityStateTracker

tracker = PersonaEntityStateTracker()
tracker.update_slot("timezone", "UTC+8")
tracker.add_relation("Alice", "MANAGES", "Project_Titan")

print("Current Entity State:", tracker.get_state())
