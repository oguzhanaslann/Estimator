import streamlit as st

class Task:
    __estimation = 0
    _name = ""
    def __init__(self, name: str, estimation: float):
        self._name = name
        self.__estimation = estimation
    
    def estimation(self):
        return self.__estimation
    
    def name(self):
        return self._name
    
    def __str__(self):
        return "%s: %.2f" % (self._name, self.__estimation)


def task_input_view(
    optimistic_estimation = 0,
    mean_estimation = 0,
    pesimistic_estimation = 0,
    risk_ratio = 0,
    position = 0     
):
    with st.container():
        title = st.text_input(label = 'Task Name', placeholder =  'Task name...', key = "task_name %s" % position)
        optimistic_col, mean_col2, pesimistic_col3= st.columns(3)   

        with optimistic_col:
            optimistic_estimation = st.number_input("optimistic", value=optimistic_estimation, placeholder="Type a number", key = "optimistic %s" % position )  
        with mean_col2:
            mean_estimation = st.number_input("Mean", value=mean_estimation, placeholder="Type a number", key = "mean %s" % position)
        with pesimistic_col3:
            pesimistic_estimation = st.number_input("Pesimistic", value=pesimistic_estimation, placeholder="Type a number", key = "pesimistic %s" % position)
            
        risk_ratio = risk_input(key = ("risk_ratio %s" % position))
        estimation = (optimistic_estimation + (4 * mean_estimation) + pesimistic_estimation) / 6
        risk_estimation = estimation * (1 + risk_ratio)
        return Task(title, risk_estimation)


def risk_input(
    label = 'Risk Ratio',
    default_value = 0.5,
    key = "risk_ratio"
    
):
    def_value = default_value
    if def_value > 1.0:
        def_value = 1.0
    elif def_value < 0.0:
        def_value = 0.0

    return st.slider(label,0.0,1.0, def_value, key = key)