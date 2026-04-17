from datetime import date

from pawpal_system import Owner, Pet, Scheduler, Task


def print_table(title: str, columns: list[str], rows: list[list[str]]) -> None:
    widths = [len(column) for column in columns]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(str(value)))

    line = "+".join("-" * (width + 2) for width in widths)
    print(f"\n{title}")
    print("=" * len(title))
    print(line)
    print(
        " | ".join(f"{column:<{widths[index]}}" for index, column in enumerate(columns))
    )
    print(line)
    for row in rows:
        print(" | ".join(f"{str(value):<{widths[index]}}" for index, value in enumerate(row)))
    print(line)


def build_demo_owner() -> Owner:
    owner = Owner("Jordan", 90)

    mochi = Pet("Mochi", "dog", 3)
    mochi.add_task(
        Task("Morning walk", "07:30", 20, "daily", due_date=date.today(), priority="high")
    )
    mochi.add_task(
        Task("Breakfast", "08:00", 10, "daily", due_date=date.today(), priority="high")
    )

    luna = Pet("Luna", "cat", 5)
    luna.add_task(
        Task("Medication", "07:30", 5, "daily", due_date=date.today(), priority="high")
    )
    luna.add_task(
        Task("Play time", "18:00", 15, "once", due_date=date.today(), priority="low")
    )

    owner.add_pet(mochi)
    owner.add_pet(luna)
    return owner


def main() -> None:
    owner = build_demo_owner()
    scheduler = Scheduler(owner)
    plan = scheduler.generate_plan(date.today())

    plan_rows = [
        [
            task.time,
            task.pet_name,
            task.description,
            f"{task.duration_minutes} min",
            task.frequency,
            task.priority,
        ]
        for task in plan
    ]
    print_table(
        "Today's Schedule",
        ["Time", "Pet", "Task", "Duration", "Frequency", "Priority"],
        plan_rows,
    )

    if scheduler.conflicts:
        conflict_rows = [[warning] for warning in scheduler.conflicts]
        print_table("Conflict Warnings", ["Warning"], conflict_rows)

    filtered_rows = [
        [task.time, task.description, task.priority]
        for task in scheduler.filter_tasks(pet_name="Mochi", completed=False)
    ]
    print_table("Filtered Tasks For Mochi", ["Time", "Task", "Priority"], filtered_rows)

    next_slot = scheduler.find_next_available_slot(25, date.today())
    print(f"\nNext available 25-minute slot: {next_slot or 'No open slot'}")

    print("\nExplanation")
    print("===========")
    print(scheduler.explain_plan(date.today()))


if __name__ == "__main__":
    main()
