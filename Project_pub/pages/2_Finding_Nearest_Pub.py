import streamlit as st
import pandas as pd
import numpy as np
import os

#Page Header
st.header("Search for the Nearest Pubs")

# Load data
FILE_DIR1 = os.path.dirname(os.path.abspath("__file__"))
data_path = os.path.join(FILE_DIR1,"resources","open_pubs_cleaned.csv")
pub_df = pd.read_csv(data_path,'r')

#Take input -latitude and longitude
col1,col2=st.columns(2)
with col1:
    latitude = st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)
with col2:
    longitude = st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)


search_location=np.array((latitude,longitude))
original_location=np.array([pub_df['latitude'],pub_df['longitude']]).T
dist=np.sqrt(np.sum((original_location-search_location)**2, axis=1))
pub_df['Distance']=dist

nearest=st.slider(label="How Many Nearest Pub You Want to See", min_value=1, max_value=100, value=5)
data_df=pub_df.sort_values(by='Distance', ascending=True)[:nearest]

st.subheader(f"{nearest} Nearest Pubs:")
st.map(data=data_df, zoom=None, use_container_width=True)
st.table(data_df[['name','address','local_authority']])