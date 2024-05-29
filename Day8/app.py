import streamlit as st
from ui import initialize_chat_history, display_chat_history, handle_user_query, process_pdf

st.set_page_config(page_title="Chat with WebSites", page_icon=":speech_balloon")
st.title("Chat with WebSites")

# Sidebar for PDF upload and connect button
with st.sidebar:
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if st.button("Connect"):
        if uploaded_file is not None:
            pdf_text = process_pdf(uploaded_file)
            st.session_state.pdf_text = pdf_text
            st.sidebar.write("PDF Uploaded and Processed")
        else:
            st.sidebar.write("Please upload a PDF file")

# Initialize chat history
initialize_chat_history(st.session_state)

# Display chat history
display_chat_history(st.session_state, st)

# User input
user_query = st.chat_input("Type a message...")

# Handle user query
if 'pdf_text' in st.session_state:
    handle_user_query(st.session_state, st, user_query, st.session_state.pdf_text)
else:
    st.write("Please upload a PDF file and click Connect.")
