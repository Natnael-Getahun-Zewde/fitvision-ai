def calculate_score(reps, form_score):

    strength_score = reps * 5

    total = strength_score + form_score

    if total > 90:
        grade = "A"

    elif total > 75:
        grade = "B"

    elif total > 60:
        grade = "C"

    else:
        grade = "D"

    return total, grade