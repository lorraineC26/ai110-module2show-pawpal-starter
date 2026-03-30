import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# --- Session state: create objects once, reuse them on every rerun ---
if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name, time_available=120, preferences={"prefer_morning": True})

if "pet" not in st.session_state:
    st.session_state.pet = Pet(pet_name, species, age=3, health_notes="")
    st.session_state.owner.add_pet(st.session_state.pet)

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(st.session_state.owner)

# Sync widget values to existing objects on every rerun
st.session_state.owner.name = owner_name
st.session_state.pet.name = pet_name
st.session_state.pet.species = species

st.markdown("### Tasks")
st.caption("Add a few tasks. These feed into the scheduler.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    preferred_time = st.selectbox("Time of day", ["morning", "afternoon", "evening", "any"])

if st.button("Add task"):
    new_task = Task(
        name=task_title,
        category="general",
        duration=int(duration),
        priority=priority,
        preferred_time=preferred_time,
        pet_name=st.session_state.pet.name,  # snapshot name at add time
    )
    st.session_state.pet.add_task(new_task)
    st.success(f"Added: {new_task}")

current_tasks = st.session_state.pet.tasks
if current_tasks:
    st.write("Current tasks:")
    st.table([t.to_dict() for t in current_tasks])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    if not st.session_state.pet.tasks:
        st.warning("Add at least one task before generating a schedule.")
    else:
        schedule = st.session_state.scheduler.generate_schedule()
        st.success(f"Schedule built! Total time: {schedule.total_duration} min")
        st.table(schedule.to_dict_list())

        st.markdown("#### Why each task was chosen")
        for task_name, reason in schedule.get_reasoning().items():
            st.markdown(f"- **{task_name}**: {reason}")
