# insureai/qa_pipeline.py
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from setup_vector_db import setup_vector_db

# Load vector database
db = setup_vector_db()

# Initialize open-source LLM
llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature": 0})

# Create RetrievalQA pipeline
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

def query_insureai(question):
    return qa_chain.run(question)
