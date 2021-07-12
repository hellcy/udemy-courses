def calculate_score(pointspossible, score=60, studentname="yuan"):
    per = score/pointspossible
    grade = ""

    if 0.9 <= per <= 1:
        grade = "A"
    elif 0.8 <= per <= 0.89:
        grade = "B"
    elif 0.7 <= per <= 0.79:
        grade = "C"
    elif 0.6 <= per <= 0.69:
        grade = "D"
    else:
        grade = "F"

    print("Percentage is {}".format(per))
    print("{} - {}".format(studentname, grade))


calculate_score(100, 80, "nancy")
