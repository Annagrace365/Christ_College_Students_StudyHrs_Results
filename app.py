import streamlit as st
import joblib

model=joblib.load("logistic_regression_studyhours_model.pkl")
st.title("Student Pass/Fail based on Study Hours")
hours=st.number_input("Enter Study Hours:", min_value=0.0 ,max_value=15.0, value=5.0)
attendance=st.number_input("Enter Attendance:", min_value=0 ,max_value=100, value=90)
if st.button("Predict"):
  prediction=model.predict([[hours,attendance]])
  if prediction[0]==1:
    st.success("Pass")
  else:
    st.error("Fail")
