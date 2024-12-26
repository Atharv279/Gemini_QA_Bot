from dotenv import load_dotenv
load_dotenv()  ##loading all the environment variables

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

  ## function to load gemini pro model and get respsonses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text  

##initilize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLm Application")

input=st.text_input("Input: ",key="Input")
submit=st.button("Ask the Question")

##When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response )