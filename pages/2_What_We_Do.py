import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(
    page_title="What We Do",
    page_icon="https://raw.githubusercontent.com/bee-io/bee-streamlit/main/assets/bee-logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open('./styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

df = pd.read_excel("./data/bee_data.xlsx",header=0)

df.drop(columns=[x for x in df.columns if not x in ['Site', 'Day', 'Month', 'Year', 'Genus']],inplace=True)

df['Timestamp'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df.drop(columns=['Year', 'Month', 'Day'], inplace=True)

coordinates = {
    'LelandFarm' : [42.063835,-71.249616],
    'SachemRock' : [42.018333,-70.951667],
    'DunrovinFarm' : [42.003699,-70.840169],
    'Christos' : [42.06734,-71.00287],
    'NativeMeadow' : [42.09107339,-71.04386531],
    'SoutheasternVocTech' : [42.183781,-71.101059],
    'Easton Powerline' : [42.183781,-71.101059],
    'StonehillFarm' : [42.183781,-71.101059],
    'VAHospital' : [42.183781,-71.101059],
    'BeaverBrook' : [42.183781,-71.101059],
}
df['lat'] = df['Site'].apply(lambda x: (coordinates[x][0] + np.random.rand(1)[0]/100 - 0.0005) if x in coordinates else None)
df['lon'] = df['Site'].apply(lambda x: (coordinates[x][1] + np.random.rand(1)[0]/100 - 0.0005) if x in coordinates else None)

df_count = df.groupby(['Genus', 'Site']).size().reset_index(name='Count')

info, bee_map = st.columns(2)
with info:
    st.title("Where do we collect data?")
    st.markdown(
        'We collect data on bee populations at various sites around Brockton. Our primary locations include farms, meadows, and other natural habitats where bees thrive. The data we gather helps us understand the health and diversity of bee populations in these areas.'
    )
    st.bar_chart(df_count, x="Site", y="Count", color="Genus", stack=True, horizontal=True)
with bee_map:
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=42.05,
            longitude=-70.97,
            zoom=9.8,
            pitch=50,
            bearing=-60,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=8,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[10, 40, 0, 80]',
                get_radius=20,
            ),
        ],
    ))

notice, graph = st.columns(2)
with notice:
    st.title("What are we noticing?")
    st.markdown(
        "We are observing a diverse range of bee species across our collection sites. The data shows that certain sites, such as Leland Farm and Sachem Rock, have higher populations of specific genera. This information is crucial for understanding the health of local bee populations and identifying areas that may need conservation efforts."
    )
with graph:
    st.title("Bee Population Trends")
    st.markdown(
        "The graph below illustrates the trends in the total bee population across all of our sites."
    )
    df_time = df.groupby('Timestamp').size().reset_index(name='Total Bees')
    st.line_chart(df_time, x='Timestamp', y='Total Bees')
    