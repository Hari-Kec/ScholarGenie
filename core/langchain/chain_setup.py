import kagglehub
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import transformers

GEMMA_PATH = kagglehub.model_download("google/gemma-3n/transformers/gemma-3n-e2b-it")

def load_summary_chain():
    tokenizer = transformers.AutoTokenizer.from_pretrained(GEMMA_PATH)
    model = transformers.AutoModelForCausalLM.from_pretrained(GEMMA_PATH)

    pipe = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        temperature=0.7,
        do_sample=True
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    with open("core/prompts/summary_prompt.txt") as f:
        prompt_template = f.read()

    prompt = PromptTemplate.from_template(prompt_template)
    return LLMChain(prompt=prompt, llm=llm)
