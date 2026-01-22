def add_student():
    name = input("Enter student name: ")
    scores = []

    for i in range(3):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    return name, scores


def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average


def display_result(name, total, average):
    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total Score:", total)
    print("Average Score:", average)


def main():
    name, scores = add_student()
    total, average = calculate_average(scores)
    display_result(name, total, average)


main()
