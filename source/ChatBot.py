import streamlit as st
from RetrievalChain import ConversationalRetrievalChaining  

def main():
    st.title('World Happiness Index - CHatBot')
    query = st.text_input('Enter your query:')
    
    if st.button('Submit'):
        if query:
            # Initialize your ConversationalRetrievalChaining instance
            retriever = ConversationalRetrievalChaining(query)
            answer = retriever.chain()
            
            # Display the answer
            st.write('Answer:', answer)
            
            # Display chat history
            st.write('Chat History:')
            for idx, (q, a) in enumerate(ConversationalRetrievalChaining.chat_history, start=1):
                st.write(f'{idx}. Query: {q}, Answer: {a}')
        else:
            st.warning('Please enter a query.')

if __name__ == '__main__':
    main()
