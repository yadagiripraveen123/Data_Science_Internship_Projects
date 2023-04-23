import streamlit as st
import pandas as pd
import numpy as np
import os
import time

# Set the page layout to wide
st.set_page_config(layout="wide")

# Add some styling to the title and subtitle
st.markdown("<h1 style='text-align: center; color: #191970; font-weight: bold;'> Welcome to Open Pubs Finder Application </h1>", unsafe_allow_html=True)
st.subheader(":AliceBlue[Here You Can Find Pubs In United Kingdom To Have Some Drink And Chillout]")

st.markdown("This is :blue[Yadagiri Praveen kumar]")

# Load data
FILE_DIR1 = os.path.dirname(os.path.abspath("__file__"))
dir_of_interest = os.path.join(FILE_DIR1,"resources","data","open_pubs_cleaned.csv")
pub_df = pd.read_csv(dir_of_interest)
st.dataframe(pub_df)

#  Display some statistics about the dataset
st.subheader("Here are some statistics about the open pubs data")
stats=['mean', 'count of the datapoints']
opt=st.radio(label="Select below options to see total count",options=stats, label_visibility ="visible")
if opt=='mean':
    st.subheader(f"mean :Navy[{pub_df.mean().to_dict()}]")
elif opt=='count of the datapoints':
    st.subheader(f"count :Navy[{pub_df.count().to_dict()}]")
st.write(pub_df.describe())


#Unique Bars and Local Authorities
unique=['Total pubs', 'Number of Local Authorities','Number of Postal Code']

option=st.radio(label="Select below options to see total count",options=unique, label_visibility ="visible")
if option=='Total pubs':
    st.subheader(f"Total Pubs in United Kingdom :violet[{pub_df.name.nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total Post Codes in United Kingdom :violet[{pub_df.postcode.nunique()}]")
else:
    st.subheader(f"Total Local Authorities in United Kingdom :violet[{pub_df.local_authority.nunique()}]")


st.markdown("You can connect me through Github and Linkedin")
button = st.button("Click Here!")
if button == True:
    st.subheader("Let's Start :cool:")
    st.markdown("https://github.com/yadagiripraveen123")
    st.markdown("https://www.linkedin.com/in/yadagiripraveenkumar/")


