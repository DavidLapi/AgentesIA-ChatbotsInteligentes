# Agente de IA Básico ⬇️⬇️

# from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
# llm = OllamaLLM(model="mistral")

# print("\nWelcome to your Agent IA! Ask me something...")

# while True:
    # question = input("Make your question (or write 'exit' to stop the machine): ")
    # if question.lower() == "exit":
        # print("Good bye, begginner!")
        # break
    # response = llm.invoke(question)
    # print("\n Response for IA: ", response)

# ---------------------------------------------------------------------------------------

# Agente de IA Básico Con Memoria ⬇️⬇️⬇️

# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
# llm = OllamaLLM(model="mistral")

# Inicialize Memory
# chat_history = ChatMessageHistory() # Stores user-AI conversation history

# Define AI Chat Prompt
# prompt = PromptTemplate(
    # imput_variables=["chat_history", "question"],
    # template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
# )

# Function to run AI chat with memory
# def run_chain(question):
    # Retrieve chat history manually
    # chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])

    # RUN the AI response generation
    # response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    # Store new user input and AI response in memory
    # chat_history.add_user_message(question)
    # chat_history.add_ai_message(response)

    # return response

# Interactive CLI Chatbot
# print("\n📤 AI Chatbot with Memory")
# print("Type 'exit' to stop.")

# while True:
    # user_input = input("\n📋 You: ")
    # if user_input.lower() == "exit":
        # print("\n👋 Good Bye!!")
        # break

    # ai_response = run_chain(user_input)
    # print(f"\n📨 AI: {ai_response}")

# Agente de IA con Interfaz Web (Aquí es donde empezaría el código) ⬇️⬇️⬇️

import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model

# Inicialize Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory() # Stores user-AI conversation history 

# Define AI Chat Prompt
prompt = PromptTemplate(
    imput_variables=["chat_history", "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)

# Function to run AI chat with memory
def run_chain(question):
    # Retrieve chat history manually
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

    # RUN the AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    # Store new user input and AI response in memory
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

# Streamlit UI
st.title("🤖 AI Chatbot with Memory ")
st.write("Ask me anything!")

user_input = st.text_input("📋 Your Question:")
if user_input:
    response = run_chain(user_input)
    st.write(f"**You:** {user_input}")
    st.write(f"**Ai:** {response}")

# Show full chat history
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")