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
    
    st.write("### Additional Chatbot Tools")
    if st.button("Daily Affirmations"):
        st.write("Receive positive affirmations to start your day with motivation.")
    if st.button("Productivity Tips"):
        st.write("Get personalized productivity tips to stay organized and focused.")
    if st.button("Health Advice"):
        st.write("Ask the chatbot for health tips and general wellness advice.")

elif menu == "Mental Support":
    st.write("## Mental Support")
    st.write("Find resources and AI support for mental health.")
    
    if st.button("Mindfulness Exercises"):
        st.write("Explore guided meditation and breathing exercises to improve focus and relaxation.")
        st.write("Examples:")
        st.write("- [Headspace](https://www.headspace.com)")
        st.write("- [Calm](https://www.calm.com)")
    if st.button("Counseling Resources"):
        st.write("Access professional counseling services and self-help tools.")
        st.write("Examples:")
        st.write("- [BetterHelp](https://www.betterhelp.com)")
        st.write("- [Talkspace](https://www.talkspace.com)")
    if st.button("Motivational Content"):
        st.write("Watch motivational videos and read inspiring stories to uplift your mood.")
        st.write("Examples:")
        st.write("- [TED Talks](https://www.ted.com/talks)")
        st.write("- [Motivation Hub on YouTube](https://www.youtube.com/c/MotivationHub)")

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
    
    st.write("### Exercise Recommendations")
    if st.button("Stretching Exercises"):
        st.write("Perform simple stretching exercises to improve flexibility and reduce muscle tension.")
        st.write("Examples:")
        st.write("- [Stretching Guide](https://www.verywellfit.com/stretching-exercises-1230823)")
        st.write("- [Stretching Videos](https://www.youtube.com/results?search_query=stretching+exercises)")
    if st.button("Strength Training"):
        st.write("Engage in light strength training exercises to build muscle strength and endurance.")
        st.write("Examples:")
        st.write("- [Strength Training Tips](https://www.self.com/story/strength-training-exercises)")
        st.write("- [Strength Training Workouts](https://www.youtube.com/results?search_query=strength+training+workouts)")
    if st.button("Cardio Workouts"):
        st.write("Try low-impact cardio workouts like walking or swimming for cardiovascular health.")
        st.write("Examples:")
        st.write("- [Cardio Exercises](https://www.healthline.com/health/fitness-exercise/cardio-exercises-list)")
        st.write("- [Cardio Workout Videos](https://www.youtube.com/results?search_query=cardio+workouts)")

elif menu == "Education":
    st.write("## Education")
    st.write("Access learning resources tailored for people of determination.")
    
    if st.button("Online Courses"):
        st.write("Browse a variety of online courses specifically designed for different abilities and learning styles.")
        st.write("Examples:")
        st.write("- [Coursera](https://www.coursera.org)")
        st.write("- [edX](https://www.edx.org)")
    if st.button("Assistive Learning Tools"):
        st.write("Discover assistive tools such as screen readers, speech-to-text software, and more.")
        st.write("Examples:")
        st.write("- [Read&Write](https://www.texthelp.com/products/read-write/)")
        st.write("- [Dragon NaturallySpeaking](https://www.nuance.com/dragon.html)")
    if st.button("Career Guidance"):
        st.write("Get career advice and explore vocational training opportunities.")
        st.write("Examples:")
        st.write("- [CareerOneStop](https://www.careeronestop.org)")
        st.write("- [My Next Move](https://www.mynextmove.org)")
    if st.button("Scholarship Opportunities"):
        st.write("Find scholarships and financial aid options for educational advancement.")
        st.write("Examples:")
        st.write("- [Scholarships.com](https://www.scholarships.com)")
        st.write("- [Fastweb](https://www.fastweb.com)")
    if st.button("Learning Communities"):
        st.write("Join communities and forums to connect with peers and share learning experiences.")
        st.write("Examples:")
        st.write("- [Reddit Learning Communities](https://www.reddit.com/r/learnprogramming)")
        st.write("- [Khan Academy Discussions](https://www.khanacademy.org)")}]}
