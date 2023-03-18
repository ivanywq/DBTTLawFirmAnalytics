import streamlit as st

st.set_page_config(
    page_title="App",
    page_icon="👋",
)
st.sidebar.success("Select a page above.")


st.header("Home")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Date: 6 Mar 2023")
with col2:
    st.write("Time: 7:00pm - 10:30pm")
with col3:
    st.write("Location: YHPSL Seminar Room 2-05")

st.write("- Python 3.7+")
st.write("- Streamlit")