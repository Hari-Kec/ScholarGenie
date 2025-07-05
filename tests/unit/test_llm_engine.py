from services.llm_engine import generate_response

def test_response():
    res = generate_response("Gravity", "summary")
    assert isinstance(res, str)
    assert len(res) > 10
