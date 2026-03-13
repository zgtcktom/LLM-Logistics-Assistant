#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nbimport
import os, sys, json


# In[2]:


get_ipython().run_line_magic('pip', 'install -q chromadb sentence-transformers')


# In[3]:


RAG_DB_PATH = "./rag/db"
RAG_DATA_PATH = "./rag/data"


# In[4]:


import chromadb
from chromadb.utils import embedding_functions


# In[5]:


client = chromadb.PersistentClient(path=RAG_DB_PATH)


# In[ ]:


default_emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="milp_examples",
    embedding_function=default_emb_fn,
)

if __name__ == "__main__":
    # documents = []
    # metadatas = []
    # ids = []

    for filename in os.listdir(RAG_DATA_PATH):
        if not filename.endswith(".json"):
            continue

        with open(os.path.join(RAG_DATA_PATH, filename), "r") as f:
            data = json.load(f)
            # documents.append(data["document"])
            # metadatas.append(data["metadata"])
            # ids.append(filename)
            collection.add(documents=[data["document"]], metadatas=[data["metadata"]], ids=[filename])

    # collection.add(documents=documents, metadatas=metadatas, ids=ids)


# In[ ]:


# collection.query(
#     query_texts=[
#         """
# distance matrix: [[0, 12, 8, 13, 10, 1, 18, 0], [0, 16, 9, 6, 14, 15, 11, 0], [0, 2, 4, 3, 17, 7, 5, 0]]
  
# all demands are 1, vehicle capacity is 3
# find the routes and total distance
# """
#     ],
#     n_results=1,
# )


# In[ ]:




