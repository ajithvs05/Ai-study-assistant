print("===== AI STUDY ASSISTANT =====")
print("Ask me a study question!")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ").lower()

    if question == "exit":
        print("AI: Good luck with your studies!")
        break

    elif "python" in question:
        print("AI: Python is a high-level programming language.")

    elif "os" in question or "operating system" in question:
        print("AI: An operating system manages computer hardware and software.")

    elif "microcontroller" in question:
        print("AI: A microcontroller is a small computer on a single integrated circuit.")

    elif "database" in question:
        print("AI: A database is used to store and manage data.")

    elif "ai" in question or "artificial intelligence" in question:
        print("AI: Artificial Intelligence allows computers to perform tasks that normally require human intelligence.")

    else:
        print("AI: I don't know this yet. Try asking about Python, OS, AI, databases or microcontrollers.")
