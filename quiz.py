print("================================")
print("        🧠 STUDY QUIZ")
print("================================")

questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit",
                    "B. Computer Personal Unit",
                    "C. Central Program Utility",
                    "D. Control Processing User"],
        "answer": "A"
    },
    {
        "question": "Which language is used in this project?",
        "options": ["A. Java",
                    "B. Python",
                    "C. C++",
                    "D. HTML"],
        "answer": "B"
    },
    {
        "question": "What does AI stand for?",
        "options": ["A. Automated Internet",
                    "B. Artificial Intelligence",
                    "C. Advanced Information",
                    "D. Automatic Interface"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print("\n================================")
print("Quiz Finished!")
print("Your Score:", score, "/", len(questions))
print("================================")
