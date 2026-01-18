import streamlit as st


def camp_window(game):
    st.write(game.atr)
    if st.button("print"):
        print(game.atr)
