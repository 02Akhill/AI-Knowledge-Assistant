# Import LangChain text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Split extracted text into chunks
def create_chunks(text: str) -> list[str]:

    # Create splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    # Split text
    chunks = splitter.split_text(text)

    return chunks