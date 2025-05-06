#from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core.indices.vector_store.base import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv
load_dotenv()

def main(url:str)-> None:
    document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.query("What is Agentic AI?")
    print(response)

if __name__ == '__main__':
    main(url='https://medium.com/data-science-collective/agentic-ai-comparing-new-open-source-frameworks-21ec676732df')