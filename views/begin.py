import streamlit as st
from streamlit_utils import go_to


def begin_window(game):
    st.set_page_config(layout="centered")
    st.title("Welcome, Traveller❗")
    st.header("What would you like to do?", divider="violet")
    st.html("<br>")

    col_1, col_2, col_3 = st.columns([1, 2, 1])

    with col_2:
        if st.button("Start a **new** Journey", width="stretch"):
            go_to("new_game")
        if st.button("See **old** friends", width="stretch"):
            go_to("load_game")
        if st.button("Learn more **about** this world", width="stretch"):
            go_to("about")

    st.html("<br><br><br><br>")
    st.write(":violet[@catelanirocha]")
    st.write("Heimur Game 4.0")
