import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

st.title("AI Career Explorer")

interests = st.text_input("Enter your interests (example: AI, maths, business)")

if st.button("Generate Careers"):

    prompt = f"""
    A student is interested in: {interests}.

    Suggest:
    1. 5 possible careers
    2. Skills they should learn
    3. 3 beginner projects they can build.

    Explain simply for a high school student.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
