import pytesseract
from PIL import Image
import tempfile

async def extract_text_from_image(uploaded_file):
    contents = await uploaded_file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(contents)
        img = Image.open(tmp.name)
        text = pytesseract.image_to_string(img)
        return text