from langchain_ollama import OllamaLLM

from langchain_core.prompts import ChatPromptTemplate


template = """
Answer the following question:

Here is the conversation history: {context}

question: {question}

answer:

"""

def start(question):
    convo


def convo(question):
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="gemma2:9b")
    chain = prompt | model
    return chain.invoke({"question": question, "context":"You're an EXPERT translator and tranlste everthing to ENGLISH. Your task is to give the as it is English translation of given sentence"
})

question  = "mere ko hillana hai"

result = convo(question)
print(result)