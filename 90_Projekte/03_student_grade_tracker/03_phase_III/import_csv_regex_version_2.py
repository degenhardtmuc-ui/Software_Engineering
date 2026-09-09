pattern = re.compile(
    r"^(?P<student_id>[^,]+),"
    r"(?P<course_id>[^,]+),"
    r"(?P<score>[0-9]+(?:\.[0-9]+)?),"
    r"(?P<date>\d{4}-\d{2}-\d{2})$"
)
# Diese vier Zeilen müssen geändert werden
student_id = match.group("student_id")
course_id = match.group("course_id")
score = float(match.group("score"))
date = match.group("date")

# Der Vorteil ist, dass man nicht mehr wissen muss, welche Nummer zu welchem Wert gehört