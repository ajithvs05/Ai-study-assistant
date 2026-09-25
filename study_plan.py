print("===== STUDY PLANNER =====")

subjects = []

while True:
    subject = input("\nEnter a subject (or type 'done'): ")

    if subject.lower() == "done":
        break

    hours = input("How many hours will you study? ")

    subjects.append((subject, hours))

print("\n===== YOUR STUDY PLAN =====")

for subject, hours in subjects:
    print(subject, "-", hours, "hours")

print("\nGood luck with your studies! 📚")
