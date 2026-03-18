def top_student(**kwargs):
    top_name = ""
    max_marks = -1
    for name, marks in kwargs.items():
        if marks > max_marks:
            max_marks = marks
            top_name = name
    return top_name
