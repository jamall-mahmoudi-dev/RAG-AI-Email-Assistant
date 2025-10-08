import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Load API key
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load vector DB
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = Chroma(persist_directory="./data", embedding_function=embeddings)

# Load prompts
base_prompt = open("./prompts/base_prompt.txt").read()
tone_prompt = open("./prompts/tone_prompt.txt").read()
business_rules_prompt = open("./prompts/business_rules_prompt.txt").read()

prompt_template = PromptTemplate(
    input_variables=["context", "email_text"],
    template=base_prompt + "\n" + tone_prompt + "\n" + business_rules_prompt
)

chat_model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)

def generate_response(email_text):
    # Retrieve context from vector DB
    docs = vectorstore.similarity_search(email_text, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    # Build prompt
    prompt = prompt_template.format(context=context, email_text=email_text)
    
    # Generate response
    response = chat_model.predict(prompt)
    return response
