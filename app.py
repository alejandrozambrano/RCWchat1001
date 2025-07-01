import streamlit as st
from langchain_core.message import AIMessage, HumanMessage
from lanchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core_prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="RCW Chat Bot" , page_icon="book",layout="wide")
st.title("Streaming Chatbot")

def retrive_reponse(user_input, chat_history):
    template= '''

    Vuos étes un assistant

'''

pront = ChatPromptTemplate.from_template(template)
llm = ChatPromptTemplate(model="gpt-40", max_tokens=2500)
chain = pront | llm | strOutputParser()
return chain.stream(
    "chat_history":chat_history,
    "user_queestion":user_input
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = 
    AIMessage(content = "Bonjour je suis Alejandra, comment je peux vous aider")

for message in st,session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message.HumanMessage):
        with st.chat_message("human"):
            st.write(messa.content)



# L'utilisateur tape une nouvelle question
user_query = st.chat_input("How can i help you")
if user_query is not None and user_query!="";
    st.session_state.chat_history.append(HumanMessage(cobntent=user_query))
    with st.chat_message("Human"):
        


