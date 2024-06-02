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

def get_bllt_pnts_frm_desc(job_description):
    template = """
you are exallent copywriter of resume writes the impactful bullet points based on the job description below are the points to be notes

Certainly! When describing your work experience on your resume, **focus on accomplishments and results** rather than just listing responsibilities. Here are some tips and examples to help you create impactful bullet points:

1. **Be Specific and Quantify:**
   - Instead of saying, "Responsible for handling customer requests," provide specific details: "Successfully managed 50-70 inbound customer requests per day, ranking in the top 5% of all support associates in 2017."
   - Quantify your achievements with numbers or percentages whenever possible. For instance:
     - "Managed day-to-day activities of 7 key corporate accounts while successfully completing 9 client projects, each with a budget above $500,000, leading to a $2.1 million increase in new business for the company."

2. **Start with Action Verbs:**
   - Begin each bullet point with an action verb to make your accomplishments stand out. Examples include:
     - "Achieved," "Implemented," "Led," "Developed," "Generated," "Reduced," etc.

3. **Tailor to the Job:**
   - Customize your bullet points for the specific job you're applying for. Highlight relevant skills and experiences that align with the position.
   - Avoid generic statements like "Managed day-to-day activities" and focus on what sets you apart.

Remember, hiring managers want to see how likely you are to excel in the job. Specific accomplishments and relevant details will make your work experience section stand out!
    """
    human_query = "Now based on the above points and the job description given. give me four imapact full bullet points with 30 to 35 words range each bullet point job description: {job_description}"
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_query)
    ])
    
    # print(chat_prompt)
    
    chain = chat_prompt | openAI_llm | output_parser
    
    response = chain.invoke({
        "job_description": job_description
    })
    
    return response