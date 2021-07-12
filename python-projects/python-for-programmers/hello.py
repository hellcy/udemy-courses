
#print("My name is " + input())


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

    print("{} - {}".format(studentname, grade))


# pointspossible = input("what is points possible?")
# score = input("what is your score?")
# studentname = input("what is your name?")

# calculate_score(int(pointspossible), int(score), studentname)

# try:
#     age = int(input())
#     print("valid age")
# except :
#     print(" you need to provide a valid number")
# except ValueError:

try:
    birthyear = int(input("What year were you born?: "))
except Exception as ex:
    print("Please provide a valid number!" + str(ex))
