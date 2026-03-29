import streamlit as st
from pawpal_system import Pet, Owner, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.markdown("A daily pet care planner that builds a schedule based on your available time and task priorities.")

st.divider()

# --- Owner + Pet Info ---
st.subheader("Owner & Pet Info")
col1, col2 = st.columns(2)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
    available_minutes = st.number_input("Available time today (minutes)", min_value=1, max_value=480, value=60)
with col2:
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Pet age", min_value=0, max_value=30, value=3)

st.divider()

# --- Task Management ---
st.subheader("Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

col_add, col_clear = st.columns([1, 1])
with col_add:
    if st.button("Add task"):
        st.session_state.tasks.append(
            {"title": task_title, "duration_minutes": int(duration), "priority": priority}
        )
with col_clear:
    if st.button("Clear all tasks"):
        st.session_state.tasks = []

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# --- Generate Schedule ---
st.subheader("Generate Schedule")

if st.button("Generate schedule"):
    if not st.session_state.tasks:
        st.warning("Add at least one task before generating a schedule.")
    else:
        owner = Owner(owner_name, int(available_minutes))
        pet = Pet(pet_name, species, int(age))
        tasks = [
            Task(t["title"], t["duration_minutes"], t["priority"])
            for t in st.session_state.tasks
        ]
        scheduler = Scheduler(owner, pet, tasks)
        scheduler.generate_plan()
        explanation = scheduler.explain_plan()

        st.success("Schedule generated!")
        st.markdown("### Plan")
        if scheduler.plan:
            for task in scheduler.plan:
                st.markdown(f"- **{task.title}** [{task.priority} priority] — {task.duration_minutes} min")
        else:
            st.warning("No tasks fit within the available time.")

        if scheduler.skipped:
            st.markdown("### Skipped Tasks (not enough time)")
            for task in scheduler.skipped:
                st.markdown(f"- {task.title} [{task.priority}] — {task.duration_minutes} min")

        st.markdown("### Explanation")
        st.text(explanation)
