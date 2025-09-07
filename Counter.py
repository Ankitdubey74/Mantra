import streamlit as st
import base64

# Page config
st.set_page_config(page_title="🕉️ Mantra Counter", layout="centered")

# Custom background with OM animation (GIF / SVG base64)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/gif;base64,{b64}");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Button styling */
        div.stButton > button {{
            width: 220px;
            height: 65px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 15px;
            background-color: #add8e6;  /* light blue */
            color: black;
            border: none;
            box-shadow: 0 0 20px rgba(173, 216, 230, 0.9); /* foggy glow */
            transition: all 0.3s ease-in-out;
        }}
        div.stButton > button:hover {{
            background-color: #5dade2; /* deeper blue */
            box-shadow: none; /* fog removed */
            color: white;
        }}

        /* Counter styling with glow */
        .counter-text {{
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            color: #00bfff; /* deep sky blue */
            text-shadow: 0 0 15px rgba(0, 191, 255, 0.8);
            transition: all 0.3s ease-in-out;
        }}

        /* Responsive design */
        @media (max-width: 768px) {{
            div.stButton > button {{
                width: 150px;
                height: 50px;
                font-size: 16px;
            }}
            .counter-text {{
                font-size: 40px;
            }}
        }}

        @media (max-width: 480px) {{
            div.stButton > button {{
                width: 120px;
                height: 45px;
                font-size: 14px;
            }}
            .counter-text {{
                font-size: 32px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add OM logo (place your om.jpg/gif in the same folder)
add_bg_from_local(r"om.gif")

# Title
st.markdown("<h1 style='text-align:center; color:#0d1b2a;'>🕉️ Mantra Counter</h1>", unsafe_allow_html=True)

# Session state for counter
if "count" not in st.session_state:
    st.session_state.count = 0

# Centered buttons layout
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("🔼 Chant"):
        st.session_state.count += 1
    if st.button("🔄 Reset"):
        st.session_state.count = 0

# Display counter with glow
st.markdown(
    f"<h2 class='counter-text'>Count: {st.session_state.count}</h2>",
    unsafe_allow_html=True
)

# Motivational message
st.markdown(
    "<p style='text-align:center; color:purple; font-size:18px;'>Keep chanting... Stay blessed 🙏</p>",
    unsafe_allow_html=True
)

