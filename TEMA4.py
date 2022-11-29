import pandas as pd
import streamlit as st
import datetime
import matplotlib.pyplot as plt

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create the title for the web app
st.title("**TEMA 4**")
expansión= st.expander("Alumno")
expansión.markdown("""
* **Autor:** Luis Camilo Angel Sesma
* **Matrícula:** A01253231
""")

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Listo! (Tienes los datos de UBER)")

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 12)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa para todos los viajes a las %s:00' % hour_to_filter)
st.map(filtered_data)

