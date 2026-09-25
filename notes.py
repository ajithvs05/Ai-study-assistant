print("===== STUDY NOTES =====")

notes = []

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Write your note: ")
        notes.append(note)
        print("Note saved!")

    elif choice == "2":
        print("\n===== YOUR NOTES =====")

        if len(notes) == 0:
            print("No notes available.")
        else:
            for i, note in enumerate(notes, 1):
                print(i, ".", note)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
