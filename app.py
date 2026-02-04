import streamlit as st
from AircraftClass import Aircraft

st.set_page_config(page_title="Aircraft Boarding", page_icon="✈️", layout="centered")

st.title("✈️ Aircraft Boarding GUI")

# --- Create / reset plane ---
with st.sidebar:
    st.header("Aircraft Setup")
    model = st.text_input("Model", value="Airbus A320")
    capacity = st.number_input("Capacity", min_value=1, max_value=500, value=2, step=1)

    if st.button("Create / Reset aircraft", type="primary"):
        st.session_state.plane = Aircraft(model, capacity)
        st.toast("Aircraft created ✅")

# Create default plane on first run
if "plane" not in st.session_state:
    st.session_state.plane = Aircraft("Airbus A320", 2)

plane: Aircraft = st.session_state.plane

# --- Main panel ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Board passenger")
    passenger_name = st.text_input("Passenger name", placeholder="e.g., Muath")

    if st.button("Board", use_container_width=True):
        ok = plane.board_passenger(passenger_name)
        if ok:
            st.success(f"{passenger_name.strip()} boarded ✅")
        else:
            if not (passenger_name or "").strip():
                st.warning("Please type a passenger name.")
            else:
                st.error("Plane is full ❌ (capacity reached)")


with col2:
    st.subheader("Status")
    st.metric("Passenger count", plane.passenger_count())
    st.metric("Capacity", plane.capacity)

# Passenger list
st.divider()
st.subheader("Passengers")

if plane.passengers:
    st.write(plane.passengers)
else:
    st.info("No passengers yet. Add someone using the form above.")

# Remove passenger feature (optional but helpful)
st.divider()
st.subheader("Manage passengers")

if plane.passengers:
    to_remove = st.selectbox("Select passenger to remove", plane.passengers)
    if st.button("Remove selected passenger"):
        plane.passengers.remove(to_remove)
        st.success(f"Removed {to_remove} ✅")
        st.rerun()
else:
    st.caption("Nothing to manage yet.")
