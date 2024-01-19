from speech_to_text import speech_to_text
from question_llm_chain import question_chain
from answer_llm_chain import answer_chain

question = question_chain.run("Python")
answer = speech_to_text('./audiofiles/Python-Project-Audio-to-Text/30_Questions_recording/Question 8.mp3')
print(question)
result = answer_chain.predict(question="What is inheritance in Java", answer=answer)
print(result)

