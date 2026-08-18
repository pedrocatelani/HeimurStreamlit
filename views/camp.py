import streamlit as st
from streamlit_utils import (
    go_to,
    render_hp_bar,
    render_mana_bar,
    render_stance_bar,
    connection_post,
)


def camp_window(game):
    st.set_page_config(layout="centered")
    st.title("Camp ⛺")
    st.header("You are safe here, traveller.", divider="green")
    st.image("assets/places/viribus.png", width="stretch")
    st.write(":green[Take your time...]")
    st.write("⏳ :green[10] Days, Cicle :orange[1]")
    st.write("Primus, Eevening🌕")

    c_col_1, c_col_2 = st.columns([1, 1])
    with c_col_1:
        st.button(
            "Delve into the Dungeons", width="stretch", help="Current dungeon: Viribus"
        )
        if st.button(
            "Hangouts",
            width="stretch",
            help="Some friends might help in your journey...",
        ):
            payload = game.day_info
            game.events = connection_post("available-hangouts", data=payload)
            go_to("hangouts")
        st.button("Search Merchant", width="stretch", help="Watcha buyin' ?")

    with c_col_2:
        st.button("Gather Materials", width="stretch", help="Be sure to bring tools.")
        st.button("Crafting", width="stretch", help="Gather beforehand")
        st.button("Rest", width="stretch", help="Recover your status.")

    st.header("Current status 🔴", divider="red")
    render_hp_bar(game.status.get("current_hp"), game.status.get("max_hp"))
    col_1, col_2 = st.columns([1, 1])
    with col_1:
        render_mana_bar(game.status.get("current_mana"), game.status.get("max_mana"))
        st.button("Check Spells", width="stretch")
        st.button("Check Weapons", width="stretch")
    with col_2:
        render_stance_bar(
            game.status.get("current_stance"), game.status.get("max_stance")
        )
        st.button("Check Armor", width="stretch")
        st.button("Check Atributes", width="stretch")

    st.html("<br><br>")
    st.header("", divider="red")
    if st.button("Give Up.", width="stretch", help="You'll Loose everything."):
        go_to("begin")
