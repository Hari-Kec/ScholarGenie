from services.pdf_parser import parse_pdf

def test_pdf_parsing():
    with open("data/input_pdfs/sample.pdf", "rb") as f:
        text = parse_pdf(f.read())
        assert len(text) > 0
