class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age


class Owner:
    def __init__(self, name: str, available_minutes: int):
        self.name = name
        self.available_minutes = available_minutes
        self.pet = None
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class Task:
    def __init__(self, title: str, duration_minutes: int, priority: str):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


class Scheduler:
    def __init__(self, owner: Owner, pet: Pet, tasks: list):
        self.owner = owner
        self.pet = pet
        self.tasks = tasks
        self.plan = []
        self.skipped = []

    def generate_plan(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: PRIORITY_ORDER.get(t.priority, 99))
        time_remaining = self.owner.available_minutes
        self.plan = []
        self.skipped = []

        for task in sorted_tasks:
            if task.duration_minutes <= time_remaining:
                self.plan.append(task)
                time_remaining -= task.duration_minutes
            else:
                self.skipped.append(task)

        return self.plan

    def explain_plan(self):
        if not self.plan:
            return "No tasks could be scheduled within the available time."

        lines = [f"Daily care plan for {self.pet.name} (Owner: {self.owner.name}):"]
        lines.append(f"Available time: {self.owner.available_minutes} minutes\n")

        time_used = 0
        for task in self.plan:
            lines.append(
                f"- {task.title} [{task.priority} priority] — {task.duration_minutes} min"
                f" (included because priority is {task.priority})"
            )
            time_used += task.duration_minutes

        lines.append(f"\nTotal time used: {time_used} min")

        if self.skipped:
            lines.append("\nSkipped tasks (not enough time):")
            for task in self.skipped:
                lines.append(f"- {task.title} [{task.priority}] — {task.duration_minutes} min")

        return "\n".join(lines)
