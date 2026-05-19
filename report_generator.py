def calc_average(backend, frontend, design):
    avg = (backend + frontend + design) / 3
    return avg

def student_grades(average):
    if average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    elif average<50:
        return "E"
    else:
        return "invalid score"

def student_report(name, backend, frontend, design):
    average = calc_average(backend, frontend, design)
    grade = student_grades(average)
    report={
        "name":name,
        "backend":backend,
        "frontend":frontend,
        "design":design,
        "average":average,
        "grade":grade
    }
    return report
name = input("Enter student name: ")
backend = int(input("Enter backend marks: "))
frontend = int(input("Enter frontend marks: "))
design = int(input("Enter design marks: "))

print(student_report(name, backend, frontend, design))

  



    