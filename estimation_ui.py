import streamlit as st
from components import task_input_view
from components import *

st.header("Estimator")

@st.cache_resource
def get_estimations(): 
    return []

for i in range(len(get_estimations())):
    task = task_input_view(position = i)
    risk_estimation = task.estimation()
    """
    """
    st.markdown(":green[Estimation]: %.2f" % risk_estimation)
    get_estimations()[i] = task

"""
"""
error_ratio = 0.0
if len(get_estimations()) > 0:
    st.subheader("Error ratio")
    error_ratio = risk_input(label="Error ratio",default_value=0.0)



add_col, calculate_col = st.columns(2)
with add_col: 
    if st.button("Add",use_container_width=True):
        get_estimations().append(Task("",0))
        st.rerun()

total = 0
with calculate_col:
    if len(get_estimations()) > 0 and st.button("Calculate",use_container_width=True):
        total = 0
        for task in get_estimations():
            total += task.estimation()

"""
"""
total = total * (1 + error_ratio)
st.markdown(":green[Total]: %.2f" % total)

