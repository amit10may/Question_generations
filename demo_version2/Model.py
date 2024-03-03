import streamlit as st


st.title("GenAi For Question Generations")
st.sidebar.success("select a page above")

if 'Model' not in st.session_state:
    st.session_state["Model"] = "gpt-4"

Model = st.selectbox(
    "Select the model you want to use.",
    ("gpt-4","llama2(Coming soon)")
)

st.session_state['Model'] = Model
