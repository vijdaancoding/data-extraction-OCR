import streamlit as st
import tempfile
import os 
import base64

from extraction_ocr import ocr_extraction, filter_text_elements

#Create a temporary directory to store uplaoded documents
def create_temp_dir(uploaded_file): 
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, uploaded_file.name)

    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(uploaded_file.read())

    output_dir = os.path.join(temp_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    return temp_file_path, output_dir

# Main function to perform OCR and text extraction
def run_ocr(uploaded_file): 
    text_elements = []
    raw_elements = []

    if uploaded_file is not None: 
        temp_file_path, output_dir = create_temp_dir(uploaded_file)

        if uploaded_file.type == 'application/pdf': 
            raw_elements = ocr_extraction(file_name=temp_file_path, output_dir=output_dir)
            text_elements = filter_text_elements(raw_elements)

            return text_elements, temp_file_path
        else: 
            print("No PDF file found")
    else: 
        print("No file found")

def get_base64_of_file(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

def show_uploaded_docs(uploaded_file, temp_file_path): 

    if uploaded_file is not None: 
        st.subheader("Doc Viewer")

        if uploaded_file.type == 'application/pdf': 
            #Display pdf in iframe
            pdf_base64 = get_base64_of_file(temp_file_path)
            pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" height="500" width="100%" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.write("No file found")

def show_extracted_text(elements):

    # Add custom CSS to style the container
    st.markdown(
        """
        <style>
        .scrollable-container {
            height: 500px;
            width: 100%;
            overflow-y: scroll;
            border: 1px solid #ccc;
            padding: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a container with the custom class
    container_html = '<div class="scrollable-container">'
    for element in elements:
        container_html += f"<p>{element}</p>"
    container_html += '</div>'

    # Render the container with the elements inside
    st.markdown(container_html, unsafe_allow_html=True)
    

def main(): 
    st.set_page_config(page_title="Doc Extractor", layout="wide")
    
    with st.container():    
        st.title("Document Data Extractor")
        st.write("The goal is to create an ETL pipeline that can load documents and preprocess them to make them RAG Ready!")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

    if uploaded_file is not None: 
        text_elements, temp_file_path = run_ocr(uploaded_file)

        with st.container():
            left_column, right_column = st.columns(2)

            with left_column: 
                with st.expander("Show original document"): 
                    show_uploaded_docs(uploaded_file, temp_file_path)

            with right_column: 
                with st.expander("Show Extracted Text"):
                    show_extracted_text(text_elements)
                    




if __name__ == "__main__": 
    main()