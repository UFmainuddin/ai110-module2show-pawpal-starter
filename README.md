# PawPal+ (Module 2 Project)

PawPal+ is a Streamlit app for planning pet care across multiple pets. It lets an owner add pets, assign care tasks, save the data between runs, mark tasks complete, and generate a daily schedule that fits inside the time they have available.

## Features

- Add and manage multiple pets in one owner profile
- Add tasks with a date, time, duration, frequency, priority, and completion status
- Sort tasks by time or by priority first and then time
- Filter tasks by pet name or completion status
- Detect exact-time conflicts and show warning messages
- Automatically create the next daily or weekly task when a recurring task is completed
- Generate a daily plan that fits inside the owner's available minutes
- Show a readable explanation of scheduled tasks, skipped tasks, and conflicts
- Save and load the owner, pets, and tasks from `data.json`
- Suggest the next available open slot for a task duration

## Smarter Scheduling

The scheduler now has these algorithmic features:

- `sort_by_time()` returns tasks in chronological order by date and time
- `sort_by_priority_then_time()` ranks high priority tasks before medium and low priority tasks
- `filter_tasks()` narrows the task list by pet name or completion status
- `mark_task_complete()` handles recurrence by creating the next daily or weekly task
- `detect_conflicts()` returns warnings when two tasks happen at the exact same time
- `find_next_available_slot()` finds the next open gap in the day that can fit a task
- `suggest_reschedule_slots()` gives a next-slot suggestion for skipped tasks

The daily plan is now priority-based. It sorts tasks by priority first and then by time, so urgent care like medication is placed before less important tasks.

## Optional Extensions Completed

### Challenge 1: Advanced Algorithmic Capability

I added a new scheduling method called `find_next_available_slot()`. This method looks at the tasks already planned for a day and finds the next open time gap that can fit a new task. I also used it in `suggest_reschedule_slots()` so skipped tasks can show a recommended new start time.

### Challenge 2: Data Persistence

I added JSON persistence to the `Owner` class with:

- `save_to_json()`
- `load_from_json()`
- `to_dict()` and `from_dict()` helpers across the data model

The Streamlit app now loads from `data.json` on startup and saves automatically after changes.

### Challenge 3: Advanced Priority Scheduling and UI

I upgraded the scheduler to sort by priority first and then by time. I also updated the UI to show clear priority badges:

- `?? High`
- `?? Medium`
- `?? Low`

### Challenge 4: Professional UI and Output Formatting

I improved the presentation in both the app and CLI:

- Streamlit metrics at the top for pets and tasks
- emoji-based task labels for better readability
- cleaner data tables with status and frequency badges
- structured CLI table output in `main.py`
- next-slot suggestions shown in the app when the day is full

### Challenge 5: Prompt Comparison

I added a prompt comparison discussion in `reflection.md`. In this environment I only had one coding agent available, so I wrote the comparison section honestly as a reasoning comparison instead of pretending I ran a live second-model tool here.

## Demo

Run the CLI demo script:

```bash
python main.py
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Demo preview:

![PawPal+ demo](demo_screenshot.png)

## Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

The tests now cover:

- task completion status changes
- task addition to a pet
- chronological sorting
- filtering by pet
- recurring daily task creation
- conflict detection
- schedule generation with skipped tasks when time runs out
- priority-first scheduling
- next available slot detection
- JSON save and load behavior

Confidence Level: 4/5 stars. The core logic and the optional features are tested and working, but I would still test more edge cases like overlapping durations, invalid saved data, and more UI editing flows.

## Project Files

- `pawpal_system.py` - backend classes, persistence, and scheduling logic
- `main.py` - CLI demo script with formatted table output
- `app.py` - Streamlit UI
- `data.json` - saved application data between runs
- `tests/test_pawpal.py` - automated tests
- `uml.md` - Mermaid UML diagram
- `uml_final.png` - exported UML image
- `reflection.md` - project reflection

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
