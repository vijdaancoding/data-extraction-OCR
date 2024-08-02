# **Data Extraction via OCR and LLM**

The repo is an attempt to create an automated pipleine for extracting infromation from different documents and converting them into JSON 

## **1. Downloading UNSTRUCTURED.IO Dependancies** 

Follow [UNSTRUCTURED.IO's](https://docs.unstructured.io/open-source/installation/full-installation) own installation guide to download all dependancies

## Quick Summary of Installation Guide 

## **Windows**

### **1. libmagic-dev**

Use WSL to enter the following commands 
``` 
sudo apt update 
sudo apt install libmagic-dev
```

### **2. Poppler**

Check out the [pdf2image docs](https://pdf2image.readthedocs.io/en/latest/installation.html) on how to install Poppler on various devices 

### **3. libreoffice**

Check out the official page of [libreoffice](https://www.libreoffice.org/download/download-libreoffice/) for download guides. 

Once the `.msi` or `.exe` file is downloaded follow the on-screen instructions

### **4. Tesseract**

The latest installer for Tesseract on windows can be found [here](https://github.com/UB-Mannheim/tesseract/wiki)

Make sure to add the `C:\Program Files\Tesseract-OCR` to your Path.
