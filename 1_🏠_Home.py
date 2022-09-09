import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = ":house:",
)

st.title("Main Page")
st.sidebar.success("Welcome to the main page!")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
    
my_input = st.text_input("Input a text here",st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You submitted:", my_input)