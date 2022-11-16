import streamlit as st
from time import sleep 
import numpy as np

st.title('Welcome to the dangerzone.')

if "visibility" not in st.session_state:
    st.session_state.v2 = "hidden"
    st.session_state.v3 = "hidden"
    st.session_state.p2 = "slacker"
    st.session_state.p3 = "honestly this one is really hard I'm sorry"
    st.session_state.d2 = True
    st.session_state.d3 = True

def reset():
    sec = np.random.randint(1, 50)
    p = st.empty()
    p.text(f"You\'re a failure and nobody loves you. \n reloads in {sec} seconds :sad:...")
    st.session_state.v2 = "hidden"
    st.session_state.v3 = "hidden"
    st.session_state.p2 = "slacker"
    st.session_state.p3 = "honestly this one is really hard I'm sorry"
    st.session_state.d2 = True
    st.session_state.d3 = True
    sleep(sec)
    p.empty()


col1, col2, col3 = st.columns(3)

with col1:
    boo = st.text_input(
        "What does a ghost bring to the party?",
    )
    if boo:
        boo = boo.lower()[:3]
        if boo == 'boo':
            st.session_state.v2 = "visible"
            st.session_state.d2 = False
        else:
            reset()
        
            
with col2:
    wrong = st.text_input(" \
        Lot's of people have said \
        Lot's of stuff about \
        Lot's of things... and they are usually... ",
        label_visibility=st.session_state.v2,
        disabled=st.session_state.d2,
        placeholder=st.session_state.p2,
    ).lower()
    if wrong:
        if wrong == 'wrong': 
            st.session_state.v3 = "visible"
            st.session_state.d3 = False
        else:
            reset()

with col3:
    cat = st.text_input(
        "By Pauli exlusion, Max really shouldn't be in the same room as this question. What is the answer?",
        label_visibility=st.session_state.v3,
        disabled=st.session_state.d3,
        placeholder=st.session_state.p3,
    ).lower()
    hex = ''
    # hex = st.color_picker("or this", disabled=st.session_state.d3, label_visibility=st.session_state.v3)
    if cat or hex:
        if cat == 'black' or hex == '#000000':    
            st.write('You win! Choose your prize: 1) kinder bueno 2) a book on irreverant philosophy 3) ~6h Max\'s time to build a weird ML project')
        else:
            reset()

