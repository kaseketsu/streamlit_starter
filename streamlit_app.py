import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader('放入文件')
if uploaded_file is not None:
    dt = pd.read_csv(uploaded_file)
    st.write(dt)