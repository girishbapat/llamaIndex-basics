from llama_index.core import SimpleDirectoryReader
from llama_index.core.indices.vector_store.base import VectorStoreIndex
import os
from dotenv import load_dotenv
import logging
import sys

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
#logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

load_dotenv()

def main(url: str)->None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the artical saying please summarize it?")
    print(response)


if __name__ == '__main__':
    main(url=r"/Users/girishb/Documents/genai/data")