from langchain_text_splitters import RecursiveCharacterTextSplitter
# Smart text splitting tool from langchain

def split_documents(documents): # Outputs from LOADER to convert into smaller chunks

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500, # maximum size of each chunk
        chunk_overlap = 100 # overlap of 100 words -> basically 100 words of previous chunk will also be present
    )

    chunks = splitter.split_documents(documents) # Breaks the document pages in chunks with metadata(preserved)

    return chunks # small infomation rich chunks