import streamlit as st
import random

st.set_page_config(page_title="Abyascus", layout="centered")
st.title("🧮 Abyascus: The 3D Math Odyssey")

# Score tracking
if 'score' not in st.session_state:
    st.session_state.score = {'Hasan': 0, 'Laiba': 0}

choice = st.radio("Kaun khel raha hai?", ["Lion Hasan 🦁", "Owl Laiba 🦉"])

player = "Hasan" if "Hasan" in choice else "Laiba"
st.subheader(f"{choice} ki bari!")

# Level selection
level = st.select_slider("Apna Level Chuno", options=["Level 1", "Level 2", "Level 3"])

# Math Logic
if level == "Level 1":
    a, b = random.randint(1, 9), random.randint(1, 9)
    ques, ans = f"{a} + {b}", a + b
elif level == "Level 2":
    a, b = random.randint(10, 50), random.randint(1, 9)
    ques, ans = f"{a} + {b}", a + b
else:
    a, b = random.randint(10, 20), random.randint(2, 5)
    ques, ans = f"{a} × {b}", a * b

st.write(f"### Sawal: {ques} = ?")
user_ans = st.number_input("Jawab yahan likho", step=1, key=f"input_{player}")

if st.button("Check Jawab ✅"):
    if user_ans == ans:
        st.success("Sahi Jawab! +10 Points ⭐")
        st.session_state.score[player] += 10
    else:
        st.error(f"Try again! Sahi jawab {ans} tha.")

st.sidebar.header("🏆 Leaderboard")
st.sidebar.write(f"🦁 Hasan: {st.session_state.score['Hasan']}")
st.sidebar.write(f"🦉 Laiba: {st.session_state.score['Laiba']}")
  
