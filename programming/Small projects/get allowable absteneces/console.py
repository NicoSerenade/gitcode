import logic as l

def run_get_max_allowable_absences():
    classes_per_week = float(input("# classes per week: "))
    weeks = float(input("# weeks: "))
    no_class_days = float(input("# no class days: "))
    allowable_percentage = float(input("% Allowable abstenence (0.2): ")) #Be aware if it changes

    allowable_absences = l.get_max_allowable_absences(classes_per_week, weeks, no_class_days, allowable_percentage)
    print(f"Allowable absences: {allowable_absences}")

def run_app():
    print("\nHere you can find out how many absences are allowed in your course at Uniandes.")
    print("\nYour time as a student is the most important thing you have, and it is wise to skip some classes if there's a more important priority calling.")

    run_get_max_allowable_absences()

run_app()