import streamlit as st
import requests as re
from time import sleep
from streamlit_utils import go_to


def finish_character_creation(data, game):
    url = "http://127.0.0.1:8000/create-char"
    with st.spinner("Wait for it...", show_time=True):
        try:
            response = re.post(url, json=data)
            if response.status_code == 200 or response.status_code == 201:
                st.success("✅ Character created!")
                sheet = response.json()
                game.atr = sheet["atr"]
                game.specs = sheet["specs"]
                game.status = sheet["status"]
                sleep(3)
                go_to("camp")
            else:
                st.error(f"❌ Server error: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Could not connect to the server: {e}")


def choose_path(path):
    st.session_state.path = path


def choose_alignment(alignment):
    st.session_state.alignment = alignment


alignment_map = {
    "none": "Decide your fate.",
    "sun-born": "Sun Born",
    "moon-blessed": "Moon Blessed",
    "stars-gazer": "Stars Gazer",
    "land-dweller": "Land Dweller",
    "sea-voyager": "Sea Voyager",
    "sky-dreamer": "Sky Dreamer",
}

descriptions = {
    "sun-born": "Born graced by the sunlight, this creatures know too well how to take advantage over foes weakness...\n\n>Low Mana buff; Stronger elemental strikes",
    "moon-blessed": "Born with a touch of the moonlight, this specimens have a natural connection to the mana lines. \n\n>High Mana buff; Initial Charisma buff",
    "stars-gazer": "Pointed ears, and eagle eyes, the Star Gazers will see you days before you even appear.\n\n >Initial Attack buff; Crit multiplier buff",
    "land-dweller": "Drifters of the land, they know every aspect of this world.\n\n>Crafting and Harvesting buff; Low Health buff",
    "sea-voyager": "Pirates, Corsairs, ocean creatures and more... Sea Voyagers built their bodies with high agility to survive.\n\n>Initial Dexterity buff; Crit % buff; Low Health buff",
    "sky-dreamer": "Dreaming of realities yet to come, this mans train their bodies and minds to endure anything standing between them and their objective.\n\n>Initial Defense buff; Dmg mitigation; High Health buff",
    "none": "Choose your blessing, traveller...",
}


def new_game_window(game):
    st.set_page_config(layout="wide")

    if "path" not in st.session_state:
        st.session_state.path = ""
    if "alignment" not in st.session_state:
        st.session_state.alignment = "none"

    if st.button("<-", help="Go back to menu"):
        go_to("begin")
    st.title("New Game")
    st.header("Wich :orange[path] will you walk ? 🔸", divider="orange")
    st.write(f"### -> :orange[{st.session_state.path.capitalize()}]")
    st.html("<br>")

    col_e1, col_1, col_2, col_3, col_e2 = st.columns([0.6, 1, 1, 1, 0.6])

    with col_1:
        st.image("assets/character/ranger.png")
        st.button(
            "Ranger", use_container_width=True, on_click=choose_path, args=("ranger",)
        )

    with col_2:
        st.image("assets/character/mage_ekibi.png")
        st.button(
            "Mage", use_container_width=True, on_click=choose_path, args=("mage",)
        )

    with col_3:
        st.image("assets/character/warrior.png")
        st.button(
            "Fighter", use_container_width=True, on_click=choose_path, args=("fighter",)
        )

    st.html("<br><br>")
    st.header("Wich :violet[blessing] will you receive ? 🟪", divider="violet")
    alignment = alignment_map[st.session_state.alignment]
    st.write(f"### -> :violet[{alignment}]")
    st.html("<br><br>")

    b_col_1, b_col_2, b_col_3, b_col_4, b_col_5 = st.columns([0.6, 1, 2, 1, 0.6])

    with b_col_2:
        st.button(
            "Sun Born", width="stretch", on_click=choose_alignment, args=("sun-born",)
        )
        st.button(
            "Moon Blessed",
            width="stretch",
            on_click=choose_alignment,
            args=("moon-blessed",),
        )
        st.button(
            "Stars Gazer",
            width="stretch",
            on_click=choose_alignment,
            args=("stars-gazer",),
        )

    with b_col_3:
        st.info(descriptions.get(st.session_state.alignment, "Escolha um destino."))

    with b_col_4:
        st.button(
            "Land Dweller",
            width="stretch",
            on_click=choose_alignment,
            args=("land-dweller",),
        )
        st.button(
            "Sea Voyager",
            width="stretch",
            on_click=choose_alignment,
            args=("sea-voyager",),
        )
        st.button(
            "Sky Dreamer",
            width="stretch",
            on_click=choose_alignment,
            args=("sky-dreamer",),
        )

    st.html("<br><br>")
    st.header("What shall be your :red[strenghts] ❓", divider="red")
    st.write(f"### -> :red[15] points.")

    a_col_1, a_col_2, a_col_3 = st.columns([2, 1, 2])

    with a_col_2:
        strenght = st.number_input("Strenght", 0, 15, step=1, value=0, icon="⚔️")
        intelligence = st.number_input(
            "Intelligence", 0, 15, step=1, value=0, icon="🧠"
        )
        dexterity = st.number_input("Dexterity", 0, 15, step=1, value=0, icon="🥾")
        constitution = st.number_input("Constitution", 0, 15, step=1, value=0, icon="❤️")
        charisma = st.number_input("Charisma", 0, 15, step=1, value=0, icon="🫦")

        total_points = strenght + intelligence + dexterity + constitution + charisma

        if total_points > 15:
            st.warning(f"You have exceeded the 15 points limit.")
            can_post = False
        else:
            st.info(f"Remaining points: {15 - total_points}")
            can_post = True

    st.html("<br>")
    if st.button("Finish Creation💫", width="stretch", disabled=not can_post):
        payload = {
            "atr": {
                "strenght": strenght,
                "intelligence": intelligence,
                "dexterity": dexterity,
                "constitution": constitution,
                "charisma": charisma,
            },
            "specs": {
                "name": "to-be-decided",
                "char_class": st.session_state.path,
                "char_alignment": st.session_state.alignment,
            },
        }

        finish_character_creation(payload, game)
