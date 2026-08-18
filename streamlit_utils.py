import streamlit as st
import requests as re


def go_to(local):
    st.session_state.current_place = local
    st.rerun()


def connection_post(url, data):
    url_full = f"http://127.0.0.1:8000/{url}"
    try:
        response = re.post(url_full, json=data)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            st.error(f"❌ Server error: {response.text}")
    except Exception as e:
        st.error(f"⚠️ Could not connect to the server: {e}")


def render_hp_bar(current, maximum):
    percent = max(0, min(100, (current / maximum) * 100))

    if percent > 65:
        color = "#2ecc71"
    elif percent > 25:
        color = "#f1c40f"
    else:
        color = "#e74c3c"

    hp_html = f"""
    <div style="background-color: #444; border-radius: 10px; width: 100%; height: 20px; border: 1px solid #000;">
        <div style="background-color: {color}; width: {percent}%; height: 100%; border-radius: 9px; transition: width 0.5s;">
        </div>
    </div>
    <p style="text-align: right; margin-top: 5px; margin-bottom: 0">{current}/{maximum} Hit Points</p>
    """
    st.html(hp_html)


def render_mana_bar(current, maximum):
    percent = max(0, min(100, (current / maximum) * 100))

    if percent > 65:
        color = "#11a5fa"
    elif percent > 25:
        color = "#4126b9"
    else:
        color = "#711c99"

    hp_html = f"""
    <div style="background-color: #444; border-radius: 10px; width: 100%; height: 20px; border: 1px solid #000;">
        <div style="background-color: {color}; width: {percent}%; height: 100%; border-radius: 9px; transition: width 0.5s;">
        </div>
    </div>
    <p style="text-align: right; margin-top: 5px; margin-bottom: 0">{current}/{maximum} Mana Pool</p>
    """
    st.html(hp_html)


def render_stance_bar(current, maximum):
    percent = max(0, min(100, (current / maximum) * 100))

    if percent > 65:
        color = "#fbff1a"
    elif percent > 25:
        color = "#cea800"
    else:
        color = "#eb7e18"

    hp_html = f"""
    <div style="background-color: #444; border-radius: 10px; width: 100%; height: 20px; border: 1px solid #000;">
        <div style="background-color: {color}; width: {percent}%; height: 100%; border-radius: 9px; transition: width 0.5s;">
        </div>
    </div>
    <p style="text-align: right; margin-top: 5px; margin-bottom: 0">{current}/{maximum} Stance</p>
    """
    st.html(hp_html)
