import streamlit as st


def go_to(local):
    st.session_state.current_place = local
    st.rerun()
