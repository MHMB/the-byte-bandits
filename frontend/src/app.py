import streamlit as st
import requests

st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered", initial_sidebar_state="auto")
st.markdown("""
<style>
body, html {
    direction: RTL;
    //unicode-bidi: bidi-override;
    text-align: right;
}
p, div, input, label, h1, h2, h3, h4, h5, h6 {
    direction: RTL;
    //unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)


# Centered header and title
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0;'>💬 InvestiChat</h1>
    <h4 style='text-align: center; margin-top: 0; color: #666;'>مشاور هوشمند سرمایه‌گذاری</h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat thread
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Inline input and button at the bottom
def send_message():
    user_input = st.session_state.user_input.strip()
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        try:
            response = requests.post(
                "http://localhost:8000/chat",
                json={"message": user_input},
                timeout=10
            )
            if response.ok:
                bot_reply = response.json().get("reply", "پاسخی دریافت نشد")
            else:
                bot_reply = "خطا:‌دسترسی به سرور امکان‌پذیر نیست."
        except Exception as e:
            bot_reply = f"Error: {e}"
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.session_state.user_input = ""

# Custom CSS for input/button alignment
st.markdown(
    """
    <style>
    div.stChatInputContainer {display: none;}
    .chat-input-row {display: flex; align-items: center; gap: 0.5rem; position: fixed; bottom: 2rem; left: 0; width: 100%; background: #fff; padding: 1rem 2rem 1rem 2rem; z-index: 100;}
    .chat-input-row input {flex: 1;}
    div.stChatInputContainer {display: none;}
    .chat-input-row {
        display: flex; align-items: center; gap: 0.5rem;
        position: fixed; bottom: 2rem; left: 0; width: 100%;
        background: #fff; padding: 1rem 2rem 1rem 2rem; z-index: 100;
    }
    .chat-input-row input {
        flex: 1;
        direction: rtl; /* Enable RTL support */
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom input and button
with st.container():
    st.markdown('<div class="chat-input-row">', unsafe_allow_html=True)
    user_input = st.text_input(
        "Type your message...",
        key="user_input",
        label_visibility="collapsed",
        placeholder="لطفا پیام خود را وارد کنید...",
        on_change=send_message,
    )
    st.markdown(
        """
        <form action="#" method="post" style="margin:0;display:inline;">
            <button type="submit" style="height:2.5rem; padding:0 1.5rem; background:#4F8BF9; color:white; border:none; border-radius:4px; font-size:1rem; cursor:pointer;" onclick="window.dispatchEvent(new Event('send_message'));">ارسال</button>
        </form>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Light theme is default in Streamlit; no extra config needed.