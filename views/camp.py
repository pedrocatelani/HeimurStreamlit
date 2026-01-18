import streamlit as st


def camp_window(game):
    st.write(game.atr)
    st.write(game.status)
    st.write(game.specs)
    if st.button("print"):
        print(game.atr)
