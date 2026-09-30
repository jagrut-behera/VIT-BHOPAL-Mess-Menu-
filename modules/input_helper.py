def choose(options, title):
    while True:
        print("\n" + title)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Please enter a valid choice.")

def pause():
    input("\nPress Enter to continue...")
