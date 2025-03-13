import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker", page_icon="🌘", layout="centered")
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: #007BFF; color: white; font-size: 18px;}  /* Changed color to blue */
    .stButton button:hover { background-color: #FF5733; color: white;}  /* Changed hover color to red */
</style>
""", unsafe_allow_html=True)

st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level.🔎")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain both upper and lower case characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit.")

    if re.search(r"[!@#$%^&*()_+]", password):  # Fixed regex for special characters
        score += 1
    else:
        feedback.append("Include at least one special character.")

    if score == 4:
        st.success("☑️**Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️**Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("**Weak password** - Follow the suggestions below to strengthen it.")

    if feedback:
        with st.expander("**Improve your password**🔎"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong.🔒")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")
