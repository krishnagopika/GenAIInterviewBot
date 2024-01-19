from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from model import llm

output_parser = StrOutputParser()

template = """Proide a question in the {topic}"""

question_prompt = PromptTemplate(template=template, input_variables=["topic"])

question_chain = LLMChain(prompt=question_prompt, llm=llm)


