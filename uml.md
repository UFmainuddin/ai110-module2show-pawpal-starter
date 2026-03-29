# PawPal+ UML Class Diagram

```
┌───────────────────────────┐
│           Owner           │
├───────────────────────────┤
│ - name: str               │
│ - available_minutes: int  │
│ - pet: Pet                │
│ - tasks: list             │
├───────────────────────────┤
│ + add_task(task: Task)    │
└───────────────────────────┘
           │ has 1
           ▼
┌───────────────────────────┐
│            Pet            │
├───────────────────────────┤
│ - name: str               │
│ - species: str            │
│ - age: int                │
└───────────────────────────┘

┌───────────────────────────┐
│           Task            │
├───────────────────────────┤
│ - title: str              │
│ - duration_minutes: int   │
│ - priority: str           │
└───────────────────────────┘

┌───────────────────────────┐
│         Scheduler         │
├───────────────────────────┤
│ - owner: Owner            │
│ - pet: Pet                │
│ - tasks: list[Task]       │
│ - plan: list[Task]        │
│ - skipped: list[Task]     │
├───────────────────────────┤
│ + generate_plan()         │
│ + explain_plan()          │
└───────────────────────────┘
```

## Relationships
- Owner **has** one Pet
- Scheduler **uses** Owner, Pet, and a list of Tasks
- Scheduler.**generate_plan()** sorts tasks by priority (high → medium → low) and fits them into available time greedily
- Scheduler.**explain_plan()** returns a human-readable summary including scheduled and skipped tasks

## Changes from initial design
- `Scheduler` gained two result attributes: `plan` and `skipped` (to store results after generating)
- `Pet` gained `age` attribute (needed by the UI)
- `Owner` gained `pet` attribute to hold a reference to the pet
