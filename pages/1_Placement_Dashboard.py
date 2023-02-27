import streamlit as st

st.title("Placements Data Analysis")
st.header("Information about Placement Data")

st.text("""This data set consists of Placement data of students in our campus. 
It includes secondary and higher secondary school percentage and specialization. 
It also includes degree specialization, type and Work experience and salary offers to the placed students""")

st.header("Placement Data Analysis")
st.text("Analyzing the Placements Data of the Students of the Certain college")

import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "placement.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Placement_Data_Full_Class.csv")

st.title("Dashboard - Placement Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

departments = st.selectbox("Select:", df['hsc_s'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['hsc_s'] == departments], x="status")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['hsc_s'] == departments], y="salary")
col2.plotly_chart(fig_2, use_container_width=True)

col3, col4 = st.columns(2)

fig_3 = px.bar(df['degree_t'])
col3.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.scatter(df['salary'])
col4.plotly_chart(fig_4, use_container_width=True)

