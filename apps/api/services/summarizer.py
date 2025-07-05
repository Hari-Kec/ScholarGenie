from services import llm_engine
from utils import prompt_builder

def get_explanation(query: str, mode: str = "normal"):
    prompt = prompt_builder.build_prompt(query, mode)
    return llm_engine.infer(prompt)