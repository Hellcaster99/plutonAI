import requests as req
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader

# ----------------- Without RAG -----------------------------

def fetchData(url: str):
    res = req.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    return soup.get_text()

#------------------- RAG ----------------------------

# def fetchData(url: str):
#     loader = WebBaseLoader(web_paths=(url,), requests_kwargs={'verify':False})
#     return loader.load()
