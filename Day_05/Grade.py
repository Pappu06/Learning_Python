# Student Grade Calculator using Functions

def calculate_average(marks):
    """Calculate average of marks"""
    return sum(marks) / len(marks)

def calculate_grade(avg):
    """Assign grade based on average"""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def student_report(name, marks):
    """Generate student report"""
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    print(f"\n📄 Report for {name}:")
    print(f"Marks: {marks}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")

# --- Main Program ---
print("**__Welcome to Student Grade Calculator!__**")

while True:
    name = input("\nEnter student name (or 'exit' to quit): ")
    if name.lower() == "exit":
        print("Exiting Grade Calculator. Goodbye!")
        break

    marks = []
    subjects = int(input(f"How many subjects for {name}? "))
    for i in range(subjects):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)

    student_report(name, marks)
