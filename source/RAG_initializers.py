from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint


class RAGInits:
    """
    invoking llm and custom template.
    
    """
    def __init__(self):
        self.llm = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct",  max_length=512,huggingfacehub_api_token="YOUR_API_TOKEN")

        self.custom_template = """ Given the following conversation and a follow up question,rephrase the follow up question to be a standalone    question.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:
"""
        
        
        