import streamlit as st
import re

st.markdown("# Form Validation Project")

name = st.text_input("Enter your name")
valid_name = re.fullmatch("[A-Za-z][a-zA-Z0-9]*",name)

dob = st.text_input("Enter your Date Of Birth (MM-DD-YYYY)")
valid_dob = re.fullmatch(r"(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])-(?:[0-9]{4})" ,dob)

email = st.text_input("Enter valid email")
valid_email = re.fullmatch(r"\b[a-zA-Z][a-zA-Z0-9]*@[a-zA-Z]+.[a-zA-Z]{2,3}\b",email)

number = st.text_input("Enter 10-digit mobile number")
valid_num = re.fullmatch(r"\b[0-9]{10}\b",number)

if st.button("SUBMIT"):
    if valid_name and valid_dob and valid_email and valid_num:
        st.success("All input data is valid")
        st.markdown(f"name : {name}")
        st.markdown(f"DOB : {dob}")
        st.markdown(f" email : {email}")
        st.markdown(f" mobile no . : {number}")
    else:
        if not valid_name:
            st.error("enter valid name")
        if not valid_dob:
            st.error("enter valid DOB")
        if not valid_email:
            st.error("enter valid email")
        if not valid_num:
            st.error("enter valid mobile number")
        





