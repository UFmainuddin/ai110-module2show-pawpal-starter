# PawPal+ Project Reflection

## 1. System Design

### Core user actions

The three main actions in my system are:

- add a pet for one owner
- add care tasks to a specific pet
- generate and review today's schedule

**a. Initial design**

I started with 4 classes for the PawPal+ system.

- **Owner** stores the owner's name, available time, and the pets they manage.
- **Pet** stores the pet's basic details and the tasks for that pet.
- **Task** stores one care item with a time, duration, frequency, completion status, and priority.
- **Scheduler** reads tasks from the owner, sorts them, filters them, checks for conflicts, and builds the daily plan.

I chose these classes because they each had one clear job. This made the system easier to understand before I wrote the real logic.

**b. Design changes**

Yes, the design changed during implementation.

At first, the project only worked with one pet and very simple tasks. Later I changed `Owner` so it could manage multiple pets. I also changed `Task` so it could store a task time, a frequency like daily or weekly, a completion status, and a priority value. I changed the `Scheduler` too, because it needed methods for sorting, filtering, conflict detection, recurrence, persistence support, and next-slot suggestions. I made these changes because the assignment and the optional extensions needed a smarter system than the first draft.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler looks at the task date, task time, completion status, task priority, and the owner's available minutes for the day. It now sorts tasks by priority first and then by time. After that it adds tasks into the plan until there is no more time left.

I treated available time as the hard limit because a schedule should not go past the time the owner actually has. I also made priority important because some pet care tasks, like medication, should be handled before lower priority tasks like play time.

**b. Tradeoffs**

One tradeoff in my scheduler is that conflict detection only checks exact time matches. It does not calculate overlapping durations like a task from 8:00 to 8:30 and another from 8:15 to 8:45.

I think this tradeoff is reasonable for this version because it keeps the logic simple and easy to explain. It still catches a common scheduling problem without making the code too complex for this project.

## 3. AI Collaboration

**a. How I used AI**

I used AI for design brainstorming, class planning, test ideas, cleanup, and optional extensions. The most helpful prompts were short and direct, like asking what methods the scheduler should have, how to sort times in `HH:MM` format, how to save nested objects to JSON, and what edge cases should be tested.

The agent-style workflow was especially helpful for the optional extension where I added a next available slot algorithm. It helped me think in steps instead of trying to change everything at once.

**b. Judgment and verification**

I did not accept every AI idea exactly as it was given. One example was the early idea to keep the scheduler very simple and only work with one pet. I changed that idea because the assignment expected the owner to manage multiple pets and for the scheduler to work across all of them.

I checked the suggestions by reading the code carefully, running the CLI demo, and running `python -m pytest`. If the suggestion made the code harder to understand or did not match the project instructions, I changed it.

**c. Organization with separate chat sessions**

Using separate chat sessions helped me stay organized because each phase had a different goal. One chat could stay focused on system design, another on algorithms, and another on testing. This made it easier to compare ideas without mixing everything together.

**d. Lead architect takeaway**

My biggest lesson was that I still had to be the lead architect even when AI was helping. AI could suggest code fast, but I still had to decide what belonged in the system, what was too much, and what needed to be tested. The final responsibility was still mine.

## 4. Testing and Verification

**a. What I tested**

I tested task completion, task addition, sorting by time, filtering by pet, recurring daily task creation, conflict detection, priority-first scheduling, next available slot detection, JSON save and load, and schedule generation when time runs out.

These tests were important because they cover the main behaviors the app depends on. If one of these breaks, the schedule shown to the user could be confusing or wrong.

**b. Confidence**

My confidence level is 4 out of 5. The most important behaviors now have automated tests, and the results pass.

If I had more time, I would test more edge cases. I would test overlapping durations, editing tasks after they are created, and more date combinations for weekly recurrence.

## 5. Reflection

**a. What went well**

I am most satisfied with the way the backend classes work together now. The owner can manage multiple pets, each pet can keep its own tasks, the data can be saved to JSON, and the scheduler can work across all of them in one place.

**b. What I would improve**

If I had another iteration, I would improve the UI more. I would let the user edit or delete tasks, and I would show better calendar-style output instead of only tables and text.

**c. Key takeaway**

I learned that planning the system first made the coding part much easier. I also learned that AI works best when I give it a clear goal and then verify the result myself.

## 6. Optional Extensions

**a. Advanced algorithmic capability**

For the optional algorithm challenge, I added `find_next_available_slot()`. This method checks the current day, looks at the busy times, and returns the next time gap that can fit a new task. I also used that idea to suggest new times for skipped tasks.

**b. Data persistence**

For persistence, I added JSON save and load support to the data model. The app now remembers pets and tasks between runs by storing them in `data.json`.

**c. Advanced priority scheduling and UI**

I upgraded the schedule so it now sorts by priority first and then by time. I also added clear emoji-based priority labels in the UI to make the plan easier to scan.

**d. Professional formatting**

I improved the formatting in both the UI and the CLI demo. The app now has top-level metrics, cleaner tables, emoji task labels, and next-slot suggestions. The CLI output also uses structured table formatting now.

**e. Prompt comparison**

For the prompt comparison idea, I documented the comparison carefully instead of pretending I had tools that were not available here. If I compare two model styles for the next-slot algorithm, I think an OpenAI-style answer is usually more modular, while a Claude-style answer is often more conversational and explanatory. For this project I would keep the more modular version, because it fits better with a clean Python class design.
