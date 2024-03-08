import streamlit as st

# Custom CSS styling
import streamlit as st

# Define your CSS styles
custom_css = """
<style>
    /* Your CSS styles here */
    .title {
        color: #ADD8E6;
        background-color: black;
        padding: 10px;
        font-size: 24px;
        font-weight: bold;
    }
</style>
"""

# Streamlit app
st.write(f'<div class="title">Hello, Streamlit with Custom CSS!</div>', unsafe_allow_html=True)
st.write('This is a paragraph.')

# Apply CSS using the custom_css variable
st.write(custom_css, unsafe_allow_html=True)


# Your content here...

original_title = '<p style="font-family:Courier; color:#FFDAB9;font-size:40px;">hello mfers</p>'
st.markdown(original_title, unsafe_allow_html=True)


