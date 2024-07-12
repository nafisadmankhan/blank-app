import streamlit as st
import random

st.title("🎈 My new Random Number Generator app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Lesson 11
random_number = random.randint(1,4)

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

if st.button('Generate Question'):
    st.write("Lesson 11", random_number)
