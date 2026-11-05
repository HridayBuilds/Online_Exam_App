
def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total marks must be greater than zero.")
    return (obtained / total) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

if __name__ == "__main__":
    obtained_marks = 85
    total_marks = 100
    pct = calculate_percentage(obtained_marks, total_marks)
    grade = calculate_grade(pct)
    print(f"Percentage: {pct}%, Grade: {grade}")
