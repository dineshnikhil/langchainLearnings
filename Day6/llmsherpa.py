import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
import bs4
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


def simpleRAGResponse(user_query):
    # loader = PyPDFLoader('./books/napoleon-hill_think-and-grow-rich.pdf')
    # loader = PyMuPDFLoader('./books/creditStatementOfMay.pdf')
    loader = UnstructuredPDFLoader('./books/creditStatementOfMay.pdf', mode='elements')
    pages = loader.load_and_split()

    vectorstore = Chroma.from_documents(documents=pages, embedding=OpenAIEmbeddings())

    # Retrieve and generate using the relevant snippets of the blog.
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    prompt = hub.pull("rlm/rag-prompt")


    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    # creating the llm
    llm = ChatOpenAI()


    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    result = rag_chain.invoke(user_query)
    vectorstore.delete_collection()
    return result

st.set_page_config(page_title="Chat with WebSites", page_icon=":speech_ballon")
st.title("Chat with WebSites")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello!"),
    ]


for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)


user_query = st.chat_input("Type a message...")

if user_query is not None and user_query.strip() != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
        
    with st.chat_message("AI"):
        response = simpleRAGResponse(user_query=user_query)
        st.markdown(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))