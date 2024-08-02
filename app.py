import streamlit as st
from PIL import Image
import tempfile
import os 
import io
import glob
import json
import base64

from extraction_ocr import ocr_extraction

# Set the page layout to wide
st.set_page_config(layout="wide")

def print_text(raw_elements):

    # Add custom CSS to style the container
    st.markdown(
        """
        <style>
        .scrollable-container {
            height: 500px;
            width: 450px;
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
    for element in raw_elements:
        container_html += f"<p>{element}</p>"
    container_html += '</div>'
    
    # Render the container with the elements inside
    st.markdown(container_html, unsafe_allow_html=True)

# Function to convert file to base64 for embedding
def get_base64_of_file(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode()

st.title("PDF and Doc Data Extractor")

uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])

if uploaded_file is not None:

    # Create a temporary directory to save uploaded files
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(uploaded_file.read())
        
        # Create an output directory within the temporary directory
        output_dir = os.path.join(temp_dir, "output")
        os.makedirs(output_dir, exist_ok=True)

        # Check if the file is a PDF
        if uploaded_file.type == "application/pdf":
            #Call OCR Function
            raw_elements = ocr_extraction(file_name=temp_file_path, output_dir=output_dir)

        # Create columns for side-by-side display
        col1, col2 = st.columns([8, 8])

        with col1:
            # Display the PDF with a scroller
            st.subheader("PDF Viewer")
            pdf_base64 = get_base64_of_file(temp_file_path)
            pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" height="500" width="450" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        with col2:
            # Display OCR text
            st.subheader("OCR Results")
            print_text(raw_elements)
    
        # Create a download button for each file in the output directory
        st.write("Download extracted files:")
        for file_path in glob.glob(os.path.join(output_dir, '*')):
            file_name = os.path.basename(file_path)
            with open(file_path, 'rb') as file:
                file_bytes = file.read()
                st.download_button(label=f"Download {file_name}", data=file_bytes, file_name=file_name)