import streamlit as st
import random

st.title("🎈 My new Random Number Generator app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

lesson01 = st.slider("Number of Questions in Lesson 01", 1, 12, 7)
lesson02 = st.slider("Number of Questions in Lesson 02", 1, 12, 6)
lesson03 = st.slider("Number of Questions in Lesson 03", 1, 12, 6)
lesson04 = st.slider("Number of Questions in Lesson 04", 1, 12, 11)
lesson05 = st.slider("Number of Questions in Lesson 05", 1, 12, 7)

lesson06 = st.slider("Number of Questions in Lesson 06", 1, 12, 2)
lesson07 = st.slider("Number of Questions in Lesson 07", 1, 12, 7)
lesson08 = st.slider("Number of Questions in Lesson 08", 1, 12, 5)
lesson09 = st.slider("Number of Questions in Lesson 09", 1, 12, 8)
lesson10 = st.slider("Number of Questions in Lesson 10", 1, 12, 1)

lesson11 = st.slider("Number of Questions in Lesson 11", 1, 12, 4)
lesson12 = st.slider("Number of Questions in Lesson 12", 1, 12, 7)
lesson13 = st.slider("Number of Questions in Lesson 13", 1, 12, 5)
lesson14 = st.slider("Number of Questions in Lesson 14", 1, 12, 7)
lesson15 = st.slider("Number of Questions in Lesson 15", 1, 12, 6)

lesson16 = st.slider("Number of Questions in Lesson 16", 1, 12, 11)
lesson17 = st.slider("Number of Questions in Lesson 17", 1, 12, 7)

if st.button('Generate Question'):
    st.write("Lesson 01 - Question Number: ", random.randint(1,lesson01))
    st.write("Lesson 02 - Question Number: ", random.randint(1,lesson02))
    st.write("Lesson 03 - Question Number: ", random.randint(1,lesson03))
    st.write("Lesson 04 - Question Number: ", random.randint(1,lesson04))
    st.write("Lesson 05 - Question Number: ", random.randint(1,lesson05))
    st.write("Lesson 06 - Question Number: ", random.randint(1,lesson06))
    st.write("Lesson 07 - Question Number: ", random.randint(1,lesson07))
    st.write("Lesson 08 - Question Number: ", random.randint(1,lesson08))
    st.write("Lesson 09 - Question Number: ", random.randint(1,lesson09))
    st.write("Lesson 10 - Question Number: ", random.randint(1,lesson10))
    st.write("Lesson 11 - Question Number: ", random.randint(1,lesson11))
    st.write("Lesson 12 - Question Number: ", random.randint(1,lesson12))
    st.write("Lesson 13 - Question Number: ", random.randint(1,lesson13))
    st.write("Lesson 14 - Question Number: ", random.randint(1,lesson14))
    st.write("Lesson 15 - Question Number: ", random.randint(1,lesson15))
    st.write("Lesson 16 - Question Number: ", random.randint(1,lesson16))
    st.write("Lesson 17 - Question Number: ", random.randint(1,lesson17))