print("===================================")
print("       🤖 AI STUDY ASSISTANT")
print("===================================")

while True:
    print("\n1. Study Planner")
    print("2. Study Notes")
    print("3. AI Questions")
    print("4. Quiz Mode")
    print("5. Study Tips")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        subject = input("Enter subject: ")
        hours = input("Enter study hours: ")

        print("\n📚 Study Plan")
        print("Subject:", subject)
        print("Study Time:", hours, "hours")

    elif choice == "2":
        note = input("Enter your study note: ")

        print("\n📝 Note Saved:")
        print(note)

    elif choice == "3":
        question = input("Ask a question: ").lower()

        if "python" in question:
            print("AI: Python is a high-level programming language.")

        elif "os" in question:
            print("AI: An operating system manages computer hardware and software.")

        elif "ai" in question:
            print("AI: Artificial Intelligence enables computers to perform tasks that normally require human intelligence.")

        elif "microcontroller" in question:
            print("AI: A microcontroller is a small computer on a single integrated circuit.")

        else:
            print("AI: I don't have an answer for that yet.")

    elif choice == "4":
        questions = [
            ("What does CPU stand for?",
             ["A. Central Processing Unit",
              "B. Computer Personal Unit",
              "C. Central Program Utility",
              "D. Control Processing User"],
             "A"),

            ("Which language is used in this project?",
             ["A. Java",
              "B. Python",
              "C. C++",
              "D. HTML"],
             "B"),

            ("What does AI stand for?",
             ["A. Automated Internet",
              "B. Artificial Intelligence",
              "C. Advanced Information",
              "D. Automatic Interface"],
             "B")
        ]

        score = 0

        for question, options, answer in questions:
            print("\n" + question)

            for option in options:
                print(option)

            user_answer = input("Your answer: ").upper()

            if user_answer == answer:
                print("✅ Correct!")
                score += 1
            else:
                print("❌ Wrong!")

        print("\nYour Score:", score, "/", len(questions))

    elif choice == "5":
        print("\n💡 Study Tips")
        print("• Study for 45 minutes.")
        print("• Take a short break.")
        print("• Practice previous questions.")
        print("• Revise regularly.")

    elif choice == "6":
        print("\nThank you for using AI Study Assistant! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.")
