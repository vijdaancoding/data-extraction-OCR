import unstructured
from unstructured.partition.pdf import partition_pdf

#path = r"C:/Ali Vijdaan/OCR/data-extraction-OCR/sample data/"
#file_name = r"Corporate Comprehensive EDI.pdf"
#output_dir = "Image Extractions"

def ocr_extraction(file_name, output_dir): 
    raw_elements = partition_pdf(
        filename=file_name,
        strategy='hi_res',
        infer_table_structure=True, 
        extract_images_in_pdf=True, 
        extract_image_block_output_dir=output_dir 
    )

    return raw_elements

