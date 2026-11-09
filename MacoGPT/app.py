
import streamlit as st
from chatbot import get_ai_response

# =====================================
# MACOGPT APPLICATION
# =====================================

st.set_page_config(
    page_title="MacoGPT",
    page_icon="🤖",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00c8ff;
}
.subtitle {
    text-align: center;
    color: #aaaaaa;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🤖 MacoGPT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Personal AI Assistant</div>',
    unsafe_allow_html=True
)

st.divider()

# Sidebar
with st.sidebar:
    st.title("🤖 MacoGPT")
    st.write("Created by Emmanuel Nkemakolam")
    st.write("Also known as Maco-Tech")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by Groq AI")

# Conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if not st.session_state.messages:
    st.markdown("### Welcome to MacoGPT!")
    st.write("Ask me anything. I am ready to help you.")

# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Message MacoGPT...")

if user_input:
    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("MacoGPT is thinking..."):
            answer = get_ai_response(
                st.session_state.messages
            )

        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
