import streamlit as st
import joblib as jl
import pandas as pd

knn_model = jl.load("knn.sav")

st.number_input("Sepal Length :", key="sl")
st.number_input("Sepal Width :", key="sw")
st.number_input("Petal Length :", key="pl")
st.number_input("Petal Width :", key="pw")
submitBtn = st.button("calculate")

sl = st.session_state.sl
sw = st.session_state.sw
pl = st.session_state.pl
pw = st.session_state.pw

if submitBtn:
    if sl > 0 and sw > 0 and pl > 0 and pw > 0:
        x = pd.DataFrame([[sl, sw, pl, pw]])
        predictY = knn_model.predict(x)
        if predictY == 0:
            st.write("The flower type is : Setotsa")
        elif predictY == 1:
            st.write("The flower type is : Versicolor")
        elif predictY == 2:
            st.write("The flower type is : Virginica")
        else:
            st.write("Nothing Found!")
    else:
        st.write("Inputs is not valid!")
