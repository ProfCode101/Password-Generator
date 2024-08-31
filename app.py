import streamlit as st
import random


def capf():
    return chr(random.randint(65, 90))

def smolf():
    return chr(random.randint(97, 122))

def numberf():
    return chr(random.randint(48, 57))

def signf():
    x = random.randint(1, 4)
    if x == 1:
        return chr(random.randint(33, 47))
    elif x == 2:
        return chr(random.randint(58, 64))
    elif x == 3:
        return chr(random.randint(91, 96))
    else:
        return chr(random.randint(123, 126))


def generate_password(length, include_cap, include_smol, include_sign, include_number):
    if not (include_cap or include_smol or include_sign or include_number):
        st.error("Go and check you washroom for your brain 🧠 ")
        return ""

    preference = []
    if include_cap:
        preference.append(capf)
    if include_smol:
        preference.append(smolf)
    if include_sign:
        preference.append(signf)
    if include_number:
        preference.append(numberf)

    password = ''.join(random.choice(preference)() for _ in range(length))
    return password


def main():

    st.set_page_config(page_title="Password Generator", page_icon="🔐")

    st.markdown(
        """
        <style>
        /* Custom style for the button */
        .stButton>button {
            color: white;  /* Text color */
            background-color:#f70a0a ;  /* Background color */
            border: none;  /* Remove border */
            padding: 10px 24px;  /* Padding for size */
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;  /* Rounded corners */
            transition-duration: 0.4s;  /* Transition effect */
        }
        .stButton>button:hover {
            background-color: #85f70c;  /* Color on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.title("🔐 Password Generator ")
    st.markdown("### Create a strong and secure password ⚔️.")


    st.markdown("#### Select Your Preferences:")
    col1, col2 = st.columns(2)

    with col1:
        length = st.number_input("🔢 Password Length", min_value=1, max_value=100, value=8, step=1)

    with col2:
        include_cap = st.checkbox("🔠 Include Capital Letters", value=True)
        include_smol = st.checkbox("🔡 Include Small Letters", value=True)
        include_sign = st.checkbox("🔣 Include Special Characters", value=True)
        include_number = st.checkbox("🔢 Include Numbers", value=True)


    if st.button("Generate Password 🎉"):
        password = generate_password(length, include_cap, include_smol, include_sign, include_number)
        if password:
            st.markdown("### 🔑 Your Generated Password:")
            st.text_input("Generated Password", value=password, label_visibility='collapsed')

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("**Remember to keep your passwords safe and secure! 🔒**")


if __name__ == "__main__":
    main()

