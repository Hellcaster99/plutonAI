import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
# from langchain.indexes import VectorstoreIndexCreator
from langchain_community.vectorstores import FAISS

# from dotenv import load_dotenv

# load_dotenv()

# os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.environ['GOOGLE_API_KEY'])
embeddings = OllamaEmbeddings(model='llama3')
# embeddings = AutoEmbeddings.from_pretrained("huggingface/transformers")
# embeddings = HuggingFaceEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    add_start_index=True
)

def RAG(doc):
    chunks = text_splitter.split_documents(doc)
    print("n_documents",len(chunks))
    
    vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
    # db = VectorstoreIndexCreator(embedding=embeddings)
    # vectorstore = db.from_documents(chunks)
    
    # retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":3})
    retriever = vectorstore.as_retriever()
    
    return retriever