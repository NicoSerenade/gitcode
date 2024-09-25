students = []

while True:
    print('Sistema de registro académico SIRA')
    choice = input('1. Add Student\n2. Remove Student\n3. Find Student\n4. List All Students\n5. Exit\nEnter your choice: ')
    if choice == '1':
        name = input('Enter the student\'s name: ').title()
        while True:
            age = input(f'Enter {name}\'s age: ')
            if age.isdigit():
                age = int(age)
                break
            else:
                print('Enter a valid age')
        courses = input(f'Enter {name}\'s courses (comma-separated): ').split(',')
        courses = [course.strip() for course in courses]
        student = {
            'name': name,
            'age': age,
            'courses': courses
         }
        students.append(student)

    elif choice == '2':
        name = input('Enter the student\'s name: ').title()
        found = False
        for student in students:
            if student['name'] == name:
                students.remove(student)
                print(f'Student {name} removed successfully')
                found = True
                break
        if not found:
            print(f'Student {name} not found')

    elif choice == '3':
        name = input('Enter the student\'s name: ').title()
        found = False
        for student in students:
            if student['name'] == name:
                if not student['courses']:
                    print(f"Found student: Name: {student['name']}, Age: {student['age']}, courses: No courses listed")
                else:
                    print(f"Found student: Name: {student['name']}, Age: {student['age']}, courses: {', '.join(student['courses'])}")
                found = True
                break
        if not found:
                print(f'Student {name} not found')

    elif choice == '4':
        if students:
            for x, student in enumerate(students, start= 1):
                if not student['courses']:
                    print(f"{x}. Name: {student['name']}, Age: {student['age']}, courses: No courses listed")
                else:
                    print(f"{x}. Name: {student['name']}, Age: {student['age']}, courses: {', '.join(student['courses'])}")
        else: 
            print('No students in the system')
    
    elif choice == '5':
        while True:
            confirm = input('Are you sure do you want to exit? (yes/no): ').lower()
            if confirm == 'yes':
                print('Have a good day!')
                break

            elif confirm == 'no': 
                break

            else: 
                print('Invalid confirmation')
                
        if confirm == 'yes': 
            break
    else: 
        print('Invalid choice, please try again.')