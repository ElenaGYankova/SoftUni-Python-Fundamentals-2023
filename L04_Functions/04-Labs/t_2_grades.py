grade_number = float(input())


def grade_as_text(grade):
    grade_text = ""
    if 2 <= grade <= 2.99:
        return "Fail"
    elif 3 <= grade <= 3.49:
        return "Poor"
    elif 3.5 <= grade <= 4.49:
        return "Good"
    elif 4.5 <= grade <= 5.49:
        return "Very Good"
    elif 5.5 <= grade <= 6:
        return "Excellent"


print(grade_as_text(grade_number))
