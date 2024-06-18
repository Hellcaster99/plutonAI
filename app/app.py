import sys
import os
import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.soup import fetchData
from lib.pdf import readFile
from lib.rag import RAG
# from lib.pluton import plutonSummarize, askPluton
from lib.pluton import Pluton

st.set_page_config(page_title="PlutonAI")
st.title('Pluton')

option = st.radio("Choose input type:", ("URL", "File"))

data = None
if option == "URL":
    url = st.text_input("Enter the URL:")
    if url:
        data = fetchData(url)
else:
    file = st.file_uploader("Upload a file:", type=["pdf"])
    if file:
        data = readFile(file)
        
if 'history' not in st.session_state:
    st.session_state.history = []

# if data and not retriever: # RAG
#     with st.spinner('Running RAG Pipeline'):
#         retriever = RAG(data)

mode = None
if data:
    mode = st.radio("Choose mode:", ("Summarize", "Q&A Chatbot"))
    btn = st.button('Select')

if mode == "Summarize":
    if btn:
        st.subheader("Summarize with Pluton")
        with st.chat_message('AI'):
            
            # Without RAG
            # Single model
            st.write_stream(Pluton(context=data, query='summarize the key points in maximum 500 words', history=st.session_state.history))
            # Multi model
            # st.write_stream(plutonSummarize(context=data, query='summarize the key points in maximum 500 words'))

            # RAG
            # Multi
            # st.write_stream(plutonSummarize(retriever=retriever, n=400))
            # Single
            # st.write_stream(Pluton(retriever=retriever, query='summarize the key points in maximum 500 words'))

            
elif mode == "Q&A Chatbot":
    st.subheader("Ask Pluton")
    
    # Print chat history
    # for message in st.session_state.history:
    #     if message is None:
    #         break
    #     if isinstance(message, HumanMessage):
    #         st.chat_message('Human').markdown(message.content)
    #     elif isinstance(message, AIMessage):
    #         st.chat_message('AI').markdown(message.content)
    
    user_query = st.chat_input("Ask anything from the article")
    
    if (user_query is not None) and (user_query != ""):
        
        st.chat_message('Human').markdown(user_query)
        # st.session_state.history.append(HumanMessage(user_query))
        
        with st.chat_message('AI'):
            
            # Without RAG
            # Single
            answer = st.write_stream(Pluton(context=data, query=user_query, history=st.session_state.history))
            # Multi
            # answer = st.write_stream(askPluton(context=data, query=user_query, history=st.session_state.history))
            
            # RAG
            # Multi
            # answer = st.write_stream(askPluton(retriever=retriever, query=user_query, history=st.session_state.history))
            # Single
            # answer = st.write_stream(Pluton(retriever=retriever, query=user_query)) 
        # st.session_state.history.append(AIMessage(answer))