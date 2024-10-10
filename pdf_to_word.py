import pdfplumber # type: ignore
from docx import Document # type: ignore

# Function to convert PDF to Word
def pdf_to_word(pdf_path, word_path):
    # Create a Word document
    doc = Document()

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Loop through the pages
        for page in pdf.pages:
            # Extract text from each page
            text = page.extract_text()
            if text:
                # Add the text to the Word document
                doc.add_paragraph(text)

    # Save the Word document
    doc.save(word_path)
    print(f"PDF has been successfully converted to Word: {word_path}")

# Example usage
# Κώδικας Python για τη μετατροπή του example.pdf σε αρχείο Word
pdf_path = "main.pdf"  # Το όνομα του PDF αρχείου
word_path = "main.docx"  # Το όνομα του Word αρχείου

# Κλήση της συνάρτησης μετατροπής
pdf_to_word(pdf_path, word_path)