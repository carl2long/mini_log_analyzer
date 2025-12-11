Red = "\033[91m"
Green = "\033[92m"
Yellow = "\033[93m"
Blue = "\033[94m"
Reset = "\033[0m"

def drill1():
    age_text = input("What is your age? ")
    try:
        age = int(age_text)
    except ValueError:
        print(Red + "Please enter a valid number" + Reset)
        return

    if age < 0:
        print(Yellow + "Age can't be negative" + Reset)
    elif age < 18:
        print(Green + "Minor" + Reset)
    elif age < 65:
        print(Green + "Adult" + Reset)
    elif age < 120:
        print(Green + "Senior" + Reset)
    else:
        print(Yellow + "That age doesn't seem realistic." + Reset)

def drill2():
    n_text = input("Enter a number: ")
    try:
        n = int(n_text)
    except ValueError:
        print(Red + "Please enter a valid number." + Reset)
        return

    total = 0
    for i in range(1, n + 1):
        print(i)
        total += i
    print(Green + f"Sum of 1 to {n} is {total}" + Reset)

def drill3():
    numbers = []
    for i in range(5):
        while True:
            value_text = input(f"Enter a number {i + 1}: ")
            try:
                value = int(value_text)
                numbers.append(value)
                break
            except ValueError:
                print(Red + "Please enter a valid number." + Reset)

    print(numbers)
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))

def drill4():
    pass
def drill5():
    pass
def main():
    while True:
        print(Blue + "\n=== Python Warmup Drills ===")
        print("1) Age classifier")
        print("2) Sum 1..n")
        print("3) List practice")
        print("4) Dictionary practice")
        print("5) Function practice")
        print("6) Exit")

        choice = input("Choose a drill (1-6): ").strip()

        if choice == "1":
            drill1()
        elif choice == "2":
            drill2()
        elif choice == "3":
            drill3()
        elif choice == "4":
            drill4()
        elif choice == "5":
            drill5()
        elif choice == "6":
            print(Green + "Goodbye!" + Reset)
            break
        else:
            print(Red + "Invalid choice, try again." + Reset)

if __name__== "__main__":
    main()
