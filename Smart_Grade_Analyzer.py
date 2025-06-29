def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter your {subject} marks (out of 100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter marks between 0 and 100 only.")
        except ValueError:
            print("Invalid input! Please enter numeric marks.")

def show_menu():
    print("\n📘 What do you want to do?")
    print("1. Show total marks")
    print("2. Show percentage")
    print("3. Show grade")
    print("4. Show subject-wise marks")
    print("5. Exit program")

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'Fail'

# 🔰 Program Start
print("🎓 Welcome to Smart Grade Analyzer 🎓")

# 📝 Taking input
math = get_marks("Maths")
physics = get_marks("Physics")
marathi = get_marks("Marathi")
chemistry = get_marks("Chemistry")
pps = get_marks("PPS")

# 📊 Calculations
total = math + physics + marathi + chemistry + pps
percentage = (total / 500) * 100
grade = calculate_grade(percentage)

# 🔁 Menu Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print(f"🧮 Total Marks: {total}/500")
    elif choice == "2":
        print(f"📈 Percentage: {percentage:.2f}%")
    elif choice == "3":
        print(f"🎖️ Grade: {grade}")
        if grade == 'Fail':
            print("😢 Sorry! You have failed.")
        else:
            print("🎉 Congratulations!")
    elif choice == "4":
        print("\n📚 Subject-wise Marks:")
        print(f"Maths: {math}")
        print(f"Physics: {physics}")
        print(f"Marathi: {marathi}")
        print(f"Chemistry: {chemistry}")
        print(f"PPS: {pps}")
    elif choice == "5":
        print("👋 Thank you for using Smart Grade Analyzer. Goodbye!")
        break
    else:
        print("⚠️ Invalid option. Please choose between 1 to 5.")
