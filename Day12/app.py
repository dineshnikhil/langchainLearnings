import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LLAMA_CLOUD_API_KEY"] = os.getenv("LLAMA_CLOUD_API_KEY")


document = LlamaParse(result_type="markdown").load_data("../Day6/books/creditStatementOfMay.pdf")

print(document)