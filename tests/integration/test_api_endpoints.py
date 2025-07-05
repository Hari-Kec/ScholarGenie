from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_parse_pdf_endpoint():
    with open("data/input_pdfs/sample.pdf", "rb") as f:
        response = client.post("/parse/", files={"file": f})
        assert response.status_code == 200
