def manage_student_database():
    # creating an empty list for storing student tuples and a set for tracking unique names
    students = []
    student_names = set()
    student_id = 1  # Start ID from 1

    while True:
        # Prompt user for input
        name = input("Please enter the student's name (or type 'stop' to finish): ")

        # Check if the user wants to stop input
        if name.lower() == 'stop':
            break

        # Check for duplicate names
        if name in student_names:
            print("This name is already in the list.")
            continue  # Skip to the next iteration of the loop

        # Add the name to the set of unique names and to the student list with a new ID
        student_names.add(name)
        students.append((student_id, name))
        student_id += 1  # Increment ID for the next student

    # Display the complete list of student tuples
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Calculate and display the total number of students
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate and display the total length of all student names combined
    total_length = sum(len(name) for _, name in students)
    print(f"Total length of all student names combined: {total_length}")

    # Identify and display the student with the longest and shortest name
    if students:
        longest_name_student = max(students, key=lambda x: len(x[1]))
        shortest_name_student = min(students, key=lambda x: len(x[1]))

        print(f"The student with the longest name is: {longest_name_student[1]}")
        print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Call the function to run the program
manage_student_database()
