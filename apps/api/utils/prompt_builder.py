def build_prompt(query: str, mode: str):
    if mode == "eli5":
        return f"Explain like I'm 5: {query}"
    elif mode == "analogy":
        return f"Give me an analogy for: {query}"
    else:
        return f"Explain this: {query}"
