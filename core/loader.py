from langchain_community.document_loaders import PyPDFLoader
# PyPDF is used to read and make page wise document objects
# This is langchain's Built-in loader
import tempfile

def load_pdfs(uploaded_files): # pdf uploaded by users
    
    all_documents = [] # To collect documents of all the PDFs
    
    for file in uploaded_files: # Each of the uploaded PDF will be processed individually
        # 🔥 Step 1: Save file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.read())
            temp_file_path = temp_file.name

        # 🔥 Step 2: Load using file path
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load() # Actual loading
                                # one page -> one document

        # Add metadata
        for i, doc in enumerate(documents): # iterate every page of each document
            doc.metadata["page"] = i+1 # page number is stored
            doc.metadata["source"] = file.name # which pdf it actually belongs 

        all_documents.extend(documents) # now combine all the documents and also avoid (list of lists) i.e. flattened structure

    return all_documents # output has a single list containing all pages, all pdfs along with metadata