import streamlit as st
import preprocessor, helper
import pandas as pd

df = preprocessor.process()

# Create a sidebar with a dropdown menu
selected_value = st.sidebar.selectbox(
    'Select an option:',
    ['Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analyis'])

st.subheader('Main Table')
st.table(df)

if selected_value == 'Medal Tally':
    st.header('Medal Tally')






