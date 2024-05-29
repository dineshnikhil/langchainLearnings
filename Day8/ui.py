import PyPDF2
from langchain_core.messages import AIMessage, HumanMessage
from llm import load_pdf, get_response_from_llm

def initialize_chat_history(session_state):
    if "chat_history" not in session_state:
        session_state.chat_history = [
            AIMessage(content="Hello!"),
        ]

def display_chat_history(session_state, st):
    for message in session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)

def handle_user_query(session_state, st, user_query, pdf_text):
    if user_query is not None and user_query.strip() != "":
        session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("Human"):
            st.markdown(user_query)
        
        # Simulate AI response (In practice, you would call your AI model here)
        response = get_response_from_llm(pdf_text, user_query)
        
        with st.chat_message("AI"):
            st.markdown(response)
            
        session_state.chat_history.append(AIMessage(content=response))

def process_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text
