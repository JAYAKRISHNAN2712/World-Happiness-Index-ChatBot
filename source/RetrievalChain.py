from RAG_initializers import RAGInits
from VectorDB import VectorDB
from langchain.chains import ConversationalRetrievalChain
from langchain_core.prompts import PromptTemplate

# "ConversationalRetrievalChaining" class for "Question-Answering" along with "Memory".
class ConversationalRetrievalChaining:
    """
    ConversationalRetrievalChaining class for "Question-Answering" along with "Memory".
    
    """
    #static-variables
    chat_history = []
    llm, custom_template = RAGInits().llm, RAGInits().custom_template   # invoking "Meta-llama3-8B-Instruct" and custom template
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=VectorDB().load_collection(), 
        condense_question_prompt = PromptTemplate.from_template(custom_template),
        return_source_documents=True)

    def __init__(self,query):
        self.query = query   # Query from user

    def chain(self) -> str:
        result = ConversationalRetrievalChaining.qa({"question":self.query,"chat_history":ConversationalRetrievalChaining.chat_history})
        ConversationalRetrievalChaining.chat_history = [(self.query, result["answer"])]

        return result['answer']
    