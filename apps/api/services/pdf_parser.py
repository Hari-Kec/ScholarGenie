import fitz  # PyMuPDF
import tempfile

async def extract_text_from_pdf(uploaded_file):
    contents = await uploaded_file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(contents)
        doc = fitz.open(tmp.name)
        text = "\n".join([page.get_text() for page in doc])
        return text