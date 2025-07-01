from langchain_ollama import OllamaLLM
from langchain_core.promts import ChatPrompTemplate
import time

template = '''
Tu es un professeur de scince au lycee. Sois clair, concis et pedagogue


Question : {question}

Reponse :

'''

model = OllamaLLM(model="mistral")
prompt = ChatPrompTemplate.from_template(template)
chain = prompt | model

def handleConverdation():
    contex=""
    print("BOnjour je suis Alexandre, comment je peux aider? Si vous n'avez pas de question ecrivez 'quit'")
    while True:
        user_input = input("Vous :")
        if user_input.lower() == 'quit':
            break
        result = chain.invoke("context":context , "question":user_input)
        for char in resulte:
            print(char, end="" , flush=True)
            time.sleep(0.02) 
        print()
        context += f

