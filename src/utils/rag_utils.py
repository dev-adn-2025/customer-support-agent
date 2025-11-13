from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.tools.retriever import create_retriever_tool
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("src/data/data.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100,
    chunk_overlap=50
)
docs_splits = text_splitter.split_documents(documents)

vector_store = Chroma.from_documents(
    documents=docs_splits
    , embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    , persist_directory="./chroma_db")

retriever = vector_store.as_retriever(search_kwargs={"k":3})

retriever_tool = create_retriever_tool(
    retriever,
    "retrieve_products_and_services_information",
    "Search and return information about products or services"
)


def get_retriever_tool():
    return retriever_tool