# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I designed 4 classes for the PawPal+ system:

- **Owner** — stores the owner's name and how many minutes they have available in the day. Responsible for holding the pet reference and a list of tasks.
- **Pet** — stores the pet's name, species, and age. Represents the animal being cared for.
- **Task** — stores a care task's title, duration in minutes, and priority level (low, medium, or high).
- **Scheduler** — takes an Owner, a Pet, and a list of Tasks. Responsible for generating a daily plan that fits within the owner's available time and explaining why each task was chosen.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, the design changed in a few small ways. The `Scheduler` class gained two new attributes — `plan` and `skipped` — to store the results of `generate_plan()` so they could be accessed separately by `explain_plan()` and the UI. The `Pet` class gained an `age` attribute and `Owner` gained a `pet` attribute, both needed once the Streamlit UI was connected and required richer data to display.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers two constraints: the owner's available time (in minutes) and each task's priority level (high, medium, or low). Tasks are sorted by priority first, then fit into the available time one by one. Time was chosen as the hard constraint because you cannot schedule more than what the day allows, while priority determines which tasks get included first.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler uses a greedy approach — it picks tasks in priority order and adds them as long as they fit. This means a large high-priority task could use up most of the time, leaving no room for several smaller lower-priority tasks. This tradeoff is reasonable because in pet care, critical tasks (like giving medication) should always come before optional ones (like enrichment activities), even if it means fewer tasks overall.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help me think about the design before writing any code. I asked it to suggest what classes I would need and what each class should do. I also used it to help me write the scheduling logic and the tests. The most helpful questions were simple ones like "what classes do I need?" and "how should the scheduler decide which tasks to include?"

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When the AI suggested the class design, I looked at each class and asked myself if it made sense for the pet care problem. For example, I checked that the Scheduler had everything it needed — the owner, the pet, and the tasks — before it could make a plan. I also ran the tests to make sure the code actually worked the way the AI said it would.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested 7 behaviors: that high-priority tasks are scheduled first, that the total scheduled time never exceeds available time, that tasks too long to fit are skipped, that an empty task list returns an empty plan, and that the explanation correctly lists task titles and skipped tasks. These tests are important because they verify the core scheduling rules — if any of them break, the app would produce incorrect or misleading plans for the user.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am confident the scheduler handles the core cases correctly since all 7 tests pass. Edge cases I would test next include: two tasks with the same priority and duration, a task with 0 minutes duration, available time set to 0, and a very large number of tasks to check performance.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the scheduling logic works. It sorts the tasks by priority and only adds a task if there is enough time left. This makes the app feel useful and realistic, because it works the same way a real person would plan their day.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had more time, I would let the user set a start time for the day and show each task with a specific time slot, like "8:00 AM - Walk (20 min)". Right now the plan just lists tasks in order without showing clock times.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that it is important to plan the design before writing code. When I knew what classes I needed and what each one did, writing the code was much easier. I also learned that AI is helpful for getting started, but I still needed to read the code and run the tests to make sure everything worked correctly.
