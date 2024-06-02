import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


openAI_llm = ChatOpenAI()
output_parser = StrOutputParser()


def translate_llm(input_lang, output_lang, query):
    template = "You are a helpful assistant that translate {input_lang} to {output_lang}"
    human_query = "{query}"
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_query)
    ])
    
    chain = chat_prompt | openAI_llm | output_parser
    
    response = chain.invoke({
        "input_lang": input_lang,
        "output_lang": output_lang,
        "query": query
    })
    
    return response