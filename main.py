print("================================")
print("      AI STUDY ASSISTANT")
print("================================")

print("\n1. Add Subject")
print("2. Study Plan")
print("3. Study Tips")
print("4. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    subject = input("Enter subject name: ")
    print("Subject added:", subject)

elif choice == "2":
    subject = input("Which subject do you want to study? ")
    hours = input("How many hours can you study? ")
    print("\nStudy Plan")
    print("Subject:", subject)
    print("Study Time:", hours, "hours")

elif choice == "3":
    print("\nStudy Tips:")
    print("- Study for 45 minutes")
    print("- Take a 10 minute break")
    print("- Practice previous questions")
    print("- Revise before sleeping")

elif choice == "4":
    print("Thank you for using AI Study Assistant!")

else:
    print("Invalid choice!")
