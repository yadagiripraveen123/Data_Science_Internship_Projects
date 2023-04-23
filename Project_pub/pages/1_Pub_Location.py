import streamlit as st
import pandas as pd
import numpy as np
import os

st.header("Display All Pubs Based on the Postal Code or Local Authority, display all the pubs in the area chosen")

# Loading the dataframe
FILE_DIR1 = os.path.dirname(os.path.abspath("__file__"))
data_path = os.path.join(FILE_DIR1,"resources","open_pubs_cleaned.csv")
pub_df = pd.read_csv(data_path)

#Displaying Pub Locations by post Code, Local Authority
unique=['Pub Name','Post Code', 'Local Authority']

option=st.radio(label="Select Below Option to See the Available Pubs",
                options=unique, horizontal=False)

if option=='Post Code':
    selected=st.selectbox(label='Select the ZipCode',options=pub_df['postcode'].unique())
    st.subheader(f"Total Pubs Found : {pub_df[pub_df['postcode']==selected].shape[0]}")
    st.map(data=pub_df[pub_df['postcode']==selected],  use_container_width=True)
elif option=='Pub Name':
    selected=st.selectbox(label='Select the Pub Name',options=pub_df['name'].unique())
    st.subheader(f"Total Pubs Found : {pub_df[pub_df['name']==selected].shape[0]}")
    st.map(data=pub_df[pub_df['name']==selected],  use_container_width=True)
elif option=='Local Authority':
    selected=st.selectbox(label='Select Local Authority',options=pub_df['local_authority'].unique())
    st.subheader(f"Total Pubs Found : {pub_df[pub_df['local_authority']==selected].shape[0]}")
    st.map(data=pub_df[pub_df['local_authority']==selected],  use_container_width=True)
