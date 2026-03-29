import pytest
from pawpal_system import Pet, Owner, Task, Scheduler


def make_scheduler(available_minutes, tasks):
    owner = Owner("Jordan", available_minutes)
    pet = Pet("Mochi", "dog", 3)
    return Scheduler(owner, pet, tasks)


def test_high_priority_task_included_first():
    tasks = [
        Task("Enrichment", 30, "low"),
        Task("Morning walk", 20, "medium"),
        Task("Medication", 10, "high"),
    ]
    scheduler = make_scheduler(60, tasks)
    plan = scheduler.generate_plan()
    assert plan[0].title == "Medication"


def test_tasks_fit_within_available_time():
    tasks = [
        Task("Walk", 30, "high"),
        Task("Feeding", 15, "high"),
        Task("Bath", 60, "medium"),
    ]
    scheduler = make_scheduler(60, tasks)
    plan = scheduler.generate_plan()
    total = sum(t.duration_minutes for t in plan)
    assert total <= 60


def test_task_skipped_when_no_time():
    tasks = [
        Task("Long walk", 90, "high"),
        Task("Feeding", 10, "medium"),
    ]
    scheduler = make_scheduler(30, tasks)
    plan = scheduler.generate_plan()
    titles = [t.title for t in plan]
    assert "Long walk" not in titles
    assert "Feeding" in titles


def test_empty_task_list():
    scheduler = make_scheduler(60, [])
    plan = scheduler.generate_plan()
    assert plan == []


def test_explain_plan_no_tasks():
    scheduler = make_scheduler(60, [])
    scheduler.generate_plan()
    explanation = scheduler.explain_plan()
    assert "No tasks" in explanation


def test_explain_plan_contains_task_titles():
    tasks = [
        Task("Medication", 10, "high"),
        Task("Walk", 20, "medium"),
    ]
    scheduler = make_scheduler(60, tasks)
    scheduler.generate_plan()
    explanation = scheduler.explain_plan()
    assert "Medication" in explanation
    assert "Walk" in explanation


def test_skipped_tasks_listed_in_explanation():
    tasks = [
        Task("Walk", 50, "high"),
        Task("Bath", 60, "low"),
    ]
    scheduler = make_scheduler(60, tasks)
    scheduler.generate_plan()
    explanation = scheduler.explain_plan()
    assert "Bath" in explanation
    assert "Skipped" in explanation
