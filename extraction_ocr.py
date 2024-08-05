import unstructured
from unstructured.partition.pdf import partition_pdf

#path = r"C:/Ali Vijdaan/OCR/data-extraction-OCR/sample data/"
#file_name = r"Corporate Comprehensive EDI.pdf"
#output_dir = "Image Extractions"

#Function for OCR Extraction from PDFs
def ocr_extraction(file_name, output_dir): 
    raw_elements = partition_pdf(
        filename=file_name,
        strategy='hi_res',
        infer_table_structure=True, 
        extract_images_in_pdf=True, 
        extract_image_block_output_dir=output_dir 
    )

    return raw_elements

#Filtering Text Elements 
text_element_items = [unstructured.documents.elements.Text, 
                      unstructured.documents.elements.NarrativeText,
                      unstructured.documents.elements.ListItem, 
                      unstructured.documents.elements.Header, 
                      unstructured.documents.elements.Footer, 
                      unstructured.documents.elements.Title, 
                      unstructured.documents.elements.CompositeElement]

image_element_items = [unstructured.documents.elements.Image]

def filter_text_elements(raw_elements): 
    text_elements = []

    for ele in raw_elements:
        if type(ele) in text_element_items: 
            text_elements.append(ele)
        else: continue

    return text_elements
    
    

    