import streamlit as st
import os
from groq import Groq

def get_groq_response(user_input):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input}
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    return chat_completion.choices[0].message.content

# Streamlit app title
st.title("People of Determination Support App")

# Sidebar navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Chatbot", "Mental Support", "Fitness Tracking", "Education"])

if menu == "Home":
    st.write("## Welcome to the People of Determination Support App")
    st.write("This app provides support through smart tools for mental well-being, fitness tracking, and education.")

elif menu == "Chatbot":
    st.write("## AI Chatbot Support")
    user_input = st.text_input("Ask the chatbot any question:")
    if st.button("Ask"): 
        if user_input:
            response = get_groq_response(user_input)
            st.write("### Chatbot Response:")
            st.write(response)
        else:
            st.warning("Please enter a question.")

elif menu == "Mental Support":
    st.write("## Mental Support")
    st.write("Find resources and AI support for mental health.")
    st.write("- Mindfulness exercises")
    st.write("- Counseling resources")
    st.write("- Motivational content")

elif menu == "Fitness Tracking":
    st.write("## Fitness Tracking")
    weight = st.number_input("Enter your weight (kg):", min_value=0)
    height = st.number_input("Enter your height (cm):", min_value=0)
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / ((height / 100) ** 2)
            st.write(f"Your BMI is: {bmi:.2f}")
        else:
            st.warning("Please enter valid values for weight and height.")

elif menu == "Education":
    st.write("## Education")
    st.write("Access learning resources tailored for people of determination.")
    st.write("- Online courses")
    st.write("- Assistive learning tools")
    st.write("- Career guidance")
