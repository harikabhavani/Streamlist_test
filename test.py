import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.text_input("User Name")
file=st.file_uploader("Upload Files")
submit=st.button("Submit")
if submit:
    df = pd.read_csv(file)
    st.write("Output 1")
    output1=df.head()
    st.write(output1)
    st.write("Output 2")
    fig = plt.figure(figsize=(10,5))
    plt.scatter(df["PetalLengthCm"],df["SepalLengthCm"])
    plt.xlabel('Petal Length in cm', fontsize=16)
    plt.ylabel('Sepal Length in cm', fontsize=16)
    st.write(fig)
