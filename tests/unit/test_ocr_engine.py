from services.ocr_engine import perform_ocr

def test_ocr_image():
    with open("sample_handwriting.png", "rb") as f:
        text = perform_ocr(f.read())
        assert len(text) > 0
