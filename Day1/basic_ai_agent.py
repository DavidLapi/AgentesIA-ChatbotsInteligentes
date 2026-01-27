from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
llm = OllamaLLM(model="mistral")

print("\nWelcome to your Agent IA! Ask me something...")

while True:
    question = input("Make your question (or write 'exit' to stop the machine): ")
    if question.lower() == "exit":
        print("Good bye, begginner!")
        break
    response = llm.invoke(question)
    print("\n Response for IA: ", response)