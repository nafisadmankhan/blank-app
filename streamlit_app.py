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
    st.write("Lesson 01 - Question Number: ", random_number)
    st.write("Lesson 02 - Question Number: ", random_number)
    st.write("Lesson 03 - Question Number: ", random_number)
    st.write("Lesson 04 - Question Number: ", random_number)
    st.write("Lesson 05 - Question Number: ", random_number)
    st.write("Lesson 06 - Question Number: ", random_number)
    st.write("Lesson 07 - Question Number: ", random_number)
    st.write("Lesson 08 - Question Number: ", random_number)
    st.write("Lesson 09 - Question Number: ", random_number)
    st.write("Lesson 10 - Question Number: ", random_number)
    st.write("Lesson 11 - Question Number: ", random.randint(1,4))
    st.write("Lesson 12 - Question Number: ", random_number)
    st.write("Lesson 13 - Question Number: ", random_number)
    st.write("Lesson 14 - Question Number: ", random_number)
    st.write("Lesson 15 - Question Number: ", random_number)
    st.write("Lesson 16 - Question Number: ", random_number)
    st.write("Lesson 17 - Question Number: ", random_number)
