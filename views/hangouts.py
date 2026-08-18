import json
import streamlit as st
from streamlit_utils import go_to


def render_hangout_card(name, game):
    with open(f"assets/companions/{name.lower()}/bond_details.json", "r") as file:
        details = json.load(file)["available"]
    bond_level = 0
    for rel in game.relationships:
        if name in rel:
            bond_level = rel[name]
            break

    col_1, col_2 = st.columns([1, 2])
    with col_1:
        st.image(f"assets/companions/{name.lower()}/token.png", width=200)
    with col_2:
        st.write(f"### :green[{name}]")

        if bond_level < 2:
            st.write("??????")
        else:
            st.write(details)

        st.write(f":yellow[Current bond level: {bond_level}]")
        col_3, col_4 = st.columns([1, 1])
        with col_3:
            st.button(
                f"Hangout with {name}",
                help="Doing this will make time pass...",
                key=f"{name}-hangout",
            )
        with col_4:
            r = game.relationships_list()
            if name in r:
                if st.button(f"See bond benefits", key=f"{name}-benefits"):
                    game.inspect_event = name
                    go_to("hangout-detail")
    st.html("<br>")


def render_bond_bennefit(dict, game):
    level = int(list(dict.keys())[0])
    bennefit = dict[str(level)]
    bond_level = 0
    for rel in game.relationships:
        if game.inspect_event in rel:
            bond_level = rel[game.inspect_event]
            break

    if level <= bond_level:
        st.write(f"### Relationship level :green[{level}]")
        st.write(bennefit)
    elif level == bond_level + 1:
        st.write(f"### Relationship level :orange[{level}]")
        st.write(bennefit)
    else:
        st.write(f"### Relationship level :red[{level}]")
        st.write(">Hangout more to find out")
    st.html("<br>")


def hangouts_window(game):
    st.set_page_config(layout="wide")
    if st.button("<-", help="Go to Camp"):
        go_to("camp")
    st.title("Available Hangouts 👋")

    if game.events:
        col_1, col_2 = st.columns([1.2, 1])
        with col_1:
            for event in game.events:
                render_hangout_card(event, game)

    else:
        st.write("# Oh!")
        st.write("## There are :red[no available] hangouts right now...")
        st.write("### Try comming back :orange[later] today")
        if st.button("Go back", width="stretch"):
            go_to("camp")


def hangout_detail_window(game):
    st.set_page_config(layout="centered")

    char = game.inspect_event
    with open(f"assets/companions/{char.lower()}/bond_details.json", "r") as file:
        details = json.load(file)

    col_1, col_2 = st.columns([0.2, 3])
    with col_1:
        if st.button("<-", help="Go to Hangouts"):
            go_to("hangouts")
    with col_2:
        if st.button("⛺", help="Go to Camp"):
            go_to("camp")
    st.title("Bond details")
    st.header(char, divider="green")
    st.write(f":orange[{details["role"]}]")
    st.write(f":blue[{details["description"]}]")
    for l in details["bennefits"]:
        render_bond_bennefit(l, game)
