from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chains import LLMChain

from model import llm
# class Score(BaseModel):
#     score: str = Field(description="score in percentage")
    

# output_parser = JsonOutputParser(pydantic_object=Score)

answer_prompt = PromptTemplate(template = """Question: {question}, Answer: {answer} evaluate the answer for the given question, and return the score in a percentage ranging [0,100]
                                          """, input_variables=["question","answer"])


answer_chain = LLMChain(prompt=answer_prompt, llm=llm)
