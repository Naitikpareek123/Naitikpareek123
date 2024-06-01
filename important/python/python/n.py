import streamlit as st
st.title('Welcome To :violet[learn And Build]')

choice= st.selectbox('Login/Signup',['Login','Sign Up'])
if choice=='Login':
    emaill=st.text_input('Email Adddress')
    Password=st.text_input('Password',type='password')
    
    st.button('Login')

else:
    emaill=st.text_input('Email Adddress')
    First_Name=st.text_input('First Name')
    Last_Name=st.text_input('Last Name')
    Password=st.text_input('Password',type='password')
    st.button('Sign Up')