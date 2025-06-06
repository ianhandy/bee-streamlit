import streamlit as st

st.set_page_config(
    page_title="Who We Are",
    page_icon="https://raw.githubusercontent.com/bee-io/bee-streamlit/main/assets/bee-logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open('./styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.title("Who We Are")
st.markdown(
        "We are a group of scientists, educators, and students dedicated to gathering and sharing data about local bee populations. Our goal is to raise awareness about the importance of bees in our ecosystem and to contribute to research that helps protect these vital pollinators."
        " Through our efforts, we aim to inspire others to take action in their own communities to support bee populations and promote biodiversity."
    )
col1, col2, col3, col4 = st.columns(4)
with col1:
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
with col2:
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
with col3:
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
with col4:
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)
        st.image("https://pbs.twimg.com/profile_images/1052352768634175488/xWk0BzTw_400x400.jpg", width=150)


        
        
        
        



