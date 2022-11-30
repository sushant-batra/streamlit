import streamlit as st
st.title("Odd or Even")
st.header("You can check whether a  number is odd or even")
number = st.number_input("Enter a positive integer that you wish to check")
if(st.button('Submit')):
    if (number.is_integer() and number>0):
        result = number%2
        if (result==1):
            st.title("Number is odd")
        else:
            st.title("Number is even")           
    else:
        st.title("Enter a valid number")