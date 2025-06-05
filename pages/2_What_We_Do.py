import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(page_title="We Love Bees", page_icon="https://raw.githubusercontent.com/bee-io/bee-streamlit/main/assets/bee-logo.png", layout="wide", initial_sidebar_state="expanded")

