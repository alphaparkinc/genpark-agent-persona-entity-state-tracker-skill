# genpark-agent-persona-entity-state-tracker-skill

Agent Skill implementing **Persistent Persona Profiles & Relational Entity State Tracking** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Utterance["User Dialogue Input"] --> SlotMatcher["Slot Extraction & Attribute Normalizer"]
    SlotMatcher --> Profile["User Persona Profile Map"]
    Utterance --> RelExtractor["Entity Relational Triples"]
    RelExtractor --> RelGraph["Entity Relation Adjacency Graph"]
    Profile & RelGraph --> UnifiedState["Unified Agent Identity & Context State"]
```
