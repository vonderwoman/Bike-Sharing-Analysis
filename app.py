import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Bike Analysis",
                   page_icon=":bar_chart:",
                   layout="wide")

# Get list of files in output folder
output_folder = 'Output'
files = os.listdir(output_folder)

# Add sidebar with options
st.sidebar.title('Please Select the Visuals Here:')
options = ['All'] + files
selected_option = st.sidebar.selectbox('', options)

# Display selected image(s)
st.title('Bike Analysis Dashboard')
st.header('Visualizations')
if selected_option == 'All':
    for file in files:
        image = Image.open(os.path.join(output_folder, file))
        st.image(image, caption=file, use_column_width=True)
else:
    image = Image.open(os.path.join(output_folder, selected_option))
    st.image(image, caption=selected_option, use_column_width=True)
