from services.llm_engine import generate_response

query = "Photosynthesis in plants"
print("Summary:", generate_response(query, "summary"))
print("Analogy:", generate_response(query, "analogy"))
