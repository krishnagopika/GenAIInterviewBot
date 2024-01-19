
from dotenv import load_dotenv
from langchain.llms.huggingface_hub import HuggingFaceHub


load_dotenv()

model = "google/flan-t5-xxl"
llm = HuggingFaceHub(
    repo_id = model, model_kwargs={"temperature": 0.5, "max_length": 200}
)
