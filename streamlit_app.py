import streamlit as st
import random

# Page Branding
st.set_page_config(page_title="Abyascus", page_icon="🧮")
st.image("1000493014.png", use_container_width=True)

st.title("🧮 Abyascus: The Math Odyssey")
st.write("Special Gift from **Prince Shaizu**")

# Scoring logic
if 'score' not in st.session_state:
    st.session_state.score = {'Hasan': 0, 'Laiba': 0}

choice = st.radio("Kaun khel raha hai?", ["Lion Hasan 🦁", "Owl Laiba 🦉"])
player = "Hasan" if "Hasan" in choice else "Laiba"

# Math Logic
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 10)

correct_ans = st.session_state.num1 + st.session_state.num2

st.subheader(f"Chalo {player}, batao:")
st.write(f"### {st.session_state.num1} + {st.session_state.num2} = ?")

user_input = st.number_input("Jawab likho:", step=1, key="math_in")

if st.button("Check Karein ✅"):
    if user_input == correct_ans:
        st.balloons()
        st.success("Sahi Jawab! +10 Points!")
        st.session_state.score[player] += 10
        del st.session_state.num1
        st.rerun()
    else:
        st.error(f"Galt jawab! Sahi jawab {correct_ans} tha.")

# Sidebar scoreboard
st.sidebar.header("🏆 Scoreboard")
st.sidebar.write(f"🦁 Hasan: {st.session_state.score['Hasan']}")
st.sidebar.write(f"🦉 Laiba: {st.session_state.score['Laiba']}")
