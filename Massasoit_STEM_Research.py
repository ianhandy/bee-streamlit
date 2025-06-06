#Entry point for the Streamlit app
import streamlit as st

st.set_page_config(
    page_title="Massasoit STEM Research",
    layout="wide",
    initial_sidebar_state="expanded",
)

with open('./styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("Welcome to Massasoit STEM Research")

what_we_do, why_join = st.columns(2)
with what_we_do:
    st.header("What We Do")
    st.markdown("""
    - **Ecology Lab Activities:** Learn to identify and sort bees using lab equipment like microscopes.
    - **Journal Club:** Read and discuss scientific papers.
    - **Communication:** Create research questions and present your findings at conventions like ESA.
    - **DNA Analysis:** Analyze DNA from bee pollen to discover their foraging habits.
    - **Computer Science:** Manage databases, code statistics in R, and maintain this website.
    """)
with why_join:
    st.header("Why You Should Join")
    st.markdown("""
    - **Do Real Science**
    - **Learn to Read Scientific Papers**
    - **Coaching and Guidance**
    - **Community and Friendship**
    - **It's Paid**
    """)



