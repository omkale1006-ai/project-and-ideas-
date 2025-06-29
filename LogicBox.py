# Main menu system
while True:
    print("\n1. Even or Odd")
    print("2. Age Checker")
    print("3. Leap Year")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        number=int(input("Enter your number:"))
        if number % 2==0:
            print(F"Ther {number} is even.")
        else:
            print(f"The {number} is odd.")
    elif ch == "2":
        
        age = int(input("Enter your age: "))
        if age >= 18:
            print("Eligible for voting!")
        else:
            print("Not eligible yet.")

    elif ch == "3":
        year = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")

    elif ch == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice")
