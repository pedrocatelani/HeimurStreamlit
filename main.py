import streamlit as st
import requests as re

from streamlit_utils import *
from views import *
from game import running_game

if "current_place" not in st.session_state:
    st.session_state.current_place = "begin"

# --- RENDERIZAÇÃO DAS CENAS ---
if st.session_state.current_place == "begin":
    begin_window(running_game)
if st.session_state.current_place == "new_game":
    new_game_window(running_game)
if st.session_state.current_place == "camp":
    camp_window(running_game)
if st.session_state.current_place == "hangouts":
    hangouts_window(running_game)
if st.session_state.current_place == "hangout-detail":
    hangout_detail_window(running_game)
